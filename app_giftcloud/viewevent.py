from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event, EventSerializer


import json
import datetime

class EventView(APIView):
    def get(self, request):
        #get Event
        all_entries = Event.objects.all()
        #serializer Event
        serializer = EventSerializer(all_entries, many=True)
        #include it on the response
        return Response(serializer.data)

    def put(self, request):
        #create Event
        body_unicode = request.body.decode('utf-8')
        content = json.loads(body_unicode)
        #content = body['content']
        p = Event(headline=content['headline'], 
                event_date=content['event_date'])
        #save Event
        p.save()
        #serializer Event
        serializer = EventSerializer(p, many=False)
        #include it on the response
        return Response(serializer.data)

class SingleEventView(APIView):
    def get(self, request, event_id):
        try:
            eve = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({"msg":"Error"}, status=404)
        serializer = EventSerializer(eve, many=False)
        return Response(serializer.data)
    #edit Event
    def post(self, request, event_id):
        body_unicode = request.body.decode('utf-8')
        content = json.loads(body_unicode)
        Event.objects.filter(id=event_id).update(headline=c['headline'], 
                                                    event_date=c['event_date'])
       return Response({ "msg": "Event updated"}, status=200)
    #delete Event
    def delete(self, request, event_id):
        try:
            eve = Event.objects.get(id=event_id).delete()
        except Event.DoesNotExist:
            return Response({"msg":"Event no faund"}, status=404)
        serializer = EventSerializer(eve, many=False)
        return Response(serializer.data)