class User:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    def validate_password(self):
        """Ensure the password has at least 1 uppercase letter, 6 characters, and 1 number."""
        import re
        pattern = r"^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$"
        if not re.match(pattern, self.password):
            raise ValueError("Password must contain at least 6 characters, 1 uppercase letter, and 1 number.")
