from django.contrib import admin
from django.urls import path, include 
from . import views
urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
	path('task-list/', views.List, name="task-list"),
	path('task-detail/<str:pk>/', views.TodoDetail, name="task-detail"),
	path('task-create/', views.TodoCreate, name="task-create"),

	path('task-update/<str:pk>/', views.TodoUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.TodoDelete, name="task-delete"),
]
