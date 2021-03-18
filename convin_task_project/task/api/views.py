from rest_framework.generics import GenericAPIView
from . serializers import TaskSerializer,TaskTrackerSerializer,TaskTrackerSerializerDisplaySerializer
from django.http import JsonResponse 
from task.models import Task,TaskTracker
from django.db.models import Q
from django.shortcuts import get_object_or_404


# This API Handling Task Creation, and Task Listing
class TaskListCreateAPI(GenericAPIView):

    serializer_class = TaskSerializer

    
    def get(self,request):
        # Search by Using Task q(url query parameter)
        
        query = request.query_params.get('q')

        qs = Task.objects.all()

        if query:
            qs = qs.filter(Q(task_type__icontains=query)|
                    Q(task_desc__icontains=query)
                )

        serializer = self.get_serializer(qs, many=True)
        return JsonResponse({'code':200,'response':serializer.data})

    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'code':201, 'message':'Task Successfully Stored'})
        return JsonResponse({'code':404, 'message':serializer.errors})


# This API View Handling Task Updation, and Single task List

class TaskUpdateDeleteAPI(GenericAPIView):

    serializer_class = TaskSerializer

    def get_object(self):
        task_id = self.kwargs['task_id']
        return get_object_or_404(Task,id=task_id)


    def get(self,request,task_id):

        instance = self.get_object()
        serializer = self.get_serializer(instance,many=False)
        return JsonResponse({'code':200,'response':serializer.data})


    def put(self,request,task_id):
        instance = self.get_object()
        serializer = self.get_serializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'code':200,'message':'Task Successfully Updated'})
        return JsonResponse({'code':404,'message':serializer.errors})


# This API View Handling TaskTracker Creation and List

class TaskTrackerListCreateAPI(GenericAPIView):

    serializer_class = TaskTrackerSerializer

    
    def get(self,request):
        # Search by Using Task q(url query parameter)
        
        query = request.query_params.get('q')

        qs = TaskTracker.objects.all()

        if query:
            qs = qs.filter(Q(task__task_type__icontains=query)|
                    Q(update_type__icontains=query)
                )

        serializer = TaskTrackerSerializerDisplaySerializer(qs, many=True)
        return JsonResponse({'code':200,'response':serializer.data})

    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'code':201, 'message':'Task Successfully Stored'})
        return JsonResponse({'code':404, 'message':serializer.errors})
    

# This API View Handling TaskTracker Updation, and Single taskTracker List

class TaskTrackerUpdateDeleteAPI(GenericAPIView):

    serializer_class = TaskTrackerSerializer

    def get_object(self):
        task_id = self.kwargs['task_tracker_id']
        return get_object_or_404(TaskTracker,id=task_id)


    def get(self,request,task_tracker_id):

        instance = self.get_object()
        serializer = TaskTrackerSerializerDisplaySerializer(instance,many=False)
        return JsonResponse({'code':200,'response':serializer.data})


    def put(self,request,task_tracker_id):

        instance = self.get_object()
        serializer = self.get_serializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse({'code':200,'message':'Task Tracker Successfully Updated'})

        return JsonResponse({'code':404,'message':serializer.errors})

