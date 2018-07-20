from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Gift, GiftSerializer


import json
import datetime

class GiftView(APIView):
    def get(self, request):
        #get Gift
        all_entries = Gift.objects.all()
        #serializer Gift
        serializer = GiftSerializer(all_entries, many=True)
        #include it on the response
        return Response(serializer.data)

    def put(self, request):
        #create Gift
        body_unicode = request.body.decode('utf-8')
        content = json.loads(body_unicode)
        #content = body['content']
        p = Gift(gift_name=content['gift_name'],
                link_url=content['link_url'], 
                price=content['price'],
                quantity=content['quantity'],
                gift_details=content['gift_details'])
        #save gift
        p.save()
        #serializer gift
        serializer = GiftSerializer(p, many=False)
        #include it on the response
        return Response(serializer.data)

class SingleGiftView(APIView):
    def get(self, request, gift_id):
        try:
            bag = Gift.objects.get(id=gift_id)
        except Gift.DoesNotExist:
            return Response({"msg":"Error"}, status=404)
        serializer = GiftSerializer(bag, many=False)
        return Response(serializer.data)
    #edit Gift
    def post(self, request, gift_id):
        body_unicode = request.body.decode('utf-8')
        content = json.loads(body_unicode)
        Gift.objects.filter(id=gift_id).update(gift_name=content['gift_name'],
                                                link_url=content['link_url'], 
                                                price=content['price'],
                                                quantity=content['quantity'],
                                                gift_details=content['gift_details'])
        return Response({ "msg": "Gift updated"}, status=200)
    #delete Gift
    def delete(self, request, gift_id):
     
        try:
            gift = Gift.objects.get(id=gift_id).delete()
        except Gift.DoesNotExist:
            return Response({"msg":"Gift no faund"}, status=404)
        serializer = GiftSerializer(gift, many=False)
        return Response(serializer.data)