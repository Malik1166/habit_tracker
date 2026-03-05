from passlib.context import CryptContext



password_manager = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(user_password: str) -> str:
    hashed_password = password_manager.hash(user_password)
    return hashed_password


def verify_password(input_password: str, saved_hash: str) -> bool:
    result = password_manager.verify(input_password, saved_hash)
    return result
