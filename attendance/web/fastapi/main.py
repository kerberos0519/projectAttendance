from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder

import sys
sys.path.append('.')
sys.path.append('I:/AI/kjh/dev/python/src/projectAttendance/attendance')

import db

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class Attendance():
    pass

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/attendance/list")
async def attendanceList(request: Request, dt:str):
    rows = db.selectAttendanceByDate(dt)
    print(rows)
    return templates.TemplateResponse("list.html", {"request": request, "attendanceList": rows, "dt" : dt})

@app.get("/attendance/list/json")
async def attendanceListJson(request: Request, dt:str):
    rows = db.selectAttendanceByDate(dt)
    print(rows)
    return jsonable_encoder(rows)

@app.get("/attendance/input")
async def attendanceInput(request: Request, name:str, dt:str):
    resultYn = ''

    try:
        db.doAttend(name, dt)
        resultYn = 'Y'
    except :
        resultYn = 'N'

    return templates.TemplateResponse("index.html", {"request": request, "inputSuccYn": resultYn})