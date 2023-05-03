from django.shortcuts import render
from dean.serializers import StudentDetailSerializer
from rest_framework import generics
from dean.models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.


class StudentCreate(generics.CreateAPIView):
    serializer_class = StudentDetailSerializer


class StudentGetAll(generics.ListAPIView):
    serializer_class = StudentDetailSerializer
    queryset = Student.objects.all()


class StudentUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentDetailSerializer
    queryset = Student.objects.all()

# @api_view(['GET'])
# def students(request):
#     data = Student.objects.all()
#
#     serializer = StudentDetailSerializer(data, context={'request': request}, many=True)
#
#     return Response(serializer.data)