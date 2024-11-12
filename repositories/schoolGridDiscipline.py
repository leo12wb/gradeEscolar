from database.database import get_db_connection
from models.schoolGridDiscipline import SchoolGridDiscipline

def create(school_grid_discipline: SchoolGridDiscipline):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO schoolGridDiscipline (schoolGridTeacherId, disciplineId, status) VALUES (%s, %s, %s)",
        (school_grid_discipline.schoolGridTeacherId, school_grid_discipline.disciplineId, school_grid_discipline.status)
    )

    school_grid_discipline_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return SchoolGridDiscipline(id=school_grid_discipline_id, **school_grid_discipline.dict(exclude={"id"}))

def readAll():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM schoolGridDiscipline")
    school_grid_disciplines = cursor.fetchall()
    cursor.close()
    connection.close()
    return [SchoolGridDiscipline(**discipline) for discipline in school_grid_disciplines]

def readOne(id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM schoolGridDiscipline WHERE id = %s", (id,))
    school_grid_discipline = cursor.fetchone()
    cursor.close()
    connection.close()
    return SchoolGridDiscipline(**school_grid_discipline) if school_grid_discipline else None

def update(id: int, school_grid_discipline: SchoolGridDiscipline):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE schoolGridDiscipline SET schoolGridTeacherId = %s, disciplineId = %s, status = %s WHERE id = %s",
        (school_grid_discipline.schoolGridTeacherId, school_grid_discipline.disciplineId, school_grid_discipline.status, id)
    )

    connection.commit()
    cursor.close()
    connection.close()
    return SchoolGridDiscipline(id=id, **school_grid_discipline.dict(exclude={"id"}))

def delete(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM schoolGridDiscipline WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
