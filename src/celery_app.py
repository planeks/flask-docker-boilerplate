from os import environ

from celery import Task, Celery


def init_celery(flask_app) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with flask_app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(
        __name__,
        task_cls=FlaskTask,
        broker_url=environ.get("REDIS_URL"),
        result_backend=environ.get("REDIS_URL"),
        task_ignore_result=True
    )
    celery_app.set_default()
    celery_app.conf.timezone = 'Europe/Kyiv'
    celery_app.autodiscover_tasks(packages=[])
    return celery_app
