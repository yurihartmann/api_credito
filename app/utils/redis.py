import redis as redis

from app.utils.logger import logger
from app.utils.settigns import Settings
from app.utils.singleton import SingletonMeta


class Redis(metaclass=SingletonMeta):
    def __init__(self):
        settings = Settings()
        self.redis = redis.Redis(host=settings.REDIS_HOSTNAME, password=settings.REDIS_PASSWORD)

    def get_item(self, key: str):
        try:
            return self.redis.get(key)
        except Exception as err:
            logger.error(f"Error on get the item on redis - {err}")
            return False

    def set_item(self, key, data: str, minutes_to_expire: int = 1):
        try:
            return self.redis.set(name=key, value=data, ex=minutes_to_expire * 60)
        except Exception as err:
            logger.error(f"Error on save the item on redis - {err} - Data {data} - Key {key}")
            return False
