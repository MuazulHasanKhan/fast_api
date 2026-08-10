# the purpose of this module is to encapsulate utility functions related to user data and password hashing
# Act as  a helper module for the main applications

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "hashed_password": pwd_context.hash("secret"),
}
}

def get_user(username: str):
    user = fake_users_db.get(username)
    if user:
        return user
    return None


def verify_password(plain_password, hash_password):
    return pwd_context.verify(plain_password, hash_password)

