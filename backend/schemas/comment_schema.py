from typing import List
from pydantic import BaseModel

class CommentItem(BaseModel):
    Id: int
    Comment: List[str]
    Username: List[str]

class CommentArray(BaseModel):
    comments: List[CommentItem]
