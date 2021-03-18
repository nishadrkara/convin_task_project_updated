from __future__ import  absolute_import,unicode_literals
from celery import shared_task
import time
from task.models import TaskTracker
from django.conf import settings
import os
import datetime

file_ = open(os.path.join(settings.BASE_DIR,'email_send_status.log'),'a')

@shared_task
def send_email_daily():
    # email we can store separate table based on requirement
    task_trackers = TaskTracker.objects.filter(is_promoted=False, update_type='PER DAY')
    for task in task_trackers:
        log = f"Time: {datetime.datetime.now()} | Email Send Successfully task_type {task.task.task_type} | updated type PER DAY | Task Description {task.task.task_desc}\n"
        file_.write(log)
        # Email Send Logic Start 
        
        # Email Send Logic End

        task.is_promoted = True
        task.save()

    file_.close()


@shared_task
def send_email_monthly():
    # email we can store separate table based on requirement
    task_trackers = TaskTracker.objects.filter(is_promoted=False, update_type='MONTHLY')
    for task in task_trackers:
        log = f"Time: {datetime.datetime.now()} | Email Send Successfully task_type {task.task.task_type} | updated type MONTHLY | Task Description {task.task.task_desc}"
        
        # Email login

        # email Logic
        file_.write(log)
        task.is_promoted = True
        task.save()
    
    file_.close()



@shared_task
def send_email_weekely():
    # email we can store separate table based on requirement
    task_trackers = TaskTracker.objects.filter(is_promoted=False, update_type='WEEKLY')
    for task in task_trackers:
        log =  f"Time: {datetime.datetime.now()} | Email Send Successfully task_type {task.task.task_type} | updated type MONTHLY | Task Description {task.task.task_desc}"
        file_.write(log)
        # email logic start

        # email logic end

        task.is_promoted = True
        task.save()
    file_.close()







