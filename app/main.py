import uvicorn
from fastapi import FastAPI

from config import settings
# from db.base import Base
# from db.session import engine
from apis.base import api_router


def include_router(app: FastAPI) -> None:
    app.include_router(api_router)


#
# def create_tables() -> None:
#     Base.metadata.create_all(bind=engine)


def start_application() -> FastAPI:
    _app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
    )

    include_router(_app)
    # create_tables()

    return _app


app = start_application()

if __name__ == '__main__':
    config = uvicorn.Config('main:app', port=8000, host='0.0.0.0', reload=True)
    server = uvicorn.Server(config)
    server.run()
