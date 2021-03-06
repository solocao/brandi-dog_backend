import datetime
import logging

from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI

import uvicorn
import socketio

from app.api.socket import sio
from app.api import games, chats, users

origins = [
    "*",
]

app = FastAPI(
    # title=config.PROJECT_NAME,
    # description=config.PROJECT_NAME,
    # version=config.PROJECT_VERSION,
    debug=True
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(
    games.router,
    prefix='/v1'
)

app.include_router(
    chats.router,
    prefix='/v1'
)

app.include_router(
    users.router,
    prefix='/v1'
)

# create socket.io app
sio_app = socketio.ASGIApp(socketio_server=sio, other_asgi_app=app)

if __name__ == "__main__":
    uvicorn.run(sio_app, host="0.0.0.0", port=8000, debug=True)
