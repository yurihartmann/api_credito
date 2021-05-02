from pydantic import BaseModel, validator


class NewProposalSchema(BaseModel):
    partner_id: int
    cpf: str

    @validator('cpf')
    def validate_cpf(cls, cpf):
        if len(cpf) != 11:
            raise ValueError('cpf is invalid')
        return cpf
