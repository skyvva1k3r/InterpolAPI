from fastapi.responses import FileResponse
from fastapi import APIRouter, Depends
from services import get_data
from schemas import Search

router = APIRouter()

@router.get('/')
async def index():
    return FileResponse('interpol(AI gen.).html')

@router.get('/search')
async def search(params: Search = Depends()):
    return get_data(params)
