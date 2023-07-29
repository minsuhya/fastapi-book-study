#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import APIRouter, HTTPException, status

from ..models.users import User, UserSignIn

user_router = APIRouter(tags=["User"])
users = {}


@user_router.post("/signup")
async def sign_new_user(user: User):
    if user.email in users:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User already exists")
    users[user.email] = user
    return {"message": "User created"}


@user_router.post("/signin")
async def sign_in_user(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    if users[user.email].password != user.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Wrong password")
    #  return users[user.email]
    return {"message": "User signed in"}
