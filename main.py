from fastapi import FastAPI
from routes import xmind_sync_github

app = FastAPI()

app.include_router(xmind_sync_github.router)