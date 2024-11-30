from tortoise import fields, models
from passlib.context import CryptContext
from datetime import datetime, timedelta


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    hashed_password = fields.CharField(max_length=128)
    is_active = fields.BooleanField(default=True)
    is_email_verified = fields.BooleanField(default=False)
    otp = fields.CharField(max_length=6, null=True)  # Store OTP
    otp_expiration = fields.DatetimeField(null=True)  # OTP expiration time

    def set_password(self, password: str):
        self.hashed_password = pwd_context.hash(password)

    def check_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.hashed_password)

    class Meta:
        table = "users"
