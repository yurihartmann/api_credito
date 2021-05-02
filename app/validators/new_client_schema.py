from datetime import datetime

from pydantic import BaseModel, validator


class NewClientSchema(BaseModel):
    cpf: str
    full_name: str
    birthDate: datetime
    email: str
    phone_number: str
    salary: int

    @validator('cpf')
    def validate_cpf(cls, cpf):
        if len(cpf) != 11:
            raise ValueError('cpf is invalid')
        return cpf

    @validator('salary')
    def validate_salary(cls, salary):
        if salary < 0:
            raise ValueError('salary do not accept negative value')
        return salary
