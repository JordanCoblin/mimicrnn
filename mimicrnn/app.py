#!C:\Users\Jordan_2\Documents\Programming\Onomastic\Scripts\python

from flask import Flask, render_template
from celery import Celery
from mimicrnn.keras_rnn import run_rnn

app = Flask(__name__)

def make_celery(flask_app):
    celery = Celery(app.import_name, backend=flask_app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(flask_app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

# configure app to use celery
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)

@app.route("/")
def main():
	rnn_task = train_rnn.delay()
	print('created celery task')
	return render_template('index.html')

@celery.task()
def train_rnn():
    #print('woah its printing :O')
    run_rnn()


if __name__ == "__main__":
	app.run()