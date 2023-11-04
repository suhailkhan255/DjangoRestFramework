from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views import View
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

@csrf_exempt    
def studentSaveAndGetAll(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythonData)
        if serializer.is_valid():
            serializer.save()
            json_dat = JSONRenderer().render(serializer.data)
            return HttpResponse(json_dat, content_type = 'application/json')
        
        json_dat = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_dat, content_type = 'application/json')
    
    if request.method == 'GET':
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many= True)
        return JsonResponse(serializer.data, safe=False)

#for primary Key based operations
@csrf_exempt
def studentUpdateDelete(request, pk):
    if request.method == 'GET':
        stu = Student.objects.get(id = pk)
        serializer = StudentSerializer(stu)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        stu = Student.objects.get(id = pk)
        serializer = StudentSerializer(stu, data = pythonData, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)

        return JsonResponse(serializer.errors, safe=False)
    
    if request.method == 'DELETE':
        stu = Student.objects.get(id = pk)
        stu.delete()
        return JsonResponse({"message":"Deleted"}, safe=False)





#Crud Using class based views    
@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):
    def get(self, request, *args, **kwargs):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many= True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythonData)
        if serializer.is_valid():
            serializer.save()
            json_dat = JSONRenderer().render(serializer.data)
            return HttpResponse(json_dat, content_type = 'application/json')
        
        json_dat = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_dat, content_type = 'application/json')
    
#for primary key based operation 
#Crud Using class based views    
@method_decorator(csrf_exempt, name='dispatch')
class StudentApiPrime(View):
    def get(self, request, pk=None):
        stu = Student.objects.get(id = pk)
        serializer = StudentSerializer(stu)
        return JsonResponse(serializer.data, safe=False)
    
    def put(self, request, pk=None):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        stu = Student.objects.get(id = pk)
        serializer = StudentSerializer(stu, data = pythonData, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False)
    
    def delete(self, request, pk=None):
        stu = Student.objects.get(id = pk)
        stu.delete()
        return JsonResponse({"message":"Deleted"}, safe=False)










