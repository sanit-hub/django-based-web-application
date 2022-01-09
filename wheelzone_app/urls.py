from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from wheelzone import settings
from . import views
from .import adminviews, staffviews, userviews

#urls for admin wheelzone
urlpatterns = [

#admin or common Views
path('', views.loginpage, name="login"),
path('logincheck/', views.logincheck, name="logincheck"),
path('admin_page/', adminviews.admin_page, name="admin_page"),
path('staff_page/', staffviews.staff_page, name="staff_page"),
path('user_page/', userviews.user_page, name="user_page"),
path('addstaff_form/', adminviews.addstaff_form, name="addstaff_form"),
path('addstaff_def/', adminviews.addstaff_def, name="addstaff_def"),



path('signup/', views.signup, name="signup"),
path('signup_def/', views.signup_def, name="signup_def"),
path('logout_user/', views.logout_user, name="logout_user"),
path('staffs_view/', adminviews.staffs_view, name="staffs_view"),
path('staffsdelete_def/<id>/', adminviews.staffsdelete_def, name="staffsdelete_def"),
path('customers_view/', adminviews.customers_view, name="customers_view"),
path('customersdelete_def/<id>/', adminviews.customersdelete_def, name="customersdelete_def"),
path('staffs_update/', adminviews.staffs_update, name="staffs_update"),
path('staffsupdate_def/', adminviews.staffsupdate_def, name="staffsupdate_def"),
path('accountupdate_form/', adminviews.accountupdate_form, name="accountupdate_form"),
path('accountupdate_def/', adminviews.accountupdate_def, name="accountupdate_def"),




#commen urls for staff and admin
path('servicestatus_admin/', adminviews.servicestatus_admin, name="servicestatus_admin"),
path('deleteservicepro_def/<id>/', adminviews.deleteservicepro_def, name="deleteservicepro_def"),
path('approveservicepro_def/<id>/', adminviews.approveservicepro_def, name="approveservicepro_def"),
path('servicedpro_def/<id>/', adminviews.servicedpro_def, name="servicedpro_def"),
path('addofflinecustomer_form/', adminviews.addofflinecustomer_form, name="addofflinecustomer_form"),
path('offlinecustomers_view/', adminviews.offlinecustomers_view, name="offlinecustomers_view"),
path('addofflinecustomer_def/', adminviews.addofflinecustomer_def, name="addofflinecustomer_def"),
path('offlinecustomersdelete_def/<id>/', adminviews.offlinecustomersdelete_def, name="offlinecustomersdelete_def"),
path('staffsupdates_staff/', staffviews.staffsupdates_staff, name="staffsupdates_staff"),
path('staffsupdatestaff_def/', staffviews.staffsupdatestaff_def, name="staffsupdatestaff_def"),
path('offlinecustomer_update', adminviews.offlinecustomer_update, name="offlinecustomer_update"),
path('offlinecustomerupdate_def', adminviews.offlinecustomerupdate_def, name="offlinecustomerupdate_def"),
path('billing_form/<id>/', adminviews.billing_form, name="billing_form"),
path('salesreportoffline_def/', adminviews.salesreportoffline_def, name="salesreportoffline_def"),

path('billingform_online/<id>/', adminviews.billingform_online, name="billingform_online"),
path('salesreportonline_def/', adminviews.salesreportonline_def, name="salesreportonline_def"),
path('salesreportview_form/', adminviews.salesreportview_form, name="salesreportview_form"),
path('salesreportview_table/', adminviews.salesreportview_table, name="salesreportview_table"),
path('salesreportdelete_def/<id>/', adminviews.salesreportdelete_def, name="salesreportdelete_def"),
path('addparts_form/', adminviews.addparts_form, name="addparts_form"),
path('addparts_def/', adminviews.addparts_def, name="addparts_def"),
path('viewparts_table/', adminviews.viewparts_table, name="viewparts_table"),
path('partsdelete_def/<id>/', adminviews.partsdelete_def, name="partsdelete_def"),
path('viewmessages_table', adminviews.viewmessages_table, name="viewmessages_table"),



#urls for  customer

path('servicerequest_def/', userviews.servicerequest_def, name="servicerequest_def"),
path('servicestatus_def/', userviews.servicestatus_def, name="servicestatus_def"),
path('deleteservice_def/<id>/', userviews.deleteservice_def, name="deleteservice_def"),
path('approveofflineservice_def/<id>/', adminviews.approveofflineservice_def, name="approveofflineservice_def"),
path('updateaccountcustomer_form', userviews.updateaccountcustomer_form, name="updateaccountcustomer_form"),
path('customeraccountupdate_def_form', userviews.customeraccountupdate_def, name="customeraccountupdate_def"),
path('message_form', userviews.message_form, name="message_form"),
path('messageform_def', userviews.messageform_def, name="messageform_def"),



]
