#!/usr/bin/env python
# -*- coding: utf-8 -*-

from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Any, List, Optional
from pydantic import BaseSettings, BaseModel
from dotenv import find_dotenv
import os


class Database:

    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        await document.create()
        return

    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def get_all(self) -> List[Any]:
        return await self.model.find_all().to_list()

    # update document
    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        des_body = body.dict()
        des_body = {k: v for k, v in des_body.items() if v is not None}
        update_query = {"$set": des_body}

        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc

    # delete document
    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True

    # delete all documents
    async def delete_all(self) -> None:
        await self.model.delete_all()
        return


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    SECRET_KEY: str = "secret_key"  # jwt 비밀키
    ACCESS_TOKEN_EXPIRES: int = 3600  # jwt 만료시간
    ACCESS_TOKEN_ALGORITHM: str = "HS256"  # jwt 알고리즘

    async def initialize_database(self):
        print("database_url:", self.DATABASE_URL)
        client = AsyncIOMotorClient(self.DATABASE_URL)
        #  await init_beanie(database=client.get_default_database(),
        await init_beanie(database=client['itoktok'],
                          document_models=[
                              "app.models.events.Event",
                              "app.models.users.User"
                          ])

    class Config:
        env_file = find_dotenv(".env")
        env_file_encoding = "utf-8"
