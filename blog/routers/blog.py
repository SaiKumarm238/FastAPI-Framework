from sys import prefix
from fastapi import APIRouter,  Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db
from ..repository import blog
from ..oauth2 import get_current_user

router = APIRouter(
    prefix ='/blog',
    tags=['Blogs']
    )


@router.get('/', response_model =List[schemas.ShowBlog])
def blog_list(db:Session= Depends(get_db), current_user:schemas.User= Depends(get_current_user)):
    return blog.blog_list(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def blog_create(request: schemas.Blog, db:Session= Depends(get_db),  current_user:schemas.User= Depends(get_current_user)):
    return blog.blog_create(request, db)

@router.get('/{id}',status_code =200, response_model =schemas.ShowBlog)
def blog_detail(id:int,db:Session= Depends(get_db),  current_user:schemas.User= Depends(get_current_user)):
    return blog.blog_detail(id,db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def blog_update(id:int, request:schemas.Blog, db:Session= Depends(get_db), current_user:schemas.User= Depends(get_current_user)):
    return blog.blog_update(id,request,db)


@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete_blog(id:int, db:Session= Depends(get_db), current_user:schemas.User= Depends(get_current_user)):
    return blog.blog_delete(id,db)