from database.database import get_db_connection
from models.classSchedule import ClassSchedule

def create(class_schedule: ClassSchedule):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO classSchedule (order, start_date, end_date, status) VALUES (%s, %s, %s)",
        ( class_schedule.order, class_schedule.start_date, class_schedule.end_date, class_schedule.status)
    )

    class_schedule_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return ClassSchedule(id=class_schedule_id, **class_schedule.dict(exclude={"id"}))

def readAll():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM classSchedule")
    class_schedules = cursor.fetchall()
    cursor.close()
    connection.close()
    return [ClassSchedule(**schedule) for schedule in class_schedules]

def readOne(id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM classSchedule WHERE id = %s", (id,))
    class_schedule = cursor.fetchone()
    cursor.close()
    connection.close()
    return ClassSchedule(**class_schedule) if class_schedule else None

def update(id: int, class_schedule: ClassSchedule):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE classSchedule SET order = %s, start_date = %s, end_date = %s, status = %s WHERE id = %s",
        (class_schedule.order, class_schedule.start_date, class_schedule.end_date, class_schedule.status, id)
    )

    connection.commit()
    cursor.close()
    connection.close()
    return ClassSchedule(id=id, **class_schedule.dict(exclude={"id"}))

def delete(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM classSchedule WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
