#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httpx
import pytest
from auth.jwt_handler import create_access_token
from app.models.events import Event
from typing import AsyncGenerator


@pytest.fixture(scope="module")  # 모듈 수준의 픽스처, 접속 토큰 반환
async def access_token() -> str:
    return create_access_token("test@gmail.com")


@pytest.fixture(scope="module")
async def mock_event() -> AsyncGenerator[Event, None]:
    new_event = Event(creator="test@gmail.com",
                      title="test event",
                      image="test image",
                      description="test description",
                      tags=["test"],
                      location="test location")

    await Event.insert_one(new_event)

    yield new_event


@pytest.mark.asyncio
async def test_get_event(default_client: httpx.AsyncClient,
                         mock_event: Event) -> None:
    """test_get_event.
        이벤트 조회

    :param default_client:
    :type default_client: httpx.AsyncClient
    :param mock_event:
    :type mock_event: Event
    :rtype: None
    """
    url = f"/event/{str(mock_event.id)}"
    response = await default_client.get(url)

    assert response.status_code == 200
    assert response.json()["title"] == mock_event.title
    assert response.json()["_id"] == str(mock_event.id)


# post event test
@pytest.mark.asyncio
async def test_post_event(default_client: httpx.AsyncClient,
                          access_token: str) -> None:
    payload = {
        "title": "post test event",
        "image": "post test image",
        "description": "post test description",
        "tags": ["test", "post"],
        "location": "post test location",
    }

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    test_response = {
        "message": "Event created successfully",
    }

    response = await default_client.post("/event/new",
                                         json=payload,
                                         headers=headers)

    assert response.status_code == 200
    assert response.json() == test_response


# get event count test
@pytest.mark.asyncio
async def test_get_event_count(default_client: httpx.AsyncClient) -> None:
    response = await default_client.get("/event/")

    events = response.json()

    assert response.status_code == 200
    assert len(events) == 2


# update event test
@pytest.mark.asyncio
async def test_update_event(default_client: httpx.AsyncClient,
                            mock_event: Event, access_token: str) -> None:
    test_payload = {
        "title": "update test event",
    }
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {access_token}",
    }

    url = f"/event/{str(mock_event.id)}"
    response = await default_client.put(url,
                                        json=test_payload,
                                        headers=headers)

    assert response.status_code == 200
    assert response.json()["title"] == test_payload["title"]


# delete event test
@pytest.mark.asyncio
async def test_delete_event(default_client: httpx.AsyncClient,
                            mock_event: Event, access_token: str) -> None:
    test_response = {
        "message": "Event deleted successfully",
    }

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {access_token}",
    }

    url = f"/event/{str(mock_event.id)}"

    response = await default_client.delete(url, headers=headers)

    assert response.status_code == 200
    assert response.json() == test_response


# get event again test
@pytest.mark.asyncio
async def test_get_event_again(default_client: httpx.AsyncClient,
                               mock_event: Event) -> None:
    url = f"/event/{str(mock_event.id)}"
    response = await default_client.get(url)

    assert response.status_code == 404
    #  assert response.status_code == 200
    #  assert response.json()["creator"] == mock_event.creator
    #  assert response.json()["_id"] == str(mock_event.id)
