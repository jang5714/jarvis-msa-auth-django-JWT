from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from user.model_data import DbUploader
from user.models import User
from user.serializers import UserSerializer



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@parser_classes([JSONParser])
def users(request):
    if request.method == 'GET':
        all_users = User.objects.all().values()
        serializer = UserSerializer(all_users, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    elif request.method == 'POST':
        print(request.data)
        new_user = request.data
        print(new_user)
        serializer = UserSerializer(data=new_user)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'join': 'SUCCESS'})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        modifyemail = request.data
        try:
            user = User.objects.get(id=modifyemail['id'])
            dbuser = User.objects.all().filter(id=modifyemail['id']).values()[0]
            for i in modifyemail:
                dbuser[i] = modifyemail[i]
            serializer = UserSerializer(data=dbuser)
            if serializer.is_valid():
                serializer.update(user, dbuser)
            return JsonResponse({'modify': 'SUCCESS'})
        except:
            return JsonResponse({'modify': '수정하고자 하는 user가 없습니다.'})
    elif request.method == 'DELETE':
        deluser = request.data
        try:
            dbuser = User.objects.get(user_email=deluser['email'])
            if deluser['user_email'] == dbuser.user_email:
                dbuser.delete()
                return JsonResponse({'remove': 'SUCCESS'})
        except:
            return JsonResponse({'remove': 'error 지우고자 하는 user가 없습니다.'})

'''
iss: 토큰 발급자 (issuer)
sub: 토큰 제목 (subject)
aud: 토큰 대상자 (audience)
exp: 토큰의 만료시간 (expiraton), 시간은 NumericDate 형식으로 되어있어야 하며 (예: 1480849147370) 언제나 현재 시간보다 이후로 설정되어있어야합니다.
nbf: Not Before 를 의미하며, 토큰의 활성 날짜와 비슷한 개념입니다. 여기에도 NumericDate 형식으로 날짜를 지정하며, 이 날짜가 지나기 전까지는 토큰이 처리되지 않습니다.
iat: 토큰이 발급된 시간 (issued at), 이 값을 사용하여 토큰의 age 가 얼마나 되었는지 판단 할 수 있습니다.
jti: JWT의 고유 식별자로서, 주로 중복적인 처리를 방지하기 위하여 사용됩니다. 일회용 토큰에 사용하면 유용합니다.
'''

'''
# Header ############################
{
    "alg": "HS256",
    "typ": "JWT"
}

# Payload ###########################
{
    "sub": "1234567890",
    "name": "John Doe",
    "iat": 1516239022
}

# Signature #########################
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)
'''


@api_view(['GET'])
def user(request):
    try:
        finduser = request.data
        dbUser = User.objects.all().filter(user_email=finduser['email']).values()[0]
        return JsonResponse(data=dbUser, safe=False)
    except:
        return JsonResponse({'find': 'fail'})


@api_view(['GET'])
def exist(request, email):
    print(f'존재여부를 체크하는 이메일 {email}')
    try:
        existck = User.objects.all().filter(user_email=email).values()[0]
        if email == existck['email']:
            return JsonResponse({'exist': '해당 이메일은 있습니다'})
    except:
        return JsonResponse({'exist':'사용 가능합니다.'})


# @api_view(['GET'])
# @parser_classes([JSONParser])
# def upload(request):
#     print('######## 1 ########')
#     DbUploader().insert_data()
#     return JsonResponse({'Product Upload': 'SUCCEESS'})
