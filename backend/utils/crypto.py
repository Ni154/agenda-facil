import base64
from cryptography.fernet import Fernet
from backend.core.settings import settings

def get_fernet():
    key = settings.ENCRYPTION_SECRET
    try:
        # Expect base64 urlsafe 32 bytes string
        base64.urlsafe_b64decode(key)
        fkey = key
    except Exception:
        # Derive/normalize (NOT strong; for demo only). Replace in production.
        fkey = base64.urlsafe_b64encode(key.encode("utf-8").ljust(32, b"0")[:32])
    return Fernet(fkey)
