from database.database import get_db_connection
from models.auxWeekSchedule import AuxWeekSchedule

def create(AuxWeekSchedule: AuxWeekSchedule):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO auxweekschedule (dayOfTheWeekId, classScheduleId, status) VALUES (%s, %s, %s)",
        (AuxWeekSchedule.dayOfTheWeekId, AuxWeekSchedule.classScheduleId, AuxWeekSchedule.status)
    )

    AuxWeekSchedule_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return AuxWeekSchedule(id=AuxWeekSchedule_id, **AuxWeekSchedule.dict(exclude={"id"}))

def readAll():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM auxweekschedule")
    AuxWeekSchedules = cursor.fetchall()
    cursor.close()
    connection.close()
    return [AuxWeekSchedule(**discipline) for discipline in AuxWeekSchedules]

def readOne(id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM auxweekschedule WHERE id = %s", (id,))
    AuxWeekSchedule = cursor.fetchone()
    cursor.close()
    connection.close()
    return AuxWeekSchedule(**AuxWeekSchedule) if AuxWeekSchedule else None

def update(id: int, AuxWeekSchedule: AuxWeekSchedule):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE auxweekschedule SET dayOfTheWeekId = %s, classScheduleId = %s, status = %s WHERE id = %s",
        ( AuxWeekSchedule.dayOfTheWeekId, AuxWeekSchedule.classScheduleId, AuxWeekSchedule.status, id)
    )

    connection.commit()
    cursor.close()
    connection.close()
    return AuxWeekSchedule(id=id, **AuxWeekSchedule.dict(exclude={"id"}))

def delete(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM auxweekschedule WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
