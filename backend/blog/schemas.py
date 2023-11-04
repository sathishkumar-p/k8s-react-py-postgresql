from typing import List, Optional,Union
from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):

    id: Union[int, None] = None
    name:str
    email:str
    password:str

    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    name:str
    email:str
    blogs : List[Blog] =[]
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body:str


    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None