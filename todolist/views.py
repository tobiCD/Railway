# todo_app/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Todolist
from .serializers import TodoSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/todo-list/',
        'Detail View': '/todo-detail/<str:pk>/',
        'Create': '/todo-create/',
        'Update': '/todo-update/<str:pk>/',
        'Delete': '/todo-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def List(request):
    todo = Todolist.objects.all()
    
    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TodoDetail(request, pk):
    try:
        todo = Todolist.objects.get(id=pk)
    except Todolist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def TodoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def TodoUpdate(request, pk):
	task = Todolist.objects.get(id=pk)
	serializer = TodoSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def TodoDelete(request, pk):
    try:
        todo = Todolist.objects.get(id=pk)
    except Todolist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    todo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
