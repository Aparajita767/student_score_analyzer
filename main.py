from fastapi import routing, FastAPI
from app.routes import upload
import logging

logging.basicConfig(
    level=logging.INFO,
    format= '%(asctime)%s [%(levelname)%s] %(name)%s : %(message)s'
)

app = FastAPI()

@app.get('/')
def read_root():
    logging.info('Root endpoint hit')
    return {'message':'Welcome to Student Score Analyzer Dashboard'}

app.include_router(upload.upload_router)
