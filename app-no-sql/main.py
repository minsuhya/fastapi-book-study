#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI
from .routes.users import user_router
from .routes.events import event_router

import uvicorn

app = FastAPI()

# regist routes
app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(event_router, prefix="/event", tags=["Event"])

#  if __name__ == "__main__":
#  uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
