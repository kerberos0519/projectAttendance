from fastapi import FastAPI
from numpy import integer

app = FastAPI()

class Attendance():
    pass

@app.get("/")
async def root():
    return {"message": "Hello World"}