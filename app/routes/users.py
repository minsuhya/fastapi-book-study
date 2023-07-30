#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm  # 인증정보(사용자명과 패스워드)를 추출하기 위해 로그인 라우트에 주입
from ..auth.jwt_handler import create_access_token

from ..auth.hash_password import HashPassword
from ..database.connection import Database
from ..models.users import User, TokenResponse

user_router = APIRouter(tags=["User"])
user_database = Database(User)
hash_password = HashPassword()


@user_router.post("/signup")
async def sign_new_user(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User already exists")
    user.password = hash_password.create_hash(user.password)
    await user_database.save(user)
    return {"message": "User created successfully"}


@user_router.post("/signin", response_model=TokenResponse)
async def sign_in_user(user: OAuth2PasswordRequestForm = Depends()) -> dict:
    """sign_in_user.

    :param user:
    :type user: OAuth2PasswordRequestForm
        OAuth2PasswordRequestForm 클래스를 sign_in_user() 라우트 함수에 주입하여
        해당함수가 OAuth2 사양을 준수하도록 한다.
    :rtype: dict
    """
    print("user:", user)
    user_exist = await User.find_one(User.email == user.username)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    if hash_password.verify_hash(user.password, user_exist.password):
        access_token = create_access_token(user_exist.email)
        return {"access_token": access_token, "token_type": "bearer"}

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Wrong password")


# 의존 라이브러리 추가
#  async def get_user(token: str):
#  user = decode_token(token)
#  return user
#
#
#  @user_router.get("/user/me")
#  async def get_user_me(user: User = Depends(get_user)):
#  """get_user_me.
#  Depends 클래스는 의존성을 주입하는 클래스입니다.
#  Depands 클래스는 라우트가 실행될 때 인수로 받은 함수를 실행하고,
#  그 함수의 반환값을 라우트의 인수로 전달합니다.
#
#  :param user:
#  :type user: User
#  """
#  return user
