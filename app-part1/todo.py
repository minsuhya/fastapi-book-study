#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from .model import Todo, TodoItem, TodoItems

todo_router = APIRouter()

todo_list = []
templates = Jinja2Templates(directory="app/templates")


@todo_router.post("/todo", status_code=201)
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list
    })
    #  return {"message": "Todo added successfully."}


@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo(request: Request):
    #  return {"todos": todo_list}
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list
    })


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(request: Request,
                          todo_id: int = Path(
                              ..., title="The ID of the todo to retrieve.")):
    for todo in todo_list:
        if todo.id == todo_id:
            #  return {"todo": todo}
            return templates.TemplateResponse("todo.html", {
                "request": request,
                "todo": todo
            })
    #  return {"message": "Todo not found."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Todo with id {todo_id} not found.",
    )


@todo_router.put("/todo/{todo_id}")
async def update_todo(
    todo_data: TodoItem,
    todo_id: int = Path(..., title="The ID of the todo to update.")
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Todo updated successfully."}
    #  return {"message": "Todo not found."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Todo with id {todo_id} not found.",
    )


@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo_list.remove(todo)
            return {"message": "Todo deleted successfully."}
    #  return {"message": "Todo not found."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Todo with id {todo_id} not found.",
    )


@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {"message": "Todo deleted successfully."}
