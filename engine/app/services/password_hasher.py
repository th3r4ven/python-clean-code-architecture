from werkzeug.security import generate_password_hash, check_password_hash

class PasswordHasher:
    @staticmethod
    def hash_password(password: str) -> str:
        return generate_password_hash(password)

    @staticmethod
    def check_password(password: str, hashed_password: str) -> bool:
        return check_password_hash(hashed_password, password)
