from django.shortcuts import render,HttpResponse,redirect
from django.http.response import StreamingHttpResponse
from home.camera import VideoCamera, IPWebCam, MaskDetect, LiveWebCam, Capture
from datetime import datetime
from home.models import Contact
from home.models import Image
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
import numpy as np
from PIL import ImageGrab
import time
import random
import os
import keyboard
import base64
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def home(request):
    #context={"var1":"ripunjay is great"}
    return render(request,'home.html')
    #return HttpResponse("ripunjay")
#def home(request):
 #   return render(request,'index.html')
def about(request):
    return render(request,'about.html')
    #return HttpResponse("about")
@csrf_exempt
def contact(request):
    if request.method == "POST" :
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<5:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
            contact.save()
            messages.success(request, 'your message has been sent!')
    return render(request,'contact.html')
    #return HttpResponse("u can contact us")
@csrf_exempt
def signup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " account successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")
@csrf_exempt      
def handlelogin(request):
    #return render(request,'login.html')
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            #messages.success(request, "Successfully Logged In")
            return render(request,"img.html")
            #return render("exit")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404 - Not found")

    #return HttpResponse("login")


def handlelogout(request):
    #return render(request,'logout.html')
    logout(request)
    messages.success(request, "Successfully logged out")
    #return redirect('home')
    return render(request,'home.html')

@csrf_exempt
def  handleimage(request):
    if request.method=="POST":
            return render(request, 'img.html')
    return HttpResponse("404 - Not found")

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')


def webcam_feed(request):
	return StreamingHttpResponse(gen(IPWebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')


def mask_feed(request):
	return StreamingHttpResponse(gen(MaskDetect()),
					content_type='multipart/x-mixed-replace; boundary=frame')
					
def livecam_feed(request):
	return StreamingHttpResponse(gen(LiveWebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')

@csrf_exempt
def capture_feed(request):
    if request.method == "POST":
        for i in range(0,1000):
            if keyboard.is_pressed('q'):
                 break
            else:
                image = ImageGrab.grab(bbox=(480,160,1440,890))
                # image = cv2.cvtColor(np.array(image),
                #             cv2.COLOR_RGB2BGR)
                # path = r"C:\Users\RIPUN_PRO\Desktop\project\hello\images"
                a = 'mask_Or_Not'
                b=random.randint(0000, 9999)
                c='.png'
                img=a+str(b)+c
                # cv2.imwrite(os.path.join(path , img), image)
                image.save(os.path.join(settings.MEDIA_ROOT, img))
                with open(os.path.join(settings.MEDIA_ROOT, img), 'rb') as file:
                    pic = file.read()
                image_obj=Image.objects.create(picture= pic)
                image_obj.save()
                time.sleep(5)
        return render(request, 'img.html')
    return HttpResponse("404 - Not found")

@csrf_exempt
def gallery(request):
    if request.method == "POST":
        obj = Image.objects.get(id=16)
        image_data = base64.b64encode(obj.picture).decode()
        data = {
            'imgs' : image_data
        }
        return render(request, 'gall.html',data)
    return HttpResponse("404 - Not found")

def exit(request):
    return(request,'cemera.html') 
    
    