def student_entity(student) -> dict:
    return {
            "id": str(student["_id"]),
            "name": student["name"],
            "sex": student["sex"],
            "grade": student["grade"]
            }

def students_entity(students_list) -> list:
    return [student_entity(s) for s in students_list]
