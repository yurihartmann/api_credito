from tortoise import Tortoise
from fastapi import FastAPI

from app.endpoints.client_router import client_router
from app.endpoints.offer_router import offer_router
from app.endpoints.proposal_router import proposal_router
from app.utils.config_connection_tortoise import config_connection_tortoise

app = FastAPI(title="Credit API", version="0.1.0")


@app.on_event('startup')
async def on_startup_fast_api():
    await Tortoise.init(
        config=config_connection_tortoise()
    )
    await Tortoise.generate_schemas()


@app.on_event("shutdown")
async def on_shutdown():
    await Tortoise.close_connections()


app.include_router(router=proposal_router, prefix='/proposal')
app.include_router(router=client_router, prefix='/client')
app.include_router(router=offer_router, prefix='/offers')
