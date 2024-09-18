import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.config import settings
from src.database import DB_URL
from src.utils.routers import router_list

app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
    redoc_url=None,
    root_path="/api",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://172.23.96.1:3000",
        "http://127.0.0.1:3000",
        "http://10.14.113.135:3000",
        "http://0.0.0.0:3000",
        "http://localhost:3000",
        "http://localhost:8100",
        "*",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
)


for router in router_list:
    app.include_router(router)


@app.get("/get_status")
def test():
    print(DB_URL)
    return {"message": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
