import os

class Config:

    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://antavio:pass123@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config:The parent configuration class with General configuration settings
    '''
    pass
class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
# class TestConfig(Config):
#     '''
#     Test configuration child class
    
#     Args:
#         Config: The parent configuration class with general configuration settings
#     '''


config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    # 'test':TestConfig
}