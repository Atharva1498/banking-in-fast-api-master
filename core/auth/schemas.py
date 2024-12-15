from pydantic import BaseModel, EmailStr, validator
from typing import Optional


# User registration schema
class UserRegisterSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    confirm_password: str

    @validator("confirm_password")
    def passwords_match(cls, confirm_password, values):
        if "password" in values and confirm_password != values["password"]:
            raise ValueError("Passwords do not match")
        return confirm_password

    class Config:
        orm_mode = True


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class EmailVerificationSchema(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True

class PasswordResetSchema(BaseModel):
    email: EmailStr
    new_password: str
    confirm_new_password: str

    @validator("confirm_new_password")
    def passwords_match(cls, confirm_new_password, values):
        if "new_password" in values and confirm_new_password != values["new_password"]:
            raise ValueError("Passwords do not match")
        return confirm_new_password

    class Config:
        orm_mode = True
