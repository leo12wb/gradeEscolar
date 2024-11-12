from database.database import get_db_connection
from models.authToken import AuthToken

def create(authToken: AuthToken):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO authToken (token, appId, status) VALUES (%s, %s, %s)",
        ( authToken.token, authToken.appId, authToken.status)
    )

    authToken_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return AuthToken(id=authToken_id, **authToken.dict(exclude={"id"}))

def readAll():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM authToken")
    authTokens = cursor.fetchall()
    cursor.close()
    connection.close()
    return [AuthToken(**auth) for auth in authTokens]

def readOne(id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM authToken WHERE id = %s", (id,))
    authToken = cursor.fetchone()
    cursor.close()
    connection.close()
    return AuthToken(**authToken) if authToken else None

def update(id: int, authToken: AuthToken):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE authToken SET token = %s, appId = %s, status = %s WHERE id = %s",
        (authToken.token, authToken.appId, authToken.status, id)
    )

    connection.commit()
    cursor.close()
    connection.close()
    return AuthToken(id=id, **authToken.dict(exclude={"id"}))

def delete(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM authToken WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
