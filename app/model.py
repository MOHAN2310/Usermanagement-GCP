from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    email: EmailStr
    project_id: str
    user_id: str = None
