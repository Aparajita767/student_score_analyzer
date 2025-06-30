from fastapi import APIRouter
from app.services.cleaning import clean_csv

clean_router = APIRouter()

@clean_router.get('/clean/{filename}')
async def clean_file(filename : str):
    '''
    API endpoint to clean previously uploaded csv file
    '''