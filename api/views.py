from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpRequest, JsonResponse
from .models import student
from .serializers import studentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET', "POST"])
def studentInfo(request):
    if request.method == "GET":
        students = student.objects.all()
        serializer = studentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def Info(request, pk):
    try:
        students = student.objects.get(pk=pk)
        print(students)
    except student.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = studentSerializer(students)
        return Response(serializer.data)

    elif request.method == "PUT":
        print(request.data)
        serializer = studentSerializer(students, data=request.data)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        students.delete()
        return Response(status.HTTP_404_NOT_FOUND)
