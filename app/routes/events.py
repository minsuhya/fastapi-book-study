#!/usr/bin/env python
# -*- coding: utf-8 -*-

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status
from ..database.connection import Database

from ..models.events import Event, EventUpdate
from typing import List

event_router = APIRouter(tags=["Event"])
event_database = Database(Event)


@event_router.get("/", response_model=List[Event])
async def get_events() -> List[Event]:
    events = await event_database.get_all()
    return events


@event_router.get("/{id}", response_model=Event)
async def get_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Event not found")
    return event


# create event
@event_router.post("/new")
async def create_event(body: Event) -> dict:
    await event_database.save(body)
    return {"message": "Event created successfully"}


# update event
@event_router.put("/{id}")
async def update_event(id: PydanticObjectId, body: EventUpdate) -> Event:
    event = await event_database.update(id, body)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Event not found")
    return event


# delete event router
@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId) -> dict:
    event = await event_database.delete(id)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Event not found")
    return {"message": "Event deleted successfully"}


# delete all events
@event_router.delete("/")
async def delete_all_events() -> dict:
    await event_database.delete_all()
    return {"message": "All events deleted"}
