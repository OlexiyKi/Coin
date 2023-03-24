from celery import Celery
from celery.schedules import crontab
import model_db
import alch_engine
from sqlalchemy.orm import Session
import os

from rate_getting import get_data
from trandfounder import find_trand



rabbit_host = os.environ.get('RABBIT_HOST', 'localhost')

app = Celery('celery_working', broker= f'pyamqp://guest@{rabbit_host}//')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    '''периодическая таска, тут запуск воркеров по времени'''
    sender.add_periodic_task(60.0, get_data_tasks.s())
    # sender.add_periodic_task(
    #     crontab(minute=0, hour='*/1'),  #every hour
    #     get_data_tasks.s()
    # )

@app.task()
def get_data_tasks():
    '''тут воркері, которіе будут собирать инфо'''
    get_data()
    find_trand()

    return True