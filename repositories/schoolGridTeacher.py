from database.database import get_db_connection
from models.schoolGridTeacher import SchoolGridTeacher

def create(school_grid_teacher: SchoolGridTeacher):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO schoolGridTeacher (useId, status) VALUES (%s, %s, %s)",
        (school_grid_teacher.useId, school_grid_teacher.status)
    )

    school_grid_teacher_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return SchoolGridTeacher(id=school_grid_teacher_id, **school_grid_teacher.dict(exclude={"id"}))

def readAll():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM schoolGridTeacher")
    school_grid_teachers = cursor.fetchall()
    cursor.close()
    connection.close()
    return [SchoolGridTeacher(**teacher) for teacher in school_grid_teachers]

def readOne(id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM schoolGridTeacher WHERE id = %s", (id,))
    school_grid_teacher = cursor.fetchone()
    cursor.close()
    connection.close()
    return SchoolGridTeacher(**school_grid_teacher) if school_grid_teacher else None

def update(id: int, school_grid_teacher: SchoolGridTeacher):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE schoolGridTeacher SET useId = %s, schoolGridId = %s, status = %s WHERE id = %s",
        (school_grid_teacher.useId, school_grid_teacher.status, id)
    )

    connection.commit()
    cursor.close()
    connection.close()
    return SchoolGridTeacher(id=id, **school_grid_teacher.dict(exclude={"id"}))

def delete(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM schoolGridTeacher WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
