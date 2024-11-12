from database.database import get_db_connection
from models.auxGridDiscipline import AuxGridDiscipline

def create(auxGridDiscipline: AuxGridDiscipline):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO auxgriddiscipline (schoolGridId, schoolGridDisciplineId, status) VALUES (%s, %s, %s)",
        (auxGridDiscipline.schoolGridId, auxGridDiscipline.schoolGridDisciplineId, auxGridDiscipline.status)
    )

    auxGridDiscipline_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return AuxGridDiscipline(id=auxGridDiscipline_id, **auxGridDiscipline.dict(exclude={"id"}))

def readAll():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM auxgriddiscipline")
    auxGridDisciplines = cursor.fetchall()
    cursor.close()
    connection.close()
    return [AuxGridDiscipline(**discipline) for discipline in auxGridDisciplines]

def readOne(id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM auxgriddiscipline WHERE id = %s", (id,))
    auxGridDiscipline = cursor.fetchone()
    cursor.close()
    connection.close()
    return AuxGridDiscipline(**auxGridDiscipline) if auxGridDiscipline else None

def update(id: int, auxGridDiscipline: AuxGridDiscipline):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE auxgriddiscipline SET schoolGridDisciplineId = %s, schoolGridId = %s, status = %s WHERE id = %s",
        ( auxGridDiscipline.schoolGridDisciplineId, auxGridDiscipline.schoolGridId, auxGridDiscipline.status, id)
    )

    connection.commit()
    cursor.close()
    connection.close()
    return AuxGridDiscipline(id=id, **auxGridDiscipline.dict(exclude={"id"}))

def delete(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM auxgriddiscipline WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
