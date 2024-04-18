from django.shortcuts import render
from rest_framework import generics
from .models import *
from rest_framework.permissions import IsAuthenticated
from .serializer import *

class CustomUserCreateApi(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializerApi
    permission_classes = (IsAuthenticated,)



class CustomUserListApi(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializerApi
    permission_classes = (IsAuthenticated,)

class CustomUserUpdateApi(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializerApi
    permission_classes = (IsAuthenticated,)


class CustomUserDestroyApi(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializerApi
    permission_classes = (IsAuthenticated,)


class CustomRetrieveApi(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializerApi
    permission_classes = (IsAuthenticated,)




class TaskCreateApi(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerApi 
    permission_classes = (IsAuthenticated,)


class TaskListApi(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerApi 
    permission_classes = (IsAuthenticated,)


class TaskUpdateApi(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerApi 
    permission_classes = (IsAuthenticated,)



class TaskDestroyApi(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerApi 
    permission_classes = (IsAuthenticated,)


class TaskRevieveApi(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerApi 
    permission_classes = (IsAuthenticated,)
           
           
       
       


