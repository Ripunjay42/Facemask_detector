from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "ripunjay Admin"
admin.site.site_title = "ripunjay Admin Portal"
admin.site.index_title = "Welcome to Facemask_Detection"
urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('signup',views.signup,name='signup'),
    path('login',views.handlelogin,name='handlelogin'),
    path('logout',views.handlelogout,name='handlelogout'),
    path('img',views.handleimage,name='handleimage'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),
    path('mask_feed', views.mask_feed, name='mask_feed'),
	path('livecam_feed', views.livecam_feed, name='livecam_feed'),
    path('cap', views.capture_feed, name='cap'),
    path('gal', views.gallery, name='gal'),
    
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)