from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

import uvicorn
app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.get("/")
def index():
    return {"data":{"name":"Alok"}}

@app.get("/blog")
def index(limit=10, published: bool=True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the database'}
    return {"data": f'{limit} blogs from the database'}

@app.get('/blog/unpublished')
def unpublished():
    return {"data":"all unpublished blogs"}

@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}

@app.get("/blog/{id}/comments")
def comments(id):
    return {'data':["comment_1", "comment_2"]}

@app.post("/blog")
def create_blog(request: Blog):
    return {"data": f"Blog is created title as {request.title}"}

if __name__=='__main__':
    uvicorn.run(app, host="127.0.0.1", port=9000)
