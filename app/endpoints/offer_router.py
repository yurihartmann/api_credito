import json

import requests
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.models.client import Client
from app.utils.exceptions import ClientDoNotExists
from app.utils.logger import logger
from app.utils.redis import Redis
from app.utils.settigns import Settings

offer_router = APIRouter()


@offer_router.get('/')
async def get_offers_for_client(cpf: str) -> JSONResponse:
    try:
        settings = Settings()
        if len(cpf) > 11:
            return JSONResponse(status_code=400, content={'message': 'cpf is too long'})

        client = await Client.filter(cpf=cpf)
        if not client:
            raise ClientDoNotExists

        offers = Redis().get_item('offers')

        if not offers:
            logger.info('Request in API for get data')
            response = requests.post(url=f'{settings.BASE_URL_DATA}/offers')
            Redis().set_item('offers', data=json.dumps(response.json()), minutes_to_expire=10)
            offers = response.json()
        else:
            logger.info('Using cache data')
            offers = json.loads(offers)

        return offers

    except ClientDoNotExists:
        return JSONResponse(status_code=400, content={'message': 'Client do not exists'})

    except Exception as err:
        logger.error(f'Error in get_offers_for_client - Error: {err}')
        return JSONResponse(status_code=400, content={'message': 'Error in get offers for client'})
