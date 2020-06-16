from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import studentSerializer
from .models import student


# Create your views here.

class studentInfo(APIView):
    def get(self, request):
        students = student.objects.all()
        serializer = studentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class Info(APIView):
    def get_object(self, id):
        try:
            return student.objects.get(id=id)
        except student.DoesNotExist:
            return None

    def get(self, request, id):
        students = self.get_object(id)
        if students is None:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = studentSerializer(students)
        return Response(serializer.data)

    def put(self, request, id):
        students = self.get_object(id=id)
        serializer = studentSerializer(students, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        students = self.get_object(id)
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#
# @api_view(['GET', "POST"])
# def studentInfo(request):
#     if request.method == "GET":
#         students = student.objects.all()
#         serializer = studentSerializer(students, many=True)
#         return Response(serializer.data)
#
#     elif request.method == "POST":
#         serializer = studentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#

# @api_view(["GET", "PUT", "DELETE"])
# def Info(request, pk):
#     try:
#         students = student.objects.get(pk=pk)
#         print(students)
#     except student.DoesNotExist:
#         return Response(status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = studentSerializer(students)
#         return Response(serializer.data)
#
#     elif request.method == "PUT":
#         print(request.data)
#         serializer = studentSerializer(students, data=request.data)
#         print(serializer)
#
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
#             return Response(serializer.data, status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "DELETE":
#         students.delete()
#         return Response(status.HTTP_404_NOT_FOUND)
