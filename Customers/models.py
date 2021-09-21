from django.db import models

# Create your models here.

#  HOME PAGE CONTACT FORM

class Contact(models.Model):
    name=models.CharField(max_length=170)
    email=models.EmailField(max_length=170)
    organisation=models.CharField(max_length=250)
    query=models.TextField()
    date=models.DateField()
    def __str__(self):
     return self.organisation
#register table
class Userinfo(models.Model):
    UserID=models.AutoField(primary_key=True)
    name=models.CharField(max_length=170)
    name_of_organization=models.CharField(max_length=170)
    organization_address=models.CharField(max_length=170)
    contact=models.CharField(max_length=12)
    email=models.EmailField(max_length=170)
    gst_no =models.CharField(max_length=15)
    password=models.CharField(max_length=16)
    date=models.DateField()
    status=models.CharField(max_length=122)


class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    order_name=models.CharField(max_length=300)
    material=models.CharField(max_length=200)
    dem=models.CharField(max_length=5)
    size=models.CharField(max_length=20)
    quantity=models.CharField(max_length=25)
    specification= models.CharField(max_length=20)
    design=models.CharField(max_length=10, default=False)
    type_of_print=models.CharField(max_length=10, default=None)
    tapping=models.CharField(max_length=20)
    Cust=models.ForeignKey(Userinfo, on_delete=models.CASCADE)
    cust_name=models.CharField(max_length=120)
    date=models.DateField()
    status=models.CharField(max_length=30, default='ongoing')
    
class OrderUpdt(models.Model):
    updtId=models.AutoField(primary_key=True)
    order_id=models.IntegerField()
    updtDesc=models.CharField(max_length=5000)
    date=models.DateField()

class Process(models.Model):
    processid=models.AutoField(primary_key=True)
    order_id= models.IntegerField()
    raw_material=models.CharField(max_length=122)
    design=models.CharField(max_length=122)
    printing=models.CharField(max_length=122)
    cylsize=models.IntegerField(blank= True , null=True )
    date=models.DateField()




