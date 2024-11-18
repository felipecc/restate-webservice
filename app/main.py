from fastapi import FastAPI
from pydantic import BaseModel
from sqlmodel import create_engine, Session
from app.models import User
import uuid


engine = create_engine("sqlite:///database.db")
app = FastAPI()


class UserRequest(BaseModel):
    id: str
    name: str
    email: str


@app.get("/uuid")
def get_uuid():
    return {"uuid": str(uuid.uuid4())}


@app.post("/user")
def create_user(user_request: UserRequest):
    with Session(engine) as session:
        user = User(
            name=user_request.name, email=user_request.email, id=user_request.id
        )
        session.add(user)
        session.commit()
        session.refresh(user)
    return {"user": user}
