import uvicorn

from turbocrawler_control.fastapi_app import get_fastapi_app
from turbocrawler_control.settings import FastAPIEnv


def create_db():
    ...
    # init_database()
    # populate_db()


create_db()
app = get_fastapi_app()
if __name__ == '__main__':
    uvicorn.run(
        app=app,
        host=FastAPIEnv.APP_HOST,
        port=FastAPIEnv.APP_PORT,
        log_level='info',
        access_log=True,
        workers=FastAPIEnv.APP_WORKERS,
        timeout_keep_alive=100
    )
