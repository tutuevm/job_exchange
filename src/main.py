from fastapi import FastAPI
import uvicorn

from src.config import settings


app = FastAPI(
        title=settings.API_TITLE,
        description=settings.API_DESCRIPTION,
        version=settings.API_VERSION,
        redoc_url=None,
    )

@app.get('/hello')
def test():
    return {'message':'hello world!'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8010, reload=True)