from fastapi import routing, FastAPI
from app.routes import upload

app = FastAPI()

@app.get('/')
def read_root():
    return {'message':'Welcome to Student Score Analyzer Dashboard'}

app.include_router(upload.upload_router)
