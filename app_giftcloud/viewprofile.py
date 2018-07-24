from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile,ProfileSerializer
from django.contrib.auth.models import User



import json
import datetime

class ProfileView(APIView):
    #get profile
    def get(self, request):
        all_entries = Profile.objects.all()
        #serializer contact
        serializer = ProfileSerializer(all_entries, many=True)
        #include it on the response
        return Response(serializer.data)

    #create Profile
    def put(self, request):
        body_unicode = request.body.decode('utf-8')
        content = json.loads(body_unicode)
        
        first_name = content.get("first_name", "")
        
        if first_name == "":
            return Response("first_name needed and can't be blank", status=400)    
        
        user = User()
        user.email = content['email']
        user.password = content['password']
        user.username = content['email']
        user.set_password(content["password"])
        user.save()
        
        profile = Profile(first_name=content['first_name'], 
                    last_name=content['last_name'], 
                    birthdate=content['birthdate'], 
                    email=content['email'], 
                    password=content['password'], user_base = user)
        #save contacts
        profile.save()
        
        
        #serializer contact
       
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data)
    
class SingleProfileView(APIView):
    def get(self, request, profile_id):
        try:
            account = Profile.objects.get(id=profile_id)
        except Profile.DoesNotExist:
            return Response({"msg":"Account no faund"}, status=404)
        serializer = ProfileSerializer(account, many=False)
        return Response(serializer.data)
    #edit Profile
    def post(self, request, profile_id):
        body_unicode = request.body.decode('utf-8')
        c = json.loads(body_unicode)
        Profile.objects.filter(id=profile_id).update(first_name=c['first_name'], 
                                                    last_name=c['last_name'],
                                                    birthdate=c['birthdate'],
                                                    email=c['email'],
                                                    password=c['password'])
        return Response({ "msg": "Profile updated"}, status=200)
    #delete an Profile
    def delete(self, request, profile_id):
        try:
            account = Profile.objects.get(id=profile_id).delete()
        except Profile.DoesNotExist:
            return Response({"msg":"Account no faund"}, status=404)
        serializer = ProfileSerializer(account, many=False)
        return Response(serializer.data)  
    