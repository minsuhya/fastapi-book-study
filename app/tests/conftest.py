#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 의존 라이브러리 임포트

import asyncio  # 활성 루프 세션을 만들어서 테스트가 단일 스레드로 실행되도록 함
import httpx  # HTTP CRUD 처리를 위한 비동기 클라이언트
import pytest  # fixture 정의를 위한 라이브러리

from app.main import app
from app.database.connection import Settings
from app.models.events import Event
from app.models.users import User


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


async def init_db():
    """init_db.
        Settings 클래스에서 새로운 데이터베이스 인스턴스 생성
    """
    test_settings = Settings()
    test_settings.DATABASE_URL = "mongodb://toktok:toktok1234@localhost:27017/testdb"

    await test_settings.initialize_database()


@pytest.fixture(scope="session")
async def default_client():
    """default_client.
        기본 클라이언트를 반환하는 fixture
        httpx를 통해 비동기로 실행되는 애플리케이션 인스턴스를 반환
    :rtype: AsyncClient"""
    await init_db()
    async with httpx.AsyncClient(app=app, base_url="http://app") as client:
        yield client
        # 리소스 정리
        await Event.find_all().delete()
        await User.find_all().delete()
