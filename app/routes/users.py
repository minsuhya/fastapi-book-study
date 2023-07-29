#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import APIRouter, HTTPException, status
from ..database.connection import Database

from ..models.users import User, UserSignIn

user_router = APIRouter(tags=["User"])
user_database = Database(User)


@user_router.post("/signup")
async def sign_new_user(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User already exists")
    await user_database.save(user)
    return {"message": "User created successfully"}


@user_router.post("/signin")
async def sign_in_user(user: UserSignIn) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    if user_exist.password != user.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Wrong password")
    return {"message": "User signed in"}
