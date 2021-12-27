from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from user.models import User
from user.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.http import JsonResponse

@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
    try:
        print(request.data)
        loginuser = request.data
        dbUser = User.objects.get(user_email=loginuser['user_email'])
        print(dbUser)
        if loginuser['password'] == dbUser.password:
            userSerializer = UserSerializer(dbUser, many=False)
            token = Token.objects.create(user= userSerializer)
            print(' ############################# ')
            print(f' 출력된 토큰값: {token}')
            print(' ############################# ')
            return JsonResponse(data=userSerializer.data, safe=False)
    except:
        return JsonResponse({'login':'fail 해당 이메일이 없습니다'})

