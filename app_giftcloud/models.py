from django.db import models
from rest_framework import serializers
# Create your models here.
STATUS_CHOICES()

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50, default='')
    zip_code = models.CharField(max_length=9, default='')
    
class ProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = ('id','full_name', 'email','phone','zip_code')
            
class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)

class NotificationSerializer(serializers.ModelSerializer):
        class Meta:
            model = Notification
            fields = ('id','title')
    
class Event(models.Model):
    headline = models.CharField(max_length=100)
    notifications = models.ManyToManyField(Notification)

class EventSerializer(serializers.ModelSerializer):
        class Meta:
            model = Event
            fields = ('id','headline')

class Gift(models.Model):
    PUBLIC = 'PB'
    PRIVATE = 'PI'
    NOT_SPECIED = 'NS'
        STATUS_CHOICES = (
            (PUBLIC, 'Public')
            (PRIVATE, 'Private')
            (NOT_SPECIED, 'Not Specied')   
        )
        id = models.AutoField(primary_key=True)
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)
        gift_status_choices = models.CharField(max_length=2,choices=STATUS_CHOICES, default=NOT_SPECIED)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title
            
class GiftSerializer(serializers.ModelSerializer):
        class Meta:
            model = Gift
            fields = ('id','title','text','created_date','published_date','gift_status_choices')           

class Platform(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=NONCE_SERVER_URL_LENGTH)
    published_date = models.DateTimeField(
                blank=True, null=True)
    #Preguntar alejandro si             
class PlatformSerializer(serializers.ModelSerializer):
        class Meta:
            model = Platform
            fields = ('id','url','published_date') 
            
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50, default='')
    
    
class ContactSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = ('id','full_name', 'email','phone')