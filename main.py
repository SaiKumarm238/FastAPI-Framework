from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] 

@app.get("/blog")
def index(limit = 10, published: bool = True, sort:Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs from the DB"}
    else:
        return {"data":f"{limit} blog list from DB"}
        


@app.get("/blog/unpublished")
def inpublished():
    return {"data": {"all unpublished blogs"}}


@app.get("/blog/{id}")
def read_item(id: int):
    #fetch blog with id = id
    return {"blog_id": id}


@app.get("/blog/{id}/comments")
def comments(id: int):
    #fetch comments of blog with id = index
    return {"data": {"id":id,
                     "comments": {"1","2"}}}

@app.post("/blog")
def create_blog(request:Blog):
    return {"data": {f"Blog Created title as {request.title}"}}