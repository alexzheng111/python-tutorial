from fastapi import FastAPI
from fastapi_tutorial.models.user import User

app = FastAPI()


@app.get("/hello")
def read_hello():
    return {"message": "Hello World!"}


@app.get("/users/{user_id}")
def get_user() -> User:
    return {
        "id": "asdf",
        "email": "alexzhengalt@gmail.com",
        "hashed_password": "asdfasdfa",
        "asdfa": 1,  # Gets stripped out
    }
