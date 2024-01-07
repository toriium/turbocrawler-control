import os


# class DatabaseEnv:
#     DB_HOST: str = os.getenv('DB_HOST')
#     DB_USER: str = os.getenv('DB_USER')
#     DB_PORT: str = os.getenv('DB_PORT')
#     DB_NAME: str = os.getenv('DB_NAME')
#     DB_PASSWORD: str = os.getenv('DB_PASSWORD')

# class FastAPIEnv:
#     APP_HOST: str = os.getenv('APP_HOST')
#     APP_PORT: int = int(os.getenv('APP_PORT'))
#     APP_WORKERS: int = int(os.getenv('APP_WORKERS'))


class FastAPIEnv:
    APP_HOST: str = "127.0.0.1"
    APP_PORT: int = 8080
    APP_WORKERS: int = 1


class DatabaseEnv:
    DB_HOST: str = "127.0.0.1"
    DB_USER: str = "root"
    DB_PORT: str = "3306"
    DB_NAME: str = "turbocrawler"
    DB_PASSWORD: str = "123"
