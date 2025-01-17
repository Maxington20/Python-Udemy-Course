# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from .serializers import TaskSerializers, UserSerializer
from .models import Task
from django.shortcuts import render
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView


# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializers

    #filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('completed',)
    ordering = ('-date_created',)
    search_fields = ('task_desc','task_name',)

    
class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_class = (AllowAny,)
    serializer_class = UserSerializer

'''
class DueTaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all().order_by('-date_created').filter(completed=False)
    serializer_class = TaskSerializers

class CompletedTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=True)
    serializer_class = TaskSerializers
    '''
