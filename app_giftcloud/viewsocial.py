from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Social, SocialSerializer

import json

class SocialView(APIView):
    def get(self, request):
        #get Social
        all_entries = Social.objects.all()
        #serializer Social
        serializer = SocialSerializer(all_entries, many=True)
        #include it on the response
        return Response(serializer.data)


class SingleSocialView(APIView):
    def get(self, request, social_id):
        try:
            socialmedia = Social.objects.get(id=social_id)
        except Social.DoesNotExist:
            return Response({"msg":"Error"}, status=404)
        serializer = EventSerializer(socialmedia, many=False)
        return Response(serializer.data)
    #edit Event
    def post(self, request, social_id):
        body_unicode = request.body.decode('utf-8')
        c = json.loads(body_unicode)
        Social.objects.filter(id=social_id).update(social_name=c['social_name'], 
                                                    url=c['event_date'])
        return Response({ "msg": "Social updated"}, status=200)
    #delete Event
    def delete(self, request, social_id):
        try:
            socialmedia = Social.objects.get(id=social_id).delete()
        except Social.DoesNotExist:
            return Response({"msg":"Social no faund"}, status=404)
        serializer = SocialSerializer(eve, many=False)
        return Response(serializer.data)