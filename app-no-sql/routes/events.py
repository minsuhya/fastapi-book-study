#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import APIRouter, Body, HTTPException, status
from ..models.events import Event
from typing import List

event_router = APIRouter(tags=["Event"])

events = []


@event_router.get("/", response_model=List[Event])
async def get_events() -> List[Event]:
    return events


@event_router.get("/{event_id}", response_model=Event)
async def get_event(event_id: int) -> Event:
    for event in events:
        if event.id == event_id:
            return event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Event not found")


# create event
@event_router.post("/new")
async def create_event(event: Event = Body(...)) -> dict:
    events.append(event)
    #  return event
    return {"message": "Event created"}


# delete event router
@event_router.delete("/{event_id}")
async def delete_event(event_id: int) -> dict:
    for event in events:
        if event.id == event_id:
            events.remove(event)
            return {"message": "Event deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Event not found")


# delete all events
@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {"message": "All events deleted"}
