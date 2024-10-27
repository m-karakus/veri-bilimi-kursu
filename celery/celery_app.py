from celery import Celery
import time

# Configure Celery to use RabbitMQ as the broker
app = Celery('celery_app', broker='pyamqp://guest@rabbitmq//', backend='rpc://')


@app.task
def add(x, y):
    time.sleep(5)  # Simulate a long-running task
    return x + y

