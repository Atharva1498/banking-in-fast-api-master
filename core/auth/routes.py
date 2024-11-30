from fastapi import APIRouter, HTTPException
from core.auth.models import User
from core.auth.schemas import (
    UserLoginSchema,
    UserRegisterSchema,
    EmailVerificationSchema,
    OTPVerificationSchema,
    PasswordResetSchema,
)
from core.shared.utils import generate_token, send_verification_email
from datetime import datetime, timedelta
import random

auth_router = APIRouter()


@auth_router.post("/register/")
async def register_user(data: UserRegisterSchema):
    user_exists = await User.filter(email=data.email).exists()
    if user_exists:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        username=data.username,
        email=data.email,
    )
    user.set_password(data.password)
    await user.save()

    # Generate OTP for email verification
    otp = generate_token(6)
    user.otp = otp
    user.otp_expiration = datetime.utcnow() + timedelta(minutes=10)
    await user.save()

    # Send verification email
    await send_verification_email(user.email, otp)

    return {"message": "User registered. Verify your email using the OTP sent."}


@auth_router.post("/verify-email/")
async def verify_email(data: OTPVerificationSchema):
    user = await User.filter(email=data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.otp != data.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    if datetime.utcnow() > user.otp_expiration:
        raise HTTPException(status_code=400, detail="OTP expired")

    user.is_email_verified = True
    user.otp = None
    user.otp_expiration = None
    await user.save()

    return {"message": "Email verified successfully."}


@auth_router.post("/login/")
async def login(data: UserLoginSchema):
    user = await User.filter(email=data.email).first()
    if not user or not user.check_password(data.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not user.is_email_verified:
        raise HTTPException(status_code=400, detail="Email not verified")

    return {"message": "Login successful."}


@auth_router.post("/forgot-password/")
async def forgot_password(data: EmailVerificationSchema):
    user = await User.filter(email=data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Generate OTP for password reset
    otp = generate_token(6)
    user.otp = otp
    user.otp_expiration = datetime.utcnow() + timedelta(minutes=10)
    await user.save()

    # Send OTP via email
    await send_verification_email(user.email, otp, reset=True)

    return {"message": "OTP sent to your email for password reset."}


@auth_router.post("/reset-password/")
async def reset_password(data: PasswordResetSchema):
    user = await User.filter(email=data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.otp != data.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    if datetime.utcnow() > user.otp_expiration:
        raise HTTPException(status_code=400, detail="OTP expired")

    user.set_password(data.new_password)
    user.otp = None
    user.otp_expiration = None
    await user.save()

    return {"message": "Password reset successfully."}
