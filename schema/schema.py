from pydantic import BaseModel

class MemberSchema(BaseModel):
    email: str 
    fullName: str 
    track: str 
    completed: bool = True
    password: str | None = None
    is_mentor: bool = False

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "email": "john@example.com",
                "fullName": "John Doe",
                "track": "Python",
                "completed": True,
                "is_mentor": False,
                "password": "password123",}
        }
