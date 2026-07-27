# pip install pyotp
import pyotp


def get_totp_code(key: str) -> str:
    """
    Generates a TOTP code from a Base32 secret key.
    
    Args:
        key: Base32 encoded secret key
    
    Returns:
        6-digit OTP code as a string
    """
    if not key:
        raise ValueError("Missing TOTP secret key")
    
    totp = pyotp.TOTP(key)
    return totp.now()

# key = "JBSWY3DPEHPK3PXP" #Sample key for testing
# print("OTP:", get_totp_code(key))
