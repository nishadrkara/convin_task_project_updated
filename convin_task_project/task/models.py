from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def validate_task_type(value):
    if not (1<=value<=4):
        raise ValidationError('Task type should between 1 and 4', params={'value':value})


class Task(models.Model):

    task_type = models.IntegerField(default=1,validators=[validate_task_type]) # 1,2,3,4
    task_desc = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task_type}"

class TaskTracker(models.Model):

    UPDATED_TYPES = [('PER DAY','PER DAY'),
                ('WEEKLY','WEEKLY'),
                ('MONTHLY','MONTHLY'),
                ]
    
    UPDATE_THROUGH = [
                    ('EMAIL','EMAIL'),
                     ('SMS','SMS')
                     ]

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    update_type = models.CharField(max_length=50, choices=UPDATED_TYPES)
    # Task Update thorugh MAIL SMS
    update_through = models.CharField(max_length=30, blank=True, null=True, choices=UPDATE_THROUGH, default='EMAIL') 
    # flag for identifying task promoted or not default not promoted
    is_promoted = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
