from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpRequest, JsonResponse
from .models import student
from .serializers import studentSerializer


# Create your views here.

@csrf_exempt
def studentInfo(request):
    if request.method == "GET":
        serializer = studentSerializer(student.objects.all(), many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = studentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def studentDetals(request, pk):
    try:
        students = student.objects.get(pk=pk)
    except student.DoesNotExist:
        return HttpRequest(status=400)
    if request.method == "GET":
        serializer = studentSerializer(students)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = studentSerializer(students, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        students.delete()
        print('delete')
        return HttpRequest(status=204)
