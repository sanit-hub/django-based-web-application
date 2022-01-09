from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from wheelzone_app.models import customuser,servicerequestcustomer,feedback
from django.http import HttpResponseRedirect, HttpResponse


def user_page(request):

    return render(request, 'wheelzone/userpage.html')

def servicerequest_def(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('user_page')
    else:

        vehicle = request.POST.get('vehicle')
        model = request.POST.get('model')
        regno = request.POST.get('regno')
        location = request.POST.get('location')
        services = request.POST.get('services')
        phonenumber = request.POST.get('phonenumber')
        current_user = request.user

        try:

            service_request = servicerequestcustomer(customer_id=current_user,vehicle=vehicle,model=model,regno=regno,location=location,services=services
            ,phonenumber=phonenumber,service_status=0)
            service_request.save()
            messages.success(request, "Registred sucessfully.")
            return redirect('user_page')
        except:
                return render(request,'wheelzone/failed1.html')



def servicestatus_def(request):
    current_user = request.user
    service_data = servicerequestcustomer.objects.filter(customer_id=current_user)
    context = {
       "service_data": service_data
       }
    return render(request, 'wheelzone/servicestatus.html', context)


def deleteservice_def(request, id=None):
    service =servicerequestcustomer.objects.get(id=id)
    service.delete()
    return redirect('servicestatus_def')


def updateaccountcustomer_form(request):
     customer_data = customuser.objects.filter(user_type=3,id=request.user.id)
     context = {
        "customer_data": customer_data
        }
     return render(request, 'wheelzone/updateaccount_customer.html', context)

def customeraccountupdate_def(request):
        if request.method != "POST":
           messages.error(request, "Invalid Method")

        else:
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')

        try:

            user = customuser.objects.get(id=request.user.id)
            if firstname != None and firstname != "":
                user.first_name = firstname
            if lastname != None and lastname != "":
                user.last_name = lastname
            if username != None and username != "":
                user.username = username
            if email != None and email != "":
                user.set_email(email)
            if password != None and password != "":
                user.set_password(password)
            user.save()
            messages.success(request, "Registerd Successfully!")
            return redirect('user_page')



        except:
                return render(request,'wheelzone/failed1.html')


def message_form(request):

    return render(request, 'wheelzone/message_form.html')

def messageform_def(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('message_form')
    else:

        message = request.POST.get('message')
        current_user = request.user

        try:

            message = feedback(customer_id=current_user,feedback=message)
            message.save()
            messages.success(request, "Registred sucessfully.")
            return redirect('user_page')
        except:
                return render(request,'wheelzone/failed1.html')
