from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact, ContactSerializer


import json
import datetime

class ContactView(APIView):
    def get(self, request):
        #get Contact
        all_entries = Contact.objects.all()
        #serializer Contact
        serializer = ContactSerializer(all_entries, many=True)
        #include it on the response
        return Response(serializer.data)

class SingleContactView(APIView):
    def get(self, request, contact_id):
        try:
            contacts = Contact.objects.get(id=contact_id)
        except Contact.DoesNotExist:
            return Response({"msg":"Error"}, status=404)
        serializer = ContactSerializer(contacts, many=False)
        return Response(serializer.data)
    #delete contact
    def delete(self, request, contact_id):
        try:
            account = Contact.objects.get(id=contact_id).delete()
        except Contact.DoesNotExist:
            return Response({"msg":"Contact no faund"}, status=404)
        serializer = ContactSerializer(account, many=False)
        return Response(serializer.data)