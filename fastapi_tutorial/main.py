from dotenv import dotenv_values
from fastapi import FastAPI
import uvicorn
from fastapi_tutorial.models.user import User

app = FastAPI()

config = {**dotenv_values()}


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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
