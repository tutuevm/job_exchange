import bcrypt


class UserManager:

    def hash_password(self, password) -> bytes:
        salt = bcrypt.gensalt()
        pwd_bytes: bytes = password.encode()
        return bcrypt.hashpw(pwd_bytes, salt)

    def validate_password(self, password, hashed_password) -> bool:
        return bcrypt.checkpw(password.encode(), hashed_password)

    def return_jwt(self):
        ...

    def check_jwt(self):
        ...


hp = UserManager().hash_password('qwerty')
print(type(hp))
