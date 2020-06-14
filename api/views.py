from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpRequest,JsonResponse
from .models import student
from .serializers import studentSerializer
# Create your views here.

@csrf_exempt
def studentInfo(request):
    if request.method == 'GET':
        students = student.objects.all()
        serializer = studentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = studentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)