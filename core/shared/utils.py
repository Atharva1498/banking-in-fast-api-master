import random
import string

async def send_verification_email(email: str, token: str, reset: bool = False):
    """
    Simulate sending an email with the verification token.
    This can be replaced with actual email-sending logic.
    """
    subject = "Reset Password OTP" if reset else "Verify Your Email"
    body = (
        f"Dear user,\n\n"
        f"Your {'reset password' if reset else 'verification'} OTP is:\n\n"
        f"{token}\n\n"
        f"Thanks,\nYour App Team"
    )
    print(f"Email to {email}: Subject: {subject}, Body: {body}")


def generate_token(length: int = 6) -> str:
    """Generate a random numeric token."""
    return ''.join(random.choices(string.digits, k=length))
