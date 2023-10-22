from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Employee(BaseModel):
    name: str
    email: str
    age: int
    company: str
    join_date: str
    job_title: str
    gender: str
    salary: int


client = MongoClient("mongodb://db:27017/")
db = client["mydatabase"]
collection = db["mycollection"]


@app.get("/employees")
async def get_employees_mail(email: str) -> List[Employee]:
    employees = []
    for employee in collection.find({"email": email}):
        employees.append(Employee(**employee))
    return employees


@app.get("/employees_gen")
async def get_employees_gen(gender: str) -> List[Employee]:
    employees = []
    for employee in collection.find({"gender": gender}):
        employees.append(Employee(**employee))
    return employees
