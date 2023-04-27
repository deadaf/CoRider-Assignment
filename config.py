from decouple import config


class Config:
    MONGO_URI = config("MONGO_URI")


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
