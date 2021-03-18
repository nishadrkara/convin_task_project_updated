import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'convin_task_project.settings')

app = Celery('convin_task_project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'weekly':'task.tasks.send_email',
#     'schedule': crontab(hour=7, minute=30, day_of_week=1),
#     'args':('nishadkrkara@gmail.com')
# }

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')