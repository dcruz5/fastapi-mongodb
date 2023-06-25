from fastapi import APIRouter, HTTPException
from models.student import Student
from schemas import students_entity, student_entity
from config.db import collection
from bson import ObjectId

router = APIRouter(tags=['students'])

@router.get('/students')
def list_students():
    return students_entity(collection.find())
 

@router.get("/students/{id}") 
def read_student(id: str):
    student = collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_entity(student)
    raise HTTPException(status_code=404, detail="Student not found")


@router.post('/students', status_code=201)
def create_student(student: Student):
    student_id = collection.insert_one(dict(student)).inserted_id
    return {'message': f"The User ID is {student_id}"}


@router.put('/students/{id}')
def update_student(id: str, student: Student):
    result = collection.find_one_and_update({"_id": ObjectId(id)}, { "$set": dict(student)})
    if result:
        return {"message": "Student updated successfully"}
    raise HTTPException(status_code=404, detail="Student not found") 


@router.delete('/students/{id}')
def delete_student(id: str):
    result = collection.find_one_and_delete({"_id": ObjectId(id)})
    if result:
        return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")
