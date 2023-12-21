#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import lru_cache
from dotenv import find_dotenv

from pydantic import BaseSettings


class Settings(BaseSettings):
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_ROOT_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str

    class Config:
        env_file = find_dotenv(".env")


#@lru_cache()
def get_settings():
    return Settings()
