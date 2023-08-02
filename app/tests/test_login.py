#!/usr/bin/env python
# -*- coding: utf-8 -*-

# REST API route test
import httpx
import pytest


@pytest.mark.asyncio  # 비동기 테스트를 위한 데코레이터
async def test_sign_new_user(default_client: httpx.AsyncClient) -> None:
    payload = {"email": "test@gmail.com", "password": "test1234"}

    # 요청 헤더와 응답 정의
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    test_response = {
        "message": "User created successfully",
    }

    # 요청
    response = await default_client.post("/user/signup",
                                         json=payload,
                                         headers=headers)

    assert response.status_code == 200
    assert response.json() == test_response


@pytest.mark.asyncio
async def test_sign_in_user(default_client: httpx.AsyncClient) -> None:
    payload = {"username": "test@gmail.com", "password": "test1234"}
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = await default_client.post("/user/signin",
                                         data=payload,
                                         headers=headers)

    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"
