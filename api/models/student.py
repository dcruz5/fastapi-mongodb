from pydantic import BaseModel

class Student(BaseModel):
    name: str
    sex: str
    grade: int
