#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form


class Todo(BaseModel):
    """Todo."""

    id: Optional[int]
    item: str

    @classmethod
    def as_form(
            cls,
            id: Optional[int] = Form(None),
            item: str = Form(...),
    ):
        return cls(id=id, item=item)

    class Config:
        """Config."""

        json_schema_extra = {"example": {"id": 1, "item": "Buy milk"}}


class TodoItem(BaseModel):
    """TodoItem."""

    item: str

    class Config:
        """Config."""

        json_schema_extra = {"example": {"item": "Buy milk"}}


class TodoItems(BaseModel):
    """TodoItems."""

    todos: List[TodoItem]

    class Config:
        """Config."""

        json_schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Buy milk"
                    },
                    {
                        "item": "Buy eggs"
                    },
                    {
                        "item": "Make appointment"
                    },
                ]
            }
        }
