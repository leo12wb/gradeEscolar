from fastapi import FastAPI, HTTPException, Request
from database.database import get_db_connection
from routes.classSchedule import router as classSchedule_router
from routes.dayOfTheWeek import router as dayOfTheWeek_router
from routes.schoolGrid import router as schoolGrid_router
from routes.schoolGridDiscipline import router as schoolGridDiscipline_router
from routes.schoolGridTeacher import router as schoolGridTeacher_router
from routes.schoolGridWeekHour import router as schoolGridWeekHour_router
from routes.authToken import router as authToken_router

app = FastAPI()

# Middleware para verificar o token
# @app.middleware("http")
# async def verify_token(request: Request, call_next):
#     token = request.headers.get("Authorization")
#     if not token:
#         raise HTTPException(status_code=403, detail="Token is missing")

#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM authToken WHERE token = %s", (token,))
#     authToken = cursor.fetchone()
#     cursor.close()
#     connection.close()
#     if(authToken):
#       response = await call_next(request)
#       return response
#     else:
#        HTTPException(status_code=403, detail="Token is missing")


# Inclui as rotas
app.include_router(classSchedule_router)
app.include_router(dayOfTheWeek_router)
app.include_router(schoolGrid_router)
app.include_router(schoolGridDiscipline_router)
app.include_router(schoolGridTeacher_router)
app.include_router(schoolGridWeekHour_router)
app.include_router(authToken_router)
