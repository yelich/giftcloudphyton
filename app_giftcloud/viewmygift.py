from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Gift, GiftSerializer, Profile, ProfileSerializer, MyGift, MyGiftSerializer


import json
import datetime

class MyGiftView(APIView):
    def get(self, request):
        #get Gift
        all_entries = MyGiftView.objects.all()
        #serializer Gift
        serializer = MyGiftSerializer(all_entries, many=True)
        #include it on the response
        return Response(serializer.data)
    def put(self, request):
        #create MyGift
        body_unicode = request.body.decode('utf-8')
        content = json.loads(body_unicode)
        #content = body['content']
        account = Gift.objects,create(gift_name=content['gift_name'])
        mygift = MyGift(fieldgift=content['fieldgift'],
                link_url=content['link_url'], 
                price=content['price'],
                quantity=content['quantity'],
                gift_details=content['gift_details'],
                privacy=content['privacy'])
        #save gift
        # gift.profile_id = request.session["id_profile"] 
        gift.save()
        gift.Profile.add()
        #serializer gift
        
        serializer = GiftSerializer(gift, many=False)
        #include it on the response
        return Response(serializer.data)
    

