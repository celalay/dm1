from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Data models
class Blog(BaseModel):
    id: int
    title: str
    content: str
    author: str
    publication_date: str

class Comment(BaseModel):
    id: int
    content: str
    author: str
    publication_date: str
    blog_id: int

# Sample data
blogs = []
comments = []

# API endpoints
@app.get("/blogs", response_model=List[Blog])
def get_all_blogs():
    return blogs

@app.post("/blogs", response_model=Blog)
def add_new_blog(blog: Blog):
    blogs.append(blog)
    return blog

@app.get("/blogs/{id}", response_model=Blog)
def get_blog(id: int):
    for blog in blogs:
        if blog.id == id:
            return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@app.put("/blogs/{id}", response_model=Blog)
def update_blog(id: int, updated_blog: Blog):
    for blog in blogs:
        if blog.id == id:
            blog.title = updated_blog.title
            blog.content = updated_blog.content
            blog.author = updated_blog.author
            blog.publication_date = updated_blog.publication_date
            return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@app.delete("/blogs/{id}")
def delete_blog(id: int):
    for blog in blogs:
        if blog.id == id:
            blogs.remove(blog)
            return {"message": "Blog deleted"}
    raise HTTPException(status_code=404, detail="Blog not found")

@app.get("/blogs/{id}/comments", response_model=List[Comment])
def get_all_comments(id: int):
    blog_comments = [comment for comment in comments if comment.blog_id == id]
    return blog_comments

@app.post("/blogs/{id}/comments", response_model=Comment)
def add_new_comment(id: int, comment: Comment):
    comment.blog_id = id
    comments.append(comment)
    return comment

@app.get("/blogs/{id}/comments/{comment_id}", response_model=Comment)
def get_comment(id: int, comment_id: int):
    for comment in comments:
        if comment.blog_id == id and comment.id == comment_id:
            return comment
    raise HTTPException(status_code=404, detail="Comment not found")

@app.put("/blogs/{id}/comments/{comment_id}", response_model=Comment)
def update_comment(id: int, comment_id: int, updated_comment: Comment):
    for comment in comments:
        if comment.blog_id == id and comment.id == comment_id:
            comment.content = updated_comment.content
            comment.author = updated_comment.author
            comment.publication_date = updated_comment.publication_date
            return comment
    raise HTTPException(status_code=404, detail="Comment not found")

@app.delete("/blogs/{id}/comments/{comment_id}")
def delete_comment(id: int, comment_id: int):
    for comment in comments:
        if comment.blog_id == id and comment.id == comment_id:
            comments.remove(comment)
            return {"message": "Comment deleted"}
    raise HTTPException(status_code=404, detail="Comment not found")
