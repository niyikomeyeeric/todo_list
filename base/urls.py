from django.urls import path
from .views import  TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleleView, CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update>/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete>/<int:pk>', DeleleView.as_view(), name='task-delete'),
]