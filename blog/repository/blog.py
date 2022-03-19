from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def blog_list(db:Session):
    blog_list = db.query(models.Blog).all()
    return blog_list

def blog_create(request:schemas.Blog, db:Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def blog_detail(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail =f"Blog with the id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message":f"Blog with the id {id} is not available"}
    return blog

def blog_update(id:int, request:schemas.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail =f"Blog with the id {id} is not available")
    blog.update({"title":request.title, "body":request.body}, synchronize_session=False)
    db.commit()
    return {"Message": "Updated Sucessfuly", "data":request}

def blog_delete(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail =f"Blog with the id {id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"Message":f"You deleted the Blog {id}"}