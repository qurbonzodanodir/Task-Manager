from django.urls import path
from.views import *

urlpatterns = [
    path('create/user',CustomUserCreateApi.as_view()),
    path('create/task',TaskCreateApi.as_view()),
    path('list/user',CustomUserListApi.as_view()),
    path('list/task',TaskListApi.as_view()),
    path('update/user/<int:pk>',CustomUserUpdateApi.as_view()),
    path('update/task/<int:pk>',TaskUpdateApi.as_view()),
    path('delete/user/<int:pk>',CustomUserDestroyApi.as_view()),
    path('delete/task/<int:pk>',TaskDestroyApi.as_view()),
    path('retriever/user/<int:pk>',CustomRetrieveApi.as_view()),
    path('retriever/task/<int:pk>',TaskRevieveApi.as_view()),

]
