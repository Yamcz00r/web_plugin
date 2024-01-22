from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from utils.database_utils import get_db
from services.user_service import create_user, get_user_by_email, delete_user
import schemas.user_schema as user_schema
import re
from fastapi.middleware.cors import CORSMiddleware
import utils.auth_utils as auth_utils
from typing import Annotated
from schemas.comment_schema import CommentItem, Comments
from services.comment_service import generate_llama_response, toxic_classify
import json
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

email_regex = "^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$"



@app.post("/users/create_user/", response_model=user_schema.UserResponse)
async def create_user_endpoint(user_data: user_schema.UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this email address already exists",
        )
    if len(user_data.password) < 8:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password is too short, must be at least 8 characters"
        )
    if not re.match(email_regex, user_data.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Enter the valid email address"
        )
    user = create_user(db, user_data)
    user_in_db = auth_utils.authenticate_user(user_data.email, user_data.password, db)
    token = await auth_utils.create_token(user_in_db)
    return dict(user=user, access_token=token)


@app.get("/users/me", response_model=user_schema.User)
def read_active_user(
    user: user_schema.User = Depends(auth_utils.get_current_user)
):
    return user


@app.post("/token")
async def generate_user_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = auth_utils.authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",

        )

    token = auth_utils.create_token(user)
    return dict(access_token=token)


@app.post("/users/delete_user/{delete_user_id}")
def delete_user_endpoint(
    delete_user_id: int,
    db: Session = Depends(get_db),
    active_user: user_schema.User = Depends(auth_utils.get_current_user)
):
    if delete_user_id != active_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission"
        )
    delete_user(db=db, user_id=delete_user_id)
    return {"message": f"Successfully, deleted a user {delete_user_id}" }

@app.post("/comments/verify")
def verify(comments: Comments):
    json_comments = comments.model_dump_json()
    print(json_comments)


@app.post("/comments")
def receiving_comments():
    generate_llama_response("hello")