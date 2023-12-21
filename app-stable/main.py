#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

from .db.connection import conn

from .routes.users import user_router
from .routes.events import event_router

#  import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# regist routes
app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(event_router, prefix="/event", tags=["Event"])


@app.on_event("startup")
def on_startup():
    conn()


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")


#  if __name__ == "__main__":
#  uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
