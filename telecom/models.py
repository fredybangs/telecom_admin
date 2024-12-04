from django.db import models


class Customers(models.Model):
    customerid = models.AutoField(db_column='CustomerID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)
    phonenumber = models.CharField(db_column='PhoneNumber', unique=True, max_length=15)
    email = models.CharField(db_column='Email', unique=True, max_length=100, blank=True, null=True)
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)
    accounttype = models.CharField(db_column='AccountType', max_length=50)
    subscriptionstatus = models.CharField(
        db_column='SubscriptionStatus', max_length=50, blank=True, null=True
    )

    class Meta:
        db_table = 'Customers'

    def __str__(self):
        return self.name


class NetworkInfrastructure(models.Model):
    cellsiteid = models.AutoField(db_column='CellSiteID', primary_key=True)
    location = models.CharField(db_column='Location', max_length=255)
    latitude = models.DecimalField(
        db_column='Latitude', max_digits=9, decimal_places=6, blank=True, null=True
    )
    longitude = models.DecimalField(
        db_column='Longitude', max_digits=9, decimal_places=6, blank=True, null=True
    )
    coveragearea = models.CharField(
        db_column='CoverageArea', max_length=255, blank=True, null=True
    )
    networktype = models.CharField(db_column='NetworkType', max_length=10)
    capacity = models.IntegerField(db_column='Capacity')

    class Meta:
        db_table = 'NetworkInfrastructure'

    def __str__(self):
        return f"Cell Site {self.cellsiteid} - {self.location}"


class PaymentMethods(models.Model):
    paymentmethodid = models.AutoField(db_column='PaymentMethodID', primary_key=True)
    methodtype = models.CharField(db_column='MethodType', max_length=50)
    methoddetails = models.CharField(
        db_column='MethodDetails', max_length=255, blank=True, null=True
    )

    class Meta:
        db_table = 'PaymentMethods'

    def __str__(self):
        return self.methodtype


class Payments(models.Model):
    paymentid = models.AutoField(db_column='PaymentID', primary_key=True)
    customerid = models.ForeignKey(
        Customers, on_delete=models.CASCADE, db_column='CustomerID', blank=True, null=True
    )
    paymentmethodid = models.ForeignKey(
        PaymentMethods,
        on_delete=models.CASCADE,
        db_column='PaymentMethodID',
        blank=True,
        null=True
    )
    paymentdate = models.DateTimeField(db_column='PaymentDate', blank=True, null=True)
    paymentamount = models.DecimalField(db_column='PaymentAmount', max_digits=10, decimal_places=2)
    paymentstatus = models.CharField(
        db_column='PaymentStatus', max_length=50, blank=True, null=True
    )

    class Meta:
        db_table = 'Payments'

    def __str__(self):
        return f"Payment {self.paymentid}"


class Services(models.Model):
    serviceid = models.AutoField(db_column='ServiceID', primary_key=True)
    servicename = models.CharField(db_column='ServiceName', max_length=100)
    description = models.TextField(db_column='Description', blank=True, null=True)
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Services'

    def __str__(self):
        return self.servicename


class ServicesSubscriptions(models.Model):
    subscriptionid = models.AutoField(db_column='SubscriptionID', primary_key=True)
    customerid = models.ForeignKey(
        Customers, on_delete=models.CASCADE, db_column='CustomerID', blank=True, null=True
    )
    servicetype = models.CharField(db_column='ServiceType', max_length=50)
    subscriptionplan = models.CharField(
        db_column='SubscriptionPlan', max_length=100, blank=True, null=True
    )
    subscriptionstatus = models.CharField(
        db_column='SubscriptionStatus', max_length=50, blank=True, null=True
    )
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)

    class Meta:
        db_table = 'ServicesSubscriptions'

    def __str__(self):
        return f"Subscription {self.subscriptionid}"
