from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

from wheelzone_app.EmailBackEnd import EmailBackEnd
from wheelzone_app.models import customuser





def loginpage(request):
    return render(request,'wheelzone/login.html')


def logincheck(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'),
                                         password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            # return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
            if user_type == '1':
                return redirect('admin_page')

            elif user_type == '2':
                # return HttpResponse("Staff Login")
                return redirect('staff_page')

            elif user_type == '3':
                # return HttpResponse("Student Login")
                return redirect('user_page')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            # return HttpResponseRedirect("/")
            return redirect('login')


def signup(request):
    return render(request,'wheelzone/signup.html')

def signup_def(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
    else:
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')


    try:
         user = authenticate(request, username=username,email=email,password=password)

         if user is None:
          user = customuser.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname, user_type=3)
          user.save()
          messages.success(request, "Registerd Successfully!")
          subject = 'welcome to wheelzone'
          message = f'Hi {user.username}, thank you for registering in wheelzone.'
          email_from = settings.EMAIL_HOST_USER
          recipient_list = [user.email,]
          send_mail( subject, message, email_from, recipient_list )
          return redirect('login')
    except:

        return render(request,'wheelzone/failed1.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
