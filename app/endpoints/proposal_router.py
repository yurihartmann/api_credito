from datetime import datetime

import requests
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.models.client import Client, ClientSchema
from app.models.client_proposal import ClientProposal
from app.utils.exceptions import ClientDoNotExists
from app.utils.logger import logger
from app.utils.settigns import Settings
from app.validators.new_proposal_schema import NewProposalSchema

proposal_router = APIRouter()


@proposal_router.post('/')
async def send_proposal(new_proposal: NewProposalSchema) -> JSONResponse:
    try:
        settings = Settings()
        client_obj = await Client.filter(cpf=new_proposal.cpf).first()
        if not client_obj:
            raise ClientDoNotExists

        client = await ClientSchema.from_tortoise_orm(client_obj)

        list_of_proposal = await ClientProposal.filter(client=client.id)

        if list_of_proposal:
            for proposal in list_of_proposal:
                days = (datetime.now() - proposal.datetime.replace(tzinfo=None)).days + 1
                if days <= 30:
                    return JSONResponse(status_code=400, content={'message': f'You already sended this proposal in last {days} days'})

        await ClientProposal.create(client=client_obj, partner_id=new_proposal.partner_id)
        response = requests.post(url=f'{settings.BASE_URL_DATA}/proposal')
        return response.json()

    except ClientDoNotExists:
        return JSONResponse(status_code=400, content={'message': 'Client do not exists'})

    except Exception as err:
        logger.error(f'Error in send_proposal - Error: {err}')
        return JSONResponse(status_code=400, content={'message': 'Error in send proposal'})
