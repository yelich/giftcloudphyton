from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile,ProfileSerializer



import json
import datetime

class ProfileView(APIView):
   
    
    def post(self, request):
                #create MyGift
        body_unicode = request.body.decode('utf-8')
        content = json.loads(body_unicode)
        
        email = content.get("email", None)
        password = content.get("password", None)
        
        if not email or not password:
            return Response("email and password needed", status=400)
            
        profiles = Profile.objects.filter(email=email)
        
        if len(profiles) == 0:
            return Response("No username with that email", status=400)
        
        user = profiles[0]
        
        if user.password != password:
            return Response("invalid password", status=400)
            
        #serializer contact
        serializer = ProfileSerializer(user, many=False)
        request.session["email"] = user.email
        #include it on the response
        return Response(serializer.data)


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        email =request.data["email"]
        password =request.data["password"]
        print(password)
        user = User.objects.filter(email=email).first()
        print(user)
        print(user.check_password(password))
        if user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            })
        return Response("invalid password", status=400)