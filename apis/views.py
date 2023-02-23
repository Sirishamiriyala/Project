from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import subprocess
# import admin

# Create your views here.
@api_view(['GET'])
def getAPI(request):
    IPAddress=request.GET.get('ip')
    
    return Response("IP Address: "+str(IPAddress))


