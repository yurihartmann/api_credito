from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.fields import *
from tortoise.models import Model

from app.models.timestamp_mixin import TimestampMixin


class Client(Model, TimestampMixin):
    id = UUIDField(pk=True)
    cpf = CharField(max_length=11, unique=True)
    full_name = TextField()
    birthDate = DateField()
    email = TextField()
    phone_number = TextField()
    salary = FloatField()


ClientSchema = pydantic_model_creator(Client, name='ClientSchema')
