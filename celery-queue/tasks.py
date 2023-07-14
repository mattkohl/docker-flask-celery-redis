import os
import time
from celery import Celery


CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery(__name__, 
                broker=CELERY_BROKER_URL, 
                backend=CELERY_RESULT_BACKEND,
                broker_connection_retry=True,
                broker_connection_retry_on_startup=True,
                broker_connection_max_retries=10,
                )


@celery.task(name='tasks.add')
def add(x: int, y: int) -> int:
    time.sleep(5)
    return x + y
