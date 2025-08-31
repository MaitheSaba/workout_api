from fastapi import APIRouter
from atleta.controller import router as atleta_router
from categorias.controller import router as categoria_router
from centro_treinamento.controller import router as centro_treinamento_router

api_router = APIRouter()

api_router.include_router(atleta_router, prefix='/atletas', tags=['atletas'])
api_router.include_router(categoria_router, prefix='/categorias', tags=['categorias'])
api_router.include_router(centro_treinamento_router, prefix='/centro_treinamento', tags=['centro_treinamento'])