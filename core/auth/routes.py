from fastapi import APIRouter, HTTPException
from core.auth.models import User
from core.auth.schemas import (
    UserLoginSchema,
    UserRegisterSchema,
    EmailVerificationSchema,
    PasswordResetSchema,
)
from core.shared.utils import send_verification_email
from datetime import datetime, timedelta

auth_router = APIRouter()

# POST: Register a new user
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

    # Send verification email
    await send_verification_email(user.email)

    return {"message": "User registered. A verification email has been sent."}

# GET: Retrieve user details
@auth_router.get("/user/{email}")
async def get_user_details(email: str):
    user = await User.filter(email=email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "user_id": user.id,
        "username": user.username,
        "email": user.email,
        "is_active": user.is_active,
        "is_email_verified": user.is_email_verified,
    }

# POST: Verify email with OTP
@auth_router.post("/verify-email/")
async def verify_email(data: EmailVerificationSchema):
    user = await User.filter(email=data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.is_email_verified = True
    await user.save()

    return {"message": "Email verified successfully."}

# GET: Check registration status
@auth_router.get("/registration-status/{email}")
async def check_registration_status(email: str):
    user = await User.filter(email=email).first()
    if not user:
        return {"registered": False, "message": "Email not registered"}
    return {"registered": True, "is_email_verified": user.is_email_verified}

# POST: Login a user
@auth_router.post("/login/")
async def login(data: UserLoginSchema):
    user = await User.filter(email=data.email).first()
    if not user or not user.check_password(data.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not user.is_email_verified:
        raise HTTPException(status_code=400, detail="Email not verified")

    return {"message": "Login successful."}

# POST: Forgot password
@auth_router.post("/forgot-password/")
async def forgot_password(data: EmailVerificationSchema):
    user = await User.filter(email=data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Send a password reset email
    await send_verification_email(user.email, reset=True)

    return {"message": "Password reset email sent."}

# POST: Reset password
@auth_router.post("/reset-password/")
async def reset_password(data: PasswordResetSchema):
    user = await User.filter(email=data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.set_password(data.new_password)
    await user.save()

    return {"message": "Password reset successfully."}
