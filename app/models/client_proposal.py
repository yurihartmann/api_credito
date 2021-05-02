from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.fields import *
from tortoise.models import Model

from app.models.client import Client


class ClientProposal(Model):
    id = UUIDField(pk=True)
    partner_id = IntField()
    client: ForeignKeyRelation[Client] = ForeignKeyField(
        "models.Client", related_name="client_proposals", to_field="id"
    )
    datetime = DatetimeField(null=True, auto_now=True)


ClientProposalSchema = pydantic_model_creator(ClientProposal, name='ClientProposalSchema')
