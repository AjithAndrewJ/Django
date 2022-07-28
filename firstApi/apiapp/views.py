from django.shortcuts import render
from django.http import HttpResponse 
from apiapp import models
import json
# pip install json

def readData(request):
    #Write the logic tp read the inmfo from Employes
    empData = models.Employe.objects.get(id=3)
    empDict = {
        'eno': empData.eno,
        'ename': empData.ename,
        'esal': empData.esal
    }
    print(empDict)
    # {'eno': 3, 'ename': 'John', 'esal': 45000}
    jsonData = json.dumps(empDict)
    print(jsonData)
    # <QuerySet [<Employe: Employe object (1)>, <Employe: Employe object (2)>, <Employe: Employe object (3)>]>
    return HttpResponse(jsonData)

{'eno': 3, 'ename': 'John', 'esal': 45000}
{"eno": 3, "ename": "John", "esal": 45000}


