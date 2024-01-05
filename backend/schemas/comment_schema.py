from typing import List
from pydantic import BaseModel

class CommentItem(BaseModel):
    id: int
    comment: List[str]
    userName: List[str]

class CommentArray(BaseModel):
    comments: List[CommentItem]
