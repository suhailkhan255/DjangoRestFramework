from django.shortcuts import render
from app.models import Student
from app.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):

    def list(sefl, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
        
    
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
    
    def retrieve(self,request, pk = None):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
       

    def update(self, request, pk):
        student=Student.objects.get(pk=pk)
        serializer=StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       

    def destroy(self,request,pk):
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
       
    