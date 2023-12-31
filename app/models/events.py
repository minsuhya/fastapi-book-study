#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Optional

from beanie import Document
from pydantic import BaseModel


class Event(Document):
    creator: Optional[str]
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "creator": "Creator",
                "title": "Evento 1",
                "image": "https://i.imgur.com/4NZ6uLY.jpg",
                "description": "Evento 1",
                "tags": ["tag1", "tag2"],
                "location": "location1"
            }
        }

    class Settings:
        """Settings."""

        name = "events"


class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
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
