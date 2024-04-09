import bson
from fastapi import APIRouter, HTTPException
from models.student import Student
from config.db import database

router = APIRouter()


# @router.get("/")
# def demo():
#     return {"Hello"}


@router.post("/", status_code=201)
async def create_student(student: Student):
    curr_student=database["student"].insert_one(student.dict())
    return {"id" : str(curr_student.inserted_id)}

@router.get("/" , status_code=200)
async def get_students(country: str = None, age: int = None):
    filtered_data={}
    if (country!=None):
        filtered_data["address.country"] = country
    if(age!=None):
        filtered_data["age"] = {"$gte": age}

    ans = list(database["student"].find(filtered_data, {"_id": 0}))
    return {"data": ans}


@router.get("/{id}", status_code=200)
async def get_student(id:str):
    student = database["student"].find_one({"_id": bson.ObjectId(id)}, {"_id": 0})
    if student:
        return student
    else:
        raise HTTPException(status_code=404, detail="Student not found")
    return {}


@router.patch("/{id}", status_code=204 )
async def update_student(id: str, student: Student):
    result = database["student"].update_one(
        {"_id": bson.ObjectId(id)},
        {"$set": student.dict(exclude_unset=True)}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {}


@router.delete("/{id}", status_code=200)
async def delete_student(id: str):
    result = database["student"].delete_one({"_id": bson.ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {}