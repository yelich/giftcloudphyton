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

    def put(self, request):
        #create Contact
        body_unicode = request.body.decode('utf-8')
        content = json.loads(body_unicode)
        #content = body['content']
        p = Contact(full_name=content['full_name'], 
                social=content['social'], 
                birthdate=content['birthdate'],
                email=content['email'],
                phone=content['phone'])
         #save Contact
        p.save()
        #serializer Contact
        serializer = ContactSerializer(p, many=False)
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
    #edit contact
    def post(self, request, contact_id):
        body_unicode = request.body.decode('utf-8')
        content = json.loads(body_unicode)
        Contact.objects.filter(id=contact_id).update(full_name=content['full_name'], 
                                                        social=content['social'], 
                                                        birthdate=content['birthdate'],
                                                        email=content['email'],
                                                        phone=content['phone'])
        return Response({ "msg": "Contact updated"}, status=200)
    #delete contact
    def delete(self, request, contact_id):
        try:
            account = Contact.objects.get(id=contact_id).delete()
        except Contact.DoesNotExist:
            return Response({"msg":"Contact no faund"}, status=404)
        serializer = ContactSerializer(account, many=False)
        return Response(serializer.data)