# convin_task_project

Task Scheduler Project CONVIN.AI

API Documetation available in Swagger
click this URL:  http://localhost:8000/swagger/

Beautiful Documetation of this API http://localhost:8000/readoc/

Celery settings inside of the settings.py
---------------------------------------------------------------

Steps for running
1. install the requirments.txt file
2. python manage.py runserver
3.create Task,update task,create task tracker(http://localhost:8000/task-tracker/),update task tracker

4.Celery beat open Terminal:  celery -A convin_task_project beat -l info

5.run Celery worker celery -A convin_task_project worker -l info

all are available swagger doc

AuditLevel log generathed when run this api server

Thanks 

Muhammed Nishad K

Email : nishadkrkara@gmail.com

Contact: +91 9744986325, +91 7994146698





