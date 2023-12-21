#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.parse import quote_plus
from sqlmodel import SQLModel, Session, create_engine
from ..models.events import Event
from ..core.config import get_settings

settings = get_settings()

database_connection_string = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    settings.MYSQL_USER,
    quote_plus(settings.MYSQL_PASSWORD),
    settings.MYSQL_HOST,
    settings.MYSQL_PORT,
    settings.MYSQL_DATABASE,
)
connect_args = {}
engine_url = create_engine(database_connection_string,
                           echo=True,
                           connect_args=connect_args)


def conn():
    SQLModel.metadata.create_all(engine_url)


def get_session():
    with Session(engine_url) as session:
        yield session
