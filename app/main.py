#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.connection import Settings
from app.routes.events import event_router
from app.routes.users import user_router

app = FastAPI()
settings = Settings()

# CORS 설정, 출처 등록
"""
CORS(Cross-Origin Resource Sharing)는 등록되지 않은 사용자가 리소스를
사용하지 못하도록 제한하는 규칙. 특정 프론트엔드 애플리케이션이 우리가 만든
웹 API를 호출하면 브라우저가 호출의 출처를 확인해서 제한한다.
즉, API와 출처(도메인)가 동일한 경우 or API가 허가한 출처만 리소스에 접근 가능
"""
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # 헤더에 자격증명 허용
    allow_methods=["*"],
    allow_headers=["*"])

# regist routes
app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(event_router, prefix="/event", tags=["Event"])


@app.on_event("startup")
async def init_db():
    await settings.initialize_database()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
