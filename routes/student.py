from fastapi import APIRouter, HTTPException
from models.student import Student
from database import student_collections
from typing import Optional

router = APIRouter()

@router.get("/students")
def view_all(course: str | None = None):

    if course:
        students = list(
            student_collections.find(
                {"course":course}
            )
        )

    else:
        students = list(
            student_collections.find()
        )


    for student in students:
        student["_id"] = str(student["_id"])

        return {"Students": students}
    


@router.post("/students")
def add(newstudent: Student):
    existing_student = student_collections.find_one({"name": newstudent.name})

    if existing_student:
        raise HTTPException(status_code=400, detail="Student Already Exists In DB")

    student_collections.insert_one(
        {"name": newstudent.name, "age": newstudent.age, "course": newstudent.course}
    )

    return {"message": "Student Added Successfully In DB", "student": newstudent}






@router.get("/students/{name}")
def view_one(name: str):
    student = student_collections.find_one({"name": name})

    if not student:
        raise HTTPException(status_code=404, detail="Student Doesn't Exist In DB")

    student["_id"] = str(student["_id"])

    return {"Student": student}




@router.put("/students/{name}")
def update_one(studentnewdata: Student, name: str):
    student = student_collections.find_one({"name": name})

    if not student:
        raise HTTPException(status_code=404, detail="Student Doesn't Exist In DB")

    student_collections.update_one(
        {"name": name},
        {
            "$set": {
                "name": studentnewdata.name,
                "age": studentnewdata.age,
                "course": studentnewdata.course,
            }
        },
    )

    return {"message": "Student Updated Successfully", "student": studentnewdata}



@router.delete("/students/{name}")
def delete_one(name: str):
    student = student_collections.find_one({"name": name})

    if not student:
        raise HTTPException(status_code=404, detail="Student Doesn't Exist In DB")

    student_collections.delete_one({"name": name})

    return {"message": "Student Deleted Successfully"}

