from django.contrib import admin
from .models import (
    Customers,
    NetworkInfrastructure,
    PaymentMethods,
    Payments,
    Services,
    ServicesSubscriptions,
)

@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('customerid', 'name', 'phonenumber', 'email', 'accounttype', 'subscriptionstatus')
    search_fields = ('name', 'phonenumber', 'email')
    list_filter = ('accounttype', 'subscriptionstatus')

@admin.register(NetworkInfrastructure)
class NetworkInfrastructureAdmin(admin.ModelAdmin):
    list_display = ('cellsiteid', 'location', 'networktype', 'capacity')
    search_fields = ('location', 'networktype')
    list_filter = ('networktype',)

@admin.register(PaymentMethods)
class PaymentMethodsAdmin(admin.ModelAdmin):
    list_display = ('paymentmethodid', 'methodtype', 'methoddetails')
    search_fields = ('methodtype',)
    list_filter = ('methodtype',)

@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('paymentid', 'customerid', 'paymentmethodid', 'paymentdate', 'paymentamount', 'paymentstatus')
    search_fields = ('customerid__name', 'paymentstatus')
    list_filter = ('paymentstatus',)

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('serviceid', 'servicename', 'price')
    search_fields = ('servicename',)
    list_filter = ('servicename',)

@admin.register(ServicesSubscriptions)
class ServicesSubscriptionsAdmin(admin.ModelAdmin):
    list_display = (
        'subscriptionid', 'customerid', 'servicetype', 'subscriptionplan',
        'subscriptionstatus', 'startdate', 'enddate'
    )
    search_fields = ('servicetype', 'customerid__name')
    list_filter = ('servicetype', 'subscriptionstatus')
