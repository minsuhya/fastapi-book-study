#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import APIRouter, Depends, HTTPException, Request, status
from ..db.connection import get_session
from ..models.events import Event, EventUpdate
from typing import List
from sqlmodel import select, delete

event_router = APIRouter(tags=["Event"])


@event_router.get("/", response_model=List[Event])
async def get_events(session=Depends(get_session)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events


@event_router.get("/{id}", response_model=Event)
async def get_event(id: int, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        return event

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Event not found")


# create event
@event_router.post("/new")
async def create_event(new_event: Event, session=Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    #  return event
    return {"message": "Event created successfully"}


# update event
@event_router.put("/edit/{id}", response_model=Event)
async def update_event(
    id: int, new_data: EventUpdate, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)

    if event:
        event_data = new_data.dict(exclude_unset=True)

        for key, value in event_data.items():
            setattr(event, key, value)

        session.add(event)
        session.commit()
        session.refresh(event)

        return event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Event not found")


# delete event router
@event_router.delete("/delete/{id}")
async def delete_event(id: int, session=Depends(get_session)) -> dict:
    event = session.get(Event, id)
    if event:
        session.delete(event)
        session.commit()
        return {"message": "Event deleted successfully"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Event not found")


# delete all events
@event_router.delete("/delete_all")
async def delete_all_events(session=Depends(get_session)) -> dict:
    statement = delete(Event)
    result = session.exec(statement)
    session.commit()
    return {"message": "All events deleted", "rowcount": result.rowcount}
