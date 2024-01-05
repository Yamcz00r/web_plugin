from typing import List
from pydantic import BaseModel


class CommentItem(BaseModel):
    id: int
    userName: str
    comment: str


class Comments(BaseModel):
    comments: List[CommentItem]
