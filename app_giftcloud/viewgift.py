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
        p = Gift(store_name=content['store_name'], 
                title=content['title'], 
                text=content['text'],
                price=content['price'],
                created_date=content['created_date'],
                published_date=content['published_date'], 
                gift_choices=content['gift_choices'],
                share_choices=content['share_choices'])
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
        c = json.loads(body_unicode)
        Gift.objects.filter(id=gift_id).update(store_name=c['store_name'], 
                                                    title=c['title'],
                                                    text=c['text'],
                                                    price=c['price'],
                                                    gift_choices=c['gift_choices'])
        return Response({ "msg": "Gift updated"}, status=200)
    #delete Gift
    def delete(self, request, gift_id):
        try:
            account = Gift.objects.get(id=gift_id).delete()
        except Gift.DoesNotExist:
            return Response({"msg":"Gift no faund"}, status=404)
        serializer = GiftSerializer(account, many=False)
        return Response(serializer.data)