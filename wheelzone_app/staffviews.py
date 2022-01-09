from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from wheelzone_app.models import customuser,servicerequestcustomer,offlinecustomer


def staff_page(request):
    all_services_count = servicerequestcustomer.objects.all().count()
    all_staff_count = customuser.objects.filter(user_type=2).count()
    all_customer_count = customuser.objects.filter(user_type=3).count()
    context={
           "all_services_count": all_services_count,
           "all_customer_count": all_customer_count,
}
    return render(request, 'wheelzone/staffpage.html',context)


def staffsupdates_staff(request):
    staff_data = customuser.objects.filter(user_type=2,id=request.user.id)
    context={
       "staff_data": staff_data
 }
    return render(request, 'wheelzone/staffupdate_staff.html',context)

def staffsupdatestaff_def(request):
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
        return redirect('staff_page')


    except:
            return render(request,'wheelzone/failed1.html')
