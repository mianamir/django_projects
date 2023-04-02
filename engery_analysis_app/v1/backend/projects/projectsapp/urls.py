from django.contrib import admin
from django.urls import path, include
from .views import (
    ProjectListAPI,
    ProjectCreateAPI,
    ProjectUpdateAPI,
    ProjectDeleteAPI
)

urlpatterns = [
    path('', ProjectListAPI.as_view(), name="project_list"),
    path('create/', ProjectCreateAPI.as_view(), name="project_create"),
    path('update/<int:project_id>/', ProjectUpdateAPI.as_view(), name="project_update"),
    path('delete/<int:project_id>', ProjectDeleteAPI.as_view(), name="project_delete"),

]
