#!/usr/bin/env python
# -*- coding: utf-8 -*-

from beanie import Document, Link
from typing import List, Optional
from pydantic import BaseModel, EmailStr
from .events import Event


class User(Document):
    """User."""

    email: EmailStr
    password: str
    events: Optional[List[Event]] = []

    class Config:
        """Config."""

        json_schema_extra = {
            "example": {
                "email": "monkey@gmail.com",
                "password": "123456",
                "events": []
            }
        }

    class Settings:
        """Settings."""

        name = "users"


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


# 토큰을 적용함으로서 응답모델로 사용하지 않는다.
class UserSignIn(BaseModel):
    """UserSignIn."""

    email: EmailStr
    password: str

    class Config:
        """Config."""

        json_schema_extra = {
            "example": {
                "email": "fastapi@gmail.com",
                "password": "123456",
                "events": []
            }
        }
