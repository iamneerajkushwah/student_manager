from pydantic import BaseModel

class Student(BaseModel):
    name: str 
    age: int
    course: str


class StudentResponse(BaseModel):
    name: str
    age: int
    course: str

class StudentListResponse(BaseModel):
    total: int
    skip: int
    limit: int
    data: list[StudentResponse]