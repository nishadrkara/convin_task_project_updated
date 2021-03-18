from task.models import Task,TaskTracker,TaskTracker
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ['id','task_type','task_desc']
        model = Task
    

    def validate_task_type(self,task_type):
        
        if not(1<=task_type<=4):
            raise serializers.ValidationError("task_type between 1 and 4")
        return task_type 
    
    def update(self,instance,validated_data):
        instance.task_type = validated_data.get('task_type',instance.task_type)
        instance.task_desc = validated_data.get('task_desc',instance.task_desc)
        instance.save()
        return instance


class TaskTrackerSerializerDisplaySerializer(serializers.ModelSerializer):
    task = serializers.SerializerMethodField()
    
    def get_task(self,instance):
        task_name = TaskSerializer(instance.task,many=False)
        return task_name.data

    class Meta:
        model = TaskTracker
        fields = ['id','task','update_type','update_through']



class TaskTrackerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TaskTracker
        fields = ['id','task','update_type','update_through']
    
    def update(self,instance,validated_data):
        
        instance.task = validated_data.get('task',instance.task)
        instance.update_type = validated_data.get('update_type',instance.update_type)
        instance.update_through = validated_data.get('update_through',instance.update_through)
        
        instance.save()
        return instance
    