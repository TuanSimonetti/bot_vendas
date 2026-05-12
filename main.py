from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.controller.controller_instagram.controller_instagram import controller_instagram_check
from src.controller.controller_tiktok.controller_tiktok import controller_tiktok_check

app = FastAPI()


@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")


@app.get("/health", status_code=200)
def health():
    return {"status": "ok"}


@app.get("/instagram_check", tags=["instagram"])
async def instagram_check():
    return controller_instagram_check()


@app.get("/tiktok_check", tags=["tiktok"])
async def tiktok_check():
    return controller_tiktok_check()