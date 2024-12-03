async def send_verification_email(email: str, reset: bool = False):
    """
    Simulates sending a verification email for registration or password reset.
    Replace this with actual email-sending logic using an email service.
    """
    subject = "Reset Password Request" if reset else "Verify Your Email"
    body = (
        f"Dear user,\n\n"
        f"{'Click here to reset your password' if reset else 'Click here to verify your email'}: "
        f"http://localhost:8000/api/auth/{'reset-password' if reset else 'verify-email'}?email={email}\n\n"
        f"Thanks,\nYour App Team"
    )
    print(f"Sending email to {email}: Subject: {subject}, Body: {body}")
