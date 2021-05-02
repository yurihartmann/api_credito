from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.models.client import Client, ClientSchema
from app.utils.exceptions import ClientAlreadyExists
from app.utils.logger import logger
from app.validators.new_client_schema import NewClientSchema

client_router = APIRouter()


@client_router.post('/')
async def create_new_client(new_client: NewClientSchema):
    try:
        if Client.filter(cpf=new_client.cpf):
            raise ClientAlreadyExists

        new_client_obj = await Client.create(**new_client.dict(exclude_unset=True))

        return await ClientSchema.from_tortoise_orm(new_client_obj)

    except ClientAlreadyExists:
        return JSONResponse(status_code=400, content={'message': 'Client with this cpf already exists'})

    except Exception as err:
        logger.error(f'Error in create_new_client - Error: {err}')
        return JSONResponse(status_code=400, content={'message': 'Error in create client'})
