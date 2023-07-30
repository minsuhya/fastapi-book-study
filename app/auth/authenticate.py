#!/usr/bin/env python
# -*- coding: utf-8 -*-

# authenticate 의존 라이브러리가 포함되며 인증 및 권한을 위해 라이트에 주입된다.
# 활성 세션에 존재하는 사용자 정보를 추출하는 단일 창구 역할을 한다.

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .jwt_handler import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/signin")


async def authenticate(token: str = Depends(oauth2_scheme)) -> str:
    if not token:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Sign in for access")

    decoded_token = verify_access_token(token)
    return decoded_token["user"]


# Depends              : oauth2_scheme을 의존 라이브러리 함수에 주입
# OAuth2PasswordBearer : 보안 로직이 존재한다는 것을 애플리케이션에 알려준다.
# verify_access_token  : 앞서 정의한 토큰 생성 및 검증 함수로, 토큰의 유효성을 검증
