from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    # name: str 
    name: str = 'Rahul Singh'
    age: Optional[int] = None
    email: EmailStr
    cgpa: Optional[float] = Field( gt=0.0, lt=10.0, default=5.0, description='A decimal value representing the cgpa of the student.')  # cgpa must be between 0.0 and 10.0

# new_student = {'name' : 'Rahul Singh'} # if you pass integer here, it will raise an error, this was not the case in TypedDict
new_student = {'age': 21, 'email':'abc@gmail.com'} # coerce to default value - if you pass string to age like '21', it automatically converts it to integer

student = Student(**new_student)
# print(student.name)  # Output: Rahul Singh
# print(student)  # Output: name='Rahul Singh'

print(student.model_dump())  # Output: {'name': 'Rahul Singh', 'age': 21, 'email': None, 'cgpa': 5.0}
print(student.model_dump_json())  # Output: JSON representation of the student object