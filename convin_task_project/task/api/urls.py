from . import views
from django.urls import path
urlpatterns = [path("tasks/",views.TaskListCreateAPI.as_view()),
              path('tasks/<int:task_id>',views.TaskUpdateDeleteAPI.as_view()),
             path('task-tracker/',views.TaskTrackerListCreateAPI.as_view()),
             path('task-tracker/<int:task_tracker_id>/',views.TaskTrackerUpdateDeleteAPI.as_view()),
             ]