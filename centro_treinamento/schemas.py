from pydantic import UUID4, Field
from typing import Annotated
from contrib.schemas import BaseSchema

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='DIO', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example='Rua A, Q01', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do centro de treinamento', example='Maria', max_length=30)]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='DIO', max_length=20)]

class CentroTreinamentoIn(CentroTreinamento):
    pass

class CentroTreinamentoOut(CentroTreinamento):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]
