#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from models.events import EventUpdate
"""
fixture는 재사용할 수 있는 테스트 자원을 정의하는 방법입니다.
pytest.fixture 데코레이터를 사용하여 정의합니다.
API 라우트 테스트 시 애플리케이션 인스턴스를 반환하는 경우에 사용
"""


# fixture 정의
@pytest.fixture
def event() -> EventUpdate:
    """event.

    :rtype: EventUpdate
        fixture decorator 인수: scope:
        session: 테스트 전체 세션 동안 해당 함수 유효
        module: 테스트 파일이 실행된 후 특정 함수에서만 유효
    """
    return EventUpdate(title="fixture Evento 1",
                       image="https://i.imgur.com/4NZ6uLY.jpg",
                       description="fixture Evento 1",
                       tags=["tag1", "tag2"],
                       location="fixture location1")


def test_event_name(event: EventUpdate) -> None:
    assert event.title == "fixture Evento 1"
