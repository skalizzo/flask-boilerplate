import os

from pydantic import BaseSettings


class Config(BaseSettings):
    env: str = 'development'
    debug: bool = True
    app_host: str = '0.0.0.0'
    app_port: int = 5000
    db_url: str = 'mysql+pymysql://flask:flask@localhost:3306/flask'
    jwt_secret_key: str = 'flask'
    jwt_algorithm: str = 'HS256'


class DevelopmentConfig(Config):
    env: str = 'development'
    debug: bool = True


class TestingConfig(Config):
    env: str = 'testing'
    debug: bool = True


class ProductionConfig(Config):
    env: str = 'production'
    debug: bool = False


def get_config():
    env = os.getenv('env', 'development')
    config_type = {
        'development': DevelopmentConfig(),
        'testing': TestingConfig(),
        'production': ProductionConfig(),
    }
    return config_type[env]
