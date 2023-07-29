#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Evento 1",
                "image": "https://i.imgur.com/4NZ6uLY.jpg",
                "description": "Evento 1",
                "tags": ["tag1", "tag2"],
                "location": "location1"
            }
        }


class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]] = Field(sa_column=Column(JSON))
    location: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Evento 1",
                "image": "https://i.imgur.com/4NZ6uLY.jpg",
                "description": "Evento 1",
                "tags": ["tag1", "tag2"],
                "location": "location1"
            }
        }
