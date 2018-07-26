from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact, ContactSerializer


import json
import datetime

class ContactView(APIView):
    def get(self, request):
        try:
            account = Contact.objects.filter(profile = request.user)
        except Profile.DoesNotExist:
            return Response({"msg":"Account no faund"}, status=404)
        serializer = ProfileSerializer(account, many=False)
        return Response(serializer.data)

class SingleContactView(APIView):
    #delete contact
    def delete(self, request, contact_id):
        try:
            account = Contact.objects.get(id=contact_id).delete()
        except Contact.DoesNotExist:
            return Response({"msg":"Contact no faund"}, status=404)
        serializer = ContactSerializer(account, many=False)
        return Response(serializer.data)