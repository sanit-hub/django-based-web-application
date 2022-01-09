from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class customuser(AbstractUser):
    user_type_data = ((1, "admin"), (2, "staff"), (3, "customer"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)



class servicerequestcustomer(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(customuser, on_delete=models.CASCADE)
    vehicle= models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    regno = models.TextField()
    location = models.TextField()
    services = models.TextField()
    phonenumber = models.TextField()
    service_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class feedback(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(customuser, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class offlinecustomer(models.Model):
    id = models.AutoField(primary_key=True)
    firstname= models.TextField()
    lastname= models.TextField()
    vehicle= models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    regno = models.TextField()
    location = models.TextField()
    services = models.TextField()
    phonenumber = models.TextField()
    service_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class salesreport(models.Model):
    id = models.AutoField(primary_key=True)
    firstname= models.TextField()
    lastname= models.TextField()
    vehicle= models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    regno = models.TextField()
    location = models.TextField()
    services = models.TextField()
    phonenumber = models.TextField()
    billamount =  models.TextField()
    month =  models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class parts(models.Model):
    id = models.AutoField(primary_key=True)
    partname= models.TextField()
    count= models.TextField()
    sellername= models.TextField()
    companyname= models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.TextField()
    cost = models.TextField()
    gst = models.TextField()
    date = models.TextField()
    objects = models.Manager()
