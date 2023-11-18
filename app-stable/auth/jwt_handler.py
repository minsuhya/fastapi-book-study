#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Path: jwt_handler.py
# JWT String Encode, Decode

import time
from datetime import datetime

from fastapi import HTTPException, status
from jose import JWTError, jwt

from app.database.connection import Settings

settings = Settings()


# create jwt token
def create_access_token(user: str):
    """
    JWT 토큰 생성
    :param user: 사용자
    :return: JWT 토큰
    """
    secret_key = settings.SECRET_KEY
    access_token_expires = settings.ACCESS_TOKEN_EXPIRES
    access_token_algorithm = settings.ACCESS_TOKEN_ALGORITHM

    payload = {"user": user, "expires": time.time() + access_token_expires}
    token = jwt.encode(payload, secret_key, algorithm=access_token_algorithm)
    return token


# verify jwt token
def verify_access_token(token: str):
    """
    JWT 토큰 검증
    :param token: JWT 토큰
    :return: JWT 토큰 검증 결과
    """
    secret_key = settings.SECRET_KEY
    access_token_algorithm = settings.ACCESS_TOKEN_ALGORITHM

    try:
        payload = jwt.decode(token,
                             secret_key,
                             algorithms=[access_token_algorithm])
        expire = payload.get("expires")

        if expire is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="No access token provided")
        if datetime.fromtimestamp(expire) < datetime.now():
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Expired access token")
        return payload
    except JWTError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Invalid access token")
