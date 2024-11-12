from database.database import get_db_connection
from models.schoolGrid import SchoolGrid
# from models.auxGridDiscipline import AuxGridDiscipline

def create(school_grid: SchoolGrid):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO schoolGrid (schoolId, segmentId, serieId, classId, status) VALUES (%s, %s, %s, %s, %s)",
        (school_grid.schoolId, school_grid.segmentId, school_grid.serieId, school_grid.classId, school_grid.status)
    )

    school_grid_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return SchoolGrid(id=school_grid_id, **school_grid.dict(exclude={"id"}))

def readAll():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM schoolGrid")
    school_grids = cursor.fetchall()
    cursor.close()
    connection.close()
    return school_grids
    #return [SchoolGrid(**grid) for grid in school_grids]

def readOne(id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM schoolGrid WHERE id = %s", (id,))
    school_grid = cursor.fetchone()
    cursor.close()
    connection.close()
    return school_grid if school_grid else None
    #return SchoolGrid(**school_grid) if school_grid else None

def readOneFull(id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT 
        sg.id AS school_grid_id,
        sg.schoolId,
        sg.segmentId,
        sg.serieId,
        sg.classId,
        sg.status AS school_grid_status,
        d.id AS day_of_week_id,
        d.week AS day_of_week,
        d.abbreviation AS day_abbreviation,
        d.ordem AS day_order,
        d.status AS day_status,
        sh.id AS school_grid_week_hour_id,
        cs.id AS class_schedule_id,  
        cs.ordem AS hour_order,
        cs.start_date,
        cs.end_date,
        sh.status AS hour_status,
        sd.schoolGridTeacherId,
        sd.disciplineId,
        sd.status AS discipline_status
    FROM 
        SchoolGrid sg
    JOIN 
        SchoolGridWeekHour sh ON sg.id = sh.schoolGridId
    JOIN 
        AuxGridWeekHour agh ON sh.id = agh.schoolGridWeekHourId
    JOIN 
        AuxWeekSchedule aws ON agh.auxWeekScheduleId = aws.classScheduleId
    JOIN 
        DayOfTheWeek d ON aws.dayOfTheWeekId = d.id
    JOIN 
        ClassSchedule cs ON aws.classScheduleId = cs.id
    JOIN 
        SchoolGridDiscipline sd ON sd.schoolGridTeacherId = sg.id
    WHERE 
        sg.id = %s
    ORDER BY 
        d.ordem, cs.ordem;
    """

    cursor.execute(query, (id,))
    rows = cursor.fetchall()

    if not rows:
        return {"message": "No data found for the given school grid id."}

    response = {
        "id": id,
        "schoolId": rows[0]['schoolId'],
        "segmentId": rows[0]['segmentId'],
        "serieId": rows[0]['serieId'],
        "classId": rows[0]['classId'],
        "status": rows[0]['school_grid_status'],
        "dayWeek": []
    }

    day_of_week_map = {}

    for row in rows:
        # Agrupar os dados por "week" (dia da semana)
        if row['day_of_week'] not in day_of_week_map:
            day_of_week_map[row['day_of_week']] = {
                "id": row['day_of_week_id'],
                "week": row['day_of_week'],
                "abbreviation": row['day_abbreviation'],
                "ordem": row['day_order'],
                "status": row['day_status'],
                "hours": []
            }

        # Adicionar as informações de hora para o dia da semana correto
        day_of_week_map[row['day_of_week']]['hours'].append({
            "class_schedule_id": row['class_schedule_id'],  # Incluindo o ID da ClassSchedule
            "ordem": row['hour_order'],
            "start_date": row['start_date'],
            "end_date": row['end_date'],
            "status": row['hour_status'],
            "discipline": {
                "schoolGridTeacherId": row['schoolGridTeacherId'],
                "disciplineId": row['disciplineId'],
                "status": row['discipline_status']
            }
        })

    # Converter o dicionário para uma lista
    response["dayWeek"] = list(day_of_week_map.values())

    cursor.close()
    connection.close()

    return response


def update(id: int, school_grid: SchoolGrid):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE schoolGrid SET schoolId = %s, segmentId = %s, serieId = %s, classId = %s, status = %s WHERE id = %s",
        (school_grid.schoolId, school_grid.segmentId, school_grid.serieId, school_grid.classId, school_grid.status, id)
    )

    connection.commit()
    cursor.close()
    connection.close()
    return SchoolGrid(id=id, **school_grid.dict(exclude={"id"}))

def delete(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM schoolGrid WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
