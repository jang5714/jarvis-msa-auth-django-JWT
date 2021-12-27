from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import datetime
# Create your views here.
@api_view(['GET'])
def auth_server_started(request):
    return Response(f"Auth Server Started At {datetime.datetime.now()}")

@api_view(['GET'])
def auth_server_test(request):
    return Response(f" Test Connection Successed ")

