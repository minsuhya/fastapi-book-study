#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    """Item."""

    name: str
    description: str | None = None
    price: float
    is_orffer: Union[bool, None] = None
    tax: float | None = None


@app.get("/")
async def read_root() -> dict:
    """read_root."""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_items(item_id: int, q: str | None = None):
    """read_item.

    :param item_id:
    :type item_id: int
    :param q:
    :type q: str | None
    """
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """update_item.

    :param item_id:
    :type item_id: int
    :param item:
    :type item: Item
    """
    return {
        "item_name": item.name,
        "item_price": item.price,
        "item_id": item_id
    }
