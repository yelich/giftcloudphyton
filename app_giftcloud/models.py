from django.db import models
from rest_framework import serializers
from django.utils import timezone
# Create your models here.

class Gift(models.Model):
    PUBLIC = 'PB'
    PRIVATE = 'PI'
    STATUS_CHOICES = (
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    )
    # HIGH = 'HG'
    # LOW = 'LW'
    # PRIORITY_CHOICES = (
    #     (HIGH, 'High'),
    #     (LOW, 'Low'),
    # )
    FACEBOOK = 'FB'
    TWITTER = 'TW'
    EMAIL = 'EM'
    SHARE_CHOICES = (
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
        (EMAIL, 'Email'),  
    )
    id = models.AutoField(primary_key=True)
    gift_name = models.CharField(max_length=50, default='')
    link_url = models.CharField(max_length=500, default='')
    store_name = models.CharField(max_length=50, default='')
    title = models.CharField(max_length=200, default='') 
    gift_details = models.TextField(null=True)
    quantity = models.CharField(max_length=50, default='')
    price = models.CharField(max_length=50, default='')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(
            blank=True, null=True)
    gift_choices = models.CharField(max_length=2,choices=STATUS_CHOICES, default=PUBLIC)
    share_choices = models.CharField(max_length=2,choices=SHARE_CHOICES, default=FACEBOOK)
    # priority_choices = models.CharField(max_length=2,choices=SHARE_CHOICES, default=LOW)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def created(self):
        self.created_date = timezone.now()
        self.save()    
    
    def __str__(self):
        return self.title

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ('id','gift_name','link_url','store_name','title','gift_details','quantity','price','created_date','published_date','gift_choices','share_choices')    

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    birthdate = models.DateField()
    password = models.CharField(max_length=8, default='')
    email = models.CharField(max_length=50, default='', unique=True)
    phone = models.CharField(max_length=13, default='')
    zip_code = models.CharField(max_length=9, default='')
    gifts = models.ManyToManyField(Gift)
    
class ProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = ('id','first_name','last_name','birthdate','password','email','phone','zip_code')

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)

class NotificationSerializer(serializers.ModelSerializer):
        class Meta:
            model = Notification
            fields = ('id','title')
    
class Event(models.Model):
    headline = models.CharField(max_length=100)
    event_date = models.DateTimeField(
                blank=True, null=True)
    notifications = models.ManyToManyField(Notification)
    gitfs = models.ManyToManyField(Gift)

class EventSerializer(serializers.ModelSerializer):
        class Meta:
            model = Event
            fields = ('id','headline')

class Social(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=256, default='')
    published_date = models.DateTimeField(
                blank=True, null=True)
                 
class SocialSerializer(serializers.ModelSerializer):
        class Meta:
            model = Social
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