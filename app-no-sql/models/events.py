#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

from pydantic import BaseModel


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
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
