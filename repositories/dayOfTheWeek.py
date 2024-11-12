from database.database import get_db_connection
from models.dayOfTheWeek import DayOfTheWeek

def create(day_of_the_week: DayOfTheWeek):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO dayOfTheWeek (week, abbreviation, status) VALUES (%s, %s, %s)",
        (day_of_the_week.week, day_of_the_week.abbreviation, day_of_the_week.status)
    )

    day_of_the_week_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return DayOfTheWeek(id=day_of_the_week_id, **day_of_the_week.dict(exclude={"id"}))

def readAll():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM dayOfTheWeek")
    days_of_the_week = cursor.fetchall()
    cursor.close()
    connection.close()
    return [DayOfTheWeek(**day) for day in days_of_the_week]

def readOne(id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM dayOfTheWeek WHERE id = %s", (id,))
    day_of_the_week = cursor.fetchone()
    cursor.close()
    connection.close()
    return DayOfTheWeek(**day_of_the_week) if day_of_the_week else None

def update(id: int, day_of_the_week: DayOfTheWeek):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE dayOfTheWeek SET week = %s, abbreviation = %s, status = %s WHERE id = %s",
        (day_of_the_week.week, day_of_the_week.abbreviation, day_of_the_week.status, id)
    )

    connection.commit()
    cursor.close()
    connection.close()
    return DayOfTheWeek(id=id, **day_of_the_week.dict(exclude={"id"}))

def delete(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM dayOfTheWeek WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
