from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from wheelzone_app.models import customuser,servicerequestcustomer,offlinecustomer,salesreport,parts,feedback
from django.views.decorators.csrf import csrf_exempt

def admin_page(request):
    all_services_count = servicerequestcustomer.objects.all().count()
    all_staff_count = customuser.objects.filter(user_type=2).count()
    all_message_count = feedback.objects.all().count()

    all_customer_count = customuser.objects.filter(user_type=3).count()
    context={
           "all_services_count": all_services_count,
           "all_staff_count": all_staff_count,
           "all_customer_count": all_customer_count,
           "all_message_count" :all_message_count
}
    return render(request, 'wheelzone/adminpage.html',context)



def addstaff_form(request):
    return render(request, 'wheelzone/addstaff_form.html')

def addofflinecustomer_form(request):
    return render(request, 'wheelzone/addofflinecustomer_form.html')

def addofflinecustomer_def(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
    else:
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        vehicle = request.POST.get('vehicle')
        model = request.POST.get('model')
        regno = request.POST.get('regno')
        location = request.POST.get('location')
        services= request.POST.get('services')
        phonenumber = request.POST.get('phonenumber')




    try:
        service_request = offlinecustomer(firstname=firstname,lastname=lastname,vehicle=vehicle,model=model,regno=regno,location=location,services=services
        ,phonenumber=phonenumber,service_status=0)

        service_request.save()
        messages.success(request, "Registred Successfully!")
        return redirect('admin_page')
    except:
             return render(request,'wheelzone/failed1.html')


def addstaff_def(request):
        if request.method != "POST":
            messages.error(request, "Invalid Method")
        else:
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')

        try:
            user = authenticate(request, username=username ,email=email,password=password)

            if user is None:
             user = customuser.objects.create_user(username=username, password=password, email=email,
                                                  first_name=firstname,
                                                  last_name=lastname, user_type=2)

             user.save()
             messages.success(request, "Registerd Successfully!")
             return redirect('admin_page')

        except:
                return render(request,'wheelzone/failed1.html')


def servicestatus_admin(request):
    service_data = servicerequestcustomer.objects.all()
    context = {
       "service_data": service_data
       }
    return render(request, 'wheelzone/servicestatus_pro.html', context)


def deleteservicepro_def(request, id=None):
        service = servicerequestcustomer.objects.get(id=id)
        service.delete()
        return redirect('servicestatus_admin')


def approveservicepro_def(request, id=None):
        approve = servicerequestcustomer.objects.get(id=id)
        approve.service_status = 1
        approve.save()
        return redirect('servicestatus_admin')


def servicedpro_def(request, id=None):
        serviced = servicerequestcustomer.objects.get(id=id)
        serviced.service_status = 2
        serviced.save()
        return redirect('servicestatus_admin')

def staffs_view(request):
     staff_data = customuser.objects.filter(user_type=2)
     context = {
        "staff_data": staff_data
        }
     return render(request, 'wheelzone/staffview.html', context)

def staffsdelete_def(request, id=None):
        staff = customuser.objects.get(id=id)
        staff.delete()
        return redirect('staffs_view')

def customers_view(request):
     customers_data = customuser.objects.filter(user_type=3)
     context = {
        "customers_data": customers_data
        }
     return render(request, 'wheelzone/customerview.html', context)

def customersdelete_def(request, id=None):
        staff = customuser.objects.get(id=id)
        staff.delete()
        return redirect('customers_view')


def staffs_update(request):
     staff_data = customuser.objects.filter(user_type=2)
     context = {
        "staff_data": staff_data
        }
     return render(request, 'wheelzone/staff_update.html', context)


def staffsupdate_def(request):
    if request.method != "POST":
       messages.error(request, "Invalid Method")

    else:
        id = request.POST.get('id')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

    try:
        user = customuser.objects.get(id=id)
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
        return redirect('admin_page')


    except:
            return render(request,'wheelzone/failed1.html')

def offlinecustomers_view(request):
     customers_data = offlinecustomer.objects.all()
     context = {
        "customers_data": customers_data
        }
     return render(request, 'wheelzone/offlinecustomers_view.html', context)

def offlinecustomersdelete_def(request, id=None):
        customer = offlinecustomer.objects.get(id=id)
        customer.delete()
        return redirect('offlinecustomers_view')

def approveofflineservice_def(request, id=None):
        approve = offlinecustomer.objects.get(id=id)
        approve.service_status = 1
        approve.save()
        return redirect('offlinecustomers_view')



def accountupdate_form(request):
     admin_data = customuser.objects.filter(user_type=1,id=request.user.id)
     context = {
        "admin_data": admin_data
        }
     return render(request, 'wheelzone/accountupdate.html', context)


def accountupdate_def(request):
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
            return redirect('admin_page')



        except:
            messages.error(request, "Failed to Add Staff!")
            return redirect('accountupdate_form')


def offlinecustomer_update(request):
     customer_data =  offlinecustomer.objects.all()
     context = {
        "customer_data": customer_data

        }
     return render(request, 'wheelzone/offlinecustomer_update.html', context)

def offlinecustomerupdate_def(request):
        if request.method != "POST":
            messages.error(request, "Invalid Method")
        else:
            id = request.POST.get('id')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            vehicle = request.POST.get('vehicle')
            model = request.POST.get('model')
            regno = request.POST.get('regno')
            location = request.POST.get('location')
            services= request.POST.get('services')
            phonenumber = request.POST.get('phonenumber')


        try:
            user = offlinecustomer.objects.get(id=id)
            if firstname != None and firstname != "":
                user.first_name = firstname
            if lastname != None and lastname != "":
                user.last_name = lastname
            if vehicle != None and username != "":
                user.vehicle = vehicle
            if regno != None and email != "":
                user.regno = regno
            if model != None and model != "":
                user.model = model
            if location != None and location != "":
                user.location = location
            if services != None and services != "":
                user.services = services
            if phonenumber != None and phonenumber != "":
                user.phonenumber = phonenumber
            user.save()

            messages.success(request, "Update Successfully!")
            return redirect('offlinecustomer_update')


        except:

           messages.error(request, "Failed to Add Staff!")
           return redirect('offlinecustomer_update')


def billing_form(request, id=None):
    customer_data = offlinecustomer.objects.filter(id=id)
    context = {
          "customer_data": customer_data
              }
    return render(request, 'wheelzone/billing_form.html', context)


def billingform_online(request, id=None):
    customer_data = servicerequestcustomer.objects.filter(customer_id_id=id)
    customer_name = customuser.objects.filter(id=id)

    context = {
          "customer_data": customer_data,
          "customer_name":customer_name,
              }


    return render(request, 'wheelzone/billingform_online.html', context)

def salesreportonline_def(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
    else:
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        vehicle = request.POST.get('vehicle')
        model = request.POST.get('model')
        regno = request.POST.get('regno')
        location = request.POST.get('location')
        services= request.POST.get('services')
        phonenumber = request.POST.get('phonenumber')
        billamount = request.POST.get('billamount')
        month = request.POST.get('month')



    try:
        service_request = salesreport(firstname=firstname,lastname=lastname,vehicle=vehicle,model=model,regno=regno,location=location,services=services
        ,phonenumber=phonenumber,billamount=billamount,month=month)

        service_request.save()
        messages.success(request, "Registred Successfully!")
        context={
            "firstname": firstname,
            "lastname": lastname,
            "vehicle": vehicle,
            "model":  model,
            "regno": regno,
            "services": services,
            "billamount":  billamount,
            "month": month,
        }
        return render(request, 'wheelzone/printbill_table.html', context)



    except:
            return render(request,'wheelzone/failed1.html')

def salesreportoffline_def(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
    else:
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        vehicle = request.POST.get('vehicle')
        model = request.POST.get('model')
        regno = request.POST.get('regno')
        location = request.POST.get('location')
        services= request.POST.get('services')
        phonenumber = request.POST.get('phonenumber')
        billamount = request.POST.get('billamount')
        month = request.POST.get('month')


    try:
        service_request = salesreport(firstname=firstname,lastname=lastname,vehicle=vehicle,model=model,regno=regno,location=location,services=services
        ,phonenumber=phonenumber,billamount=billamount,month=month)

        service_request.save()
        messages.success(request, "Registred Successfully!")
        context={
            "firstname": firstname,
            "lastname": lastname,
            "vehicle": vehicle,
            "model":  model,
            "regno": regno,
            "services": services,
            "billamount":  billamount,
            "month": month,
        }
        return render(request, 'wheelzone/printbill_table.html', context)


    except:
            return render(request,'wheelzone/failed1.html')

def salesreportview_form(request):

     return render(request, 'wheelzone/salesreportview_form.html')

def salesreportview_table(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
    else:
        firstdate = request.POST.get('firstdate')
        lastdate = request.POST.get('lastdate')
        sales_data = salesreport.objects.filter(month__range=[firstdate, lastdate])
        context = {
           "sales_data": sales_data
               }
    return render(request, 'wheelzone/salesreportview_table.html',context)


def salesreportdelete_def(request, id=None):
    sales = salesreport.objects.get(id=id)
    sales.delete()
    return redirect('salesreportview_table')


def addparts_form(request):
    return render(request, 'wheelzone/addparts_form.html')




def addparts_def(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
    else:
        partname = request.POST.get('partname')
        count = request.POST.get('count')
        sellername = request.POST.get('sellername')
        companyname = request.POST.get('companyname')
        color = request.POST.get('color')
        model= request.POST.get('model')
        cost= request.POST.get('cost')
        gst = request.POST.get('gst')
        date = request.POST.get('date')


    try:
        service_request = parts(partname=partname,count=count,sellername=sellername,companyname=companyname,color=color,model=model,cost=cost
        ,gst=gst,date=date)

        service_request.save()
        messages.success(request, "Registred Successfully!")
        return redirect('addparts_form',context)



    except:
        messages.error(request, "Failed to Add parts!")
        return redirect('addparts_form')



def viewparts_table(request):
     parts_data = parts.objects.all()
     context = {
        "parts_data": parts_data
        }
     return render(request, 'wheelzone/viewparts_table.html', context)


def partsdelete_def(request, id=None):
     part= parts.objects.get(id=id)
     part.delete()
     return redirect('viewparts_table')


def viewmessages_table(request):
     message = feedback.objects.all()
     context = {
        "message": message
        }
     return render(request, 'wheelzone/viewmessages_table.html', context)
