from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from categorias.models import CategoriaModel
from categorias.schemas import CategoriaIn, CategoriaOut
from contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select 
from fastapi_pagination.limit_offset import LimitOffsetPage
from fastapi_pagination.ext.sqlalchemy import paginate as sqlalchemy_paginate

router = APIRouter()

@router.post(
    '/', 
    summary = 'Criar uma nova categoria',
    status_code = status.HTTP_201_CREATED,
    response_model = CategoriaOut    
)

async def post(
    db_session: DatabaseDependency, 
    categoria_in: CategoriaIn = Body(...)
) -> CategoriaOut:
    categoria_out = CategoriaOut(id=uuid4(), ** categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())

    db_session.add(categoria_model)
    await db_session.commit()

    return categoria_out

@router.get(
    '/', 
    summary = 'Consultar todas as categorias',
    status_code = status.HTTP_200_OK,
    response_model = LimitOffsetPage[CategoriaOut]    
)

async def query(db_session: DatabaseDependency) -> LimitOffsetPage[CategoriaOut]:
    categorias = select(CategoriaModel)

    return await sqlalchemy_paginate(db_session, categorias)


@router.get(
    '/{id}', 
    summary = 'Consultar uma categoria pelo id',
    status_code = status.HTTP_200_OK,
    response_model = CategoriaOut  
)

async def query(id: UUID4, db_session: DatabaseDependency) -> CategoriaOut:
    categoria: CategoriaOut = (
        await db_session.execute(select(CategoriaModel).filter_by(id=id))).scalars().first()

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Categoria não encontrada no id: {id}')
    
    return categoria