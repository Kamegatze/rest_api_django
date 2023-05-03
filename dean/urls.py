from django.contrib import admin
from django.urls import path, include
from dean.views import *
from dean import views

app_name = 'dean'
urlpatterns = [
    path('student/create', StudentCreate.as_view()),
    path(r'student/getAll', StudentGetAll.as_view()),
    path('student/delete_and_update/<int:pk>', StudentUpdateDelete.as_view()),
]