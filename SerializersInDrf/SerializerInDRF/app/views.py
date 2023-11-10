from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt



#implementing Serialization
def student_detail(request,pk):
    stu = Student.objects.get(id = pk)
    print(type(stu)) #<class 'app.models.Student'>
    print(stu) #Student object (1)

    # converting query set in Native python data type
    serializer = StudentSerializer(stu)
    print(type(serializer)) #<class 'app.serializers.StudentSerializer'>
    print(serializer)
    '''
    StudentSerializer(<Student: Student object (1)>):
    name = CharField(max_length=20)
    roll = IntegerField()
    city = CharField(max_length=20)
    '''
    print(type(serializer.data)) #<class 'rest_framework.utils.serializer_helpers.ReturnDict'>
    print(serializer.data) #{'name': 'rahul', 'roll': 100, 'city': 'kanpur'}


    # converting python data type to Json
    json_dat = JSONRenderer().render(serializer.data)
    print(type(json_dat)) #<class 'bytes'>

    return HttpResponse(json_dat)


def getAllStudent(request):
    stu = Student.objects.all()

    # converting query set in Native python data type
    serializer = StudentSerializer(stu, many= True)
    print(type(serializer))# <class 'rest_framework.serializers.ListSerializer'>
    print(serializer.data)
    """[
    OrderedDict([('name', 'rahul'), ('roll', 100), ('city', 'kanpur')]), 
    OrderedDict([('name', 'shubham'), ('roll', 101), ('city', 'Allahabad')]),
    OrderedDict([('name', 'singh'), ('roll', 202), ('city', 'AMETHI')]) 
    ]
    """  
    # converting python data type to Json
    # json_dat = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_dat, content_type = 'application/json')
    # we can use directly JsonResponse insted wrinting above two lines we can
    return JsonResponse(serializer.data, safe=False) #if data is non dictionary then use safe=False in JsonResponse

#implementing De-Serialization
#to ignore the csrf error we use this notation
@csrf_exempt    
def saveEmployee(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data = pythonData)
        if serializer.is_valid():
            serializer.save()
            res = {"message":"data saved"}
            json_dat = JSONRenderer().render(serializer.data)
            return HttpResponse(json_dat, content_type = 'application/json')
        
        json_dat = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_dat, content_type = 'application/json')



        