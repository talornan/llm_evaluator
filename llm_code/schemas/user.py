from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    user_type: str
    email: str