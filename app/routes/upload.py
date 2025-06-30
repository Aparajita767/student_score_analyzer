from fastapi import APIRouter,File, UploadFile , HTTPException
import os
import shutil
from pathlib import Path
import logging

upload_router = APIRouter()
logger = logging.getLogger(__name__)

ALLOWED_EXTENSIONS = ['.csv']

def is_allowed_file(filename):
    '''
    Check if filename has valid extension
    '''
    filename = filename.strip() #strip before splitext as whitespace after . is  not stripped afterwards
    ext = os.path.splitext(filename)[1].lower() #splitext returns (root, ext) choose only ext
    return ext in ALLOWED_EXTENSIONS

@upload_router.post('/upload')
async def file_upload(file : UploadFile = File(...)):

    filename = Path(file.filename).name

    if not is_allowed_file(file.filename):
        logger.warning(f'Rejected upload  {file.filename}')
        raise HTTPException(status_code=400, detail= 'Only CSV files are allowed')
    
    file_location = os.path.join('data',filename)

    with open(file_location, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    logger.info(f'Uploaded file saved : {file_location}')
    return {'message' : 'File has been successfully uploaded', 'filename' : file.filename}
