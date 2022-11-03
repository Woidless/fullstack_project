import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJNGO_SETTINGS_MODULE',
                    'health_project.settings')

app = Celery('health_project')
app.config_from_object(
    'django.conf:settings',
    namespace='CELERY'
)
app.autodiscover_tasks()


# celery spam task
app.conf.beat_schedule = {
    'send-spam-every-24-hours':
    {
        'task': 'health_project.tasks.send_spam_email',
        'schedule': crontab(day_of_week='sunday')
    }
}