from fastapi import FastAPI
import uvicorn

from src.config import settings
from src.utils.routers import router_list

app = FastAPI(title=settings.API_TITLE,
              description=settings.API_DESCRIPTION,
              version=settings.API_VERSION,
              redoc_url=None,
              )

for router in router_list:
    app.include_router(router)


@app.get('/get_status')
def test():
    return {'message': 'OK'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8010, reload=True)
