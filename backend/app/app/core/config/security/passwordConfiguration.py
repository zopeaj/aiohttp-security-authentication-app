from passlib.context import CryptContext

class PasswordConfiguration:
    def __init__(self):
        self.bCryptPassword = CryptContext(scheme=['bcrypt'])

    def hash_password(plain_password: str) -> str:
        return self.bCryptPassword.hash(plain_password)

    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return self.bCryptPassword.verify(plain_password, hashed_password)

