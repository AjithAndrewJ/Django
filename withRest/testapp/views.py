from django.shortcuts import render
from testapp import models
from testapp import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

# @--> decorators
# Create your views here.

@api_view(['GET'])
def readOneData(request, id):#id = 1
    movieInfo = models.Movie.objects.get(id=id)#Beast Movie
    ms = serializers.MovieSerializer(movieInfo)
    print(ms.data)
    # {'title': 'Beast', 'hero': 'Vijay', 'heroine': 'Pooja', 'releasedDate': '2022-06-08', 'genre': 'Action'}
    return Response(ms.data)
    # read/2 --> read


@api_view(['GET', 'POST'])
def readCompleteData(request):
    if request.method == "GET":
        movieData = models.Movie.objects.all()
        ms = serializers.MovieSerializer(movieData, many=True)
        print(ms.data)
        return Response(ms.data)

    elif request.method == "POST":
        #write the logic to add the movie info
        ms = serializers.MovieSerializer(data = request.data)
        if ms.is_valid():
            ms.save()
            return Response(ms.data)




