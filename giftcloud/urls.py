"""giftcloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_giftcloud import viewprofile, viewgift, viewcontact, viewnotification, viewevent, viewsocial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', viewprofile.ProfileView.as_view(), name='profile'),
    path('editprofile/<int:profile_id>', viewprofile.SingleProfileView.as_view(), name='editprofile'),
    
    path('gift/', viewgift.GiftView.as_view(), name='gift'),
    path('editgift/<int:gift_id>', viewgift.SingleGiftView.as_view(), name='editgift'),
    path('account/', viewgift.GiftView.as_view(), name='getgift'),
    
    path('contact/', viewcontact.ContactView.as_view(), name='contact'),
    path('contact/<int:contact_id>', viewcontact.ContactView.as_view(), name='editcontact'),
    
    path('notification/', viewnotification.NotificationView.as_view(), name='notification'),
    path('editnotification/<int:notification_id>', viewnotification.NotificationView.as_view(), name='editnotification'),
    
    path('event/', viewevent.EventView.as_view(), name='event'),
    path('editevent/<int:event_id>', viewevent.EventView.as_view(), name='editevent'),
    
    path('social/', viewsocial.SocialView.as_view(), name='social')
    
    
    
    
]
