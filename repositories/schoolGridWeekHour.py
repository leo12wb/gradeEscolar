from database.database import get_db_connection
from models.schoolGridWeekHour import SchoolGridWeekHour

def create(school_grid_week_hour: SchoolGridWeekHour):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO schoolGridWeekHour (schoolGridId,auxGridDisciplineId, status) VALUES (%s, %s, %s, %s)",
        (school_grid_week_hour.schoolGridId, school_grid_week_hour.auxGridDisciplineId, school_grid_week_hour.status)
    )

    school_grid_week_hour_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return SchoolGridWeekHour(id=school_grid_week_hour_id, **school_grid_week_hour.dict(exclude={"id"}))

def readAll():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM schoolGridWeekHour")
    school_grid_week_hours = cursor.fetchall()
    cursor.close()
    connection.close()
    return [SchoolGridWeekHour(**hour) for hour in school_grid_week_hours]

def readOne(id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM schoolGridWeekHour WHERE id = %s", (id,))
    school_grid_week_hour = cursor.fetchone()
    cursor.close()
    connection.close()
    return SchoolGridWeekHour(**school_grid_week_hour) if school_grid_week_hour else None

def update(id: int, school_grid_week_hour: SchoolGridWeekHour):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE schoolGridWeekHour SET schoolGridId = %s, auxGridDisciplineId = %s, status = %s WHERE id = %s",
        (school_grid_week_hour.schoolGridId, school_grid_week_hour.auxGridDisciplineId, school_grid_week_hour.status, id)
    )

    connection.commit()
    cursor.close()
    connection.close()
    return SchoolGridWeekHour(id=id, **school_grid_week_hour.dict(exclude={"id"}))

def delete(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM schoolGridWeekHour WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
