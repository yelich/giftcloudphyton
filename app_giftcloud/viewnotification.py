from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Notification, NotificationSerializer


import json
import datetime

class NotificationView(APIView):
    def get(self, request):
        #get Notification
        all_entries = Notification.objects.all()
        #serializer Notification
        serializer = NotificationSerializer(all_entries, many=True)
        #include it on the response
        return Response(serializer.data)

    def put(self, request):
        #create Notification
        body_unicode = request.body.decode('utf-8')
        content = json.loads(body_unicode)
        #content = body['content']
        p = Notification(title=content['title'], 
                from_contact=content['from_contact'], 
                to=content['to'])
         #save Notification
        p.save()
        #serializer Notification
        serializer = ContactSerializer(p, many=False)
        #include it on the response
        return Response(serializer.data)

class SingleNotificationView(APIView):
    def get(self, request, notification_id):
        try:
            notifications = Notification.objects.get(id=notification_id)
        except Notification.DoesNotExist:
            return Response({"msg":"Error"}, status=404)
        serializer = NotificationSerializer(notifications, many=False)
        return Response(serializer.data)
    #edit notification
    def post(self, request, notification_id):
        body_unicode = request.body.decode('utf-8')
        content = json.loads(body_unicode)
        Notification.objects.filter(id=notification_id).update(title=content['title'], 
                                                                from_contact=content['from_contact'], 
                                                                to=content['to'])
        return Response({ "msg": "Notification updated"}, status=200)
    #delete contact
    def delete(self, request, notification_id):
        try:
            notifications = Notification.objects.get(id=notification_id).delete()
        except Notification.DoesNotExist:
            return Response({"msg":"Notification no faund"}, status=404)
        serializer = NotificationSerializer(notifications, many=False)
        return Response(serializer.data)