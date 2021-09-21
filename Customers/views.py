from django.shortcuts import render,HttpResponse,redirect
from Customers.models import  Contact, Userinfo,Order, OrderUpdt,Process
from django.db import IntegrityError
import datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate,login


recent=0


def home(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        org=request.POST.get('Organisation')
        message=request.POST.get('message')
        contact=Contact(name=name, email=email, organisation=org, query=message, date=datetime.datetime.today())
        contact.save()
        Subject = 'One client responded'
        msg="The following Client contacted you through your website. Here are the details:\nName of the Client :"+contact.name+"\nOrganisation : "+contact.organisation+"\nE-mail Address : "+contact.email+ "\nClient's Message :"+contact.query+"\nThanks."
        email_from=settings.EMAIL_HOST_USER
        recipient_list=['arshriar41@gmail.com']
        send_mail(Subject,msg,email_from,recipient_list)
        messages.success(request, 'Form Submitted Successfully!')
    return render(request, 'home.html')

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('email')
        password=request.POST.get('pswd')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('login/')
        else:
            messages.error(request,'This is not a valid email and password or your account is inactive')
            return redirect('/login')
    return render(request, 'login.html')

def register(request):
    if request.method =='POST':
        #get parameters
        name=request.POST.get('name')
        org_name = request.POST.get('organization')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        email=request.POST.get('email')
        gst=request.POST.get('gst')
        pswd=request.POST.get('pswd')
        repswd=request.POST.get('repswd')
        if pswd!=repswd:
            messages.error(request, 'Passwords did not match.Please try again.')
            return redirect('/register')
        if len(contact)!=10:
            messages.error(request,'Please enter valid number')
            return redirect('/register')
        if len(gst)!=15 or not gst.isalnum():
            messages.error(request,'Enter valid GST number')
            return redirect('/register')
        rege=Userinfo( name=name, name_of_organization = org_name, organization_address =address, contact=contact, email=email, gst_no=gst, password=pswd, date=datetime.datetime.today(),status='inactive') 
        try:
            myuser=User.objects.create_user(email,email,pswd)
            myuser.is_active=False
            myuser.save()
        except IntegrityError:
            messages.error(request, 'Account already exists')
            return redirect('/register')
        rege.save()
        messages.success(request,"Your account has been successfully created. Your Details will be verified by the Firm and your account will be activated soon.")
        Subject = 'One client registered'
        msg="The following Client registered on your website. Here are the details:\nName of the Client :"+rege.name+"\nOrganisation Name : "+rege.name_of_organization+"\nAddress : "+rege.organization_address+"\n Contact Number : "+rege.contact+"\nE-mail Address : "+rege.email+ "\n GST Number : "+rege.gst_no+"\n If interest, set the status of this client to active on admin site.\n Thanks."
        email_from=settings.EMAIL_HOST_USER
        recipient_list=['arshriar41@gmail.com']
        send_mail(Subject,msg,email_from,recipient_list)
    return render(request, 'register.html')

def product_range(request):
    return render(request, 'products.html')

def logoutuser(request):
	logout(request)
	return redirect('/')
	
def dashboard(request):
    guest=Userinfo.objects.get(email=request.user)
    ordd=Order.objects.filter(Cust=guest)
    active=[]
    inactive=[]
    for i in ordd:
        if i.status=='ongoing':
            active.append(i)
        else:
            inactive.append(i)
    context={'active':active,'inactive':inactive}
    return render(request, 'dashboard.html',context)
    return render(request, 'dashboard.html')

def profile(request):
    obj=Userinfo.objects.get(email=request.user.username)
    user={
        'name':obj.name,
        'organization':obj.name_of_organization,
        'address':obj.organization_address,
        'contact':obj.contact,
        'email':obj.email,
        'gst':obj.gst_no,
        'pswd':obj.password         
    }
    return render(request, 'profile.html',user)

def LoggedProducts(request):
    return render(request, 'LoggedProducts.html')

@login_required(login_url='/login')
def Product_desc(request,pid):
    global recent
    if request.method=='POST':
        name=request.POST.get('name')
        material=request.POST.getlist('mat[]')
        dem=request.POST['dem']
        size=request.POST.get('size')
        qty=request.POST.get('qty')
        speci=request.POST['sp']
        tape=request.POST['tape']
        guest=Userinfo.objects.get(email=request.user)
        if speci=='print':
            design=request.POST.get('design')
            typeop = request.POST.get('type')
        else:
        	design="No"
        	typeop="None"
        
        ordd=Order(order_name=name, material=material, dem=dem, size=size, quantity=qty, specification=speci,design=design, type_of_print=typeop, tapping=tape, Cust=guest, cust_name=guest.name_of_organization,date=datetime.datetime.today())
        ordd.save()
        recent=ordd.order_id
        update=OrderUpdt(order_id=ordd.order_id,updtDesc='Your order has been placed successfully.', date=datetime.datetime.today())
        update.save()
        process=Process(order_id=ordd.order_id, raw_material=ordd.material, design=ordd.design, printing=ordd.type_of_print,date=datetime.datetime.today())
        process.save()
        return redirect('/summary')
    temp='product'+str(pid)+'.html'
    return render(request,temp)

def summary(request):
    guest=Userinfo.objects.get(email=request.user)
    ordd=Order.objects.get(Cust=guest, order_id=recent)
    context={ 'ordd' :ordd, 'guest': guest} 
    return render(request,'summary.html',context)

def tracker(request):
    if request.method=='POST':
        key=request.POST.get('orderid')
        guest=Userinfo.objects.get(email=request.user)
        try:
            orders=Order.objects.get(order_id=key , Cust=guest)

            if orders:
                updts=OrderUpdt.objects.filter(order_id=key)

                context={'updts':updts}
                return render(request, 'tracker.html',context)
            messages.error(request,'No details found. Enter correct details')
            return redirect('/trackorder')
        except:
            messages.error(request,'No details found. Enter correct details')
            return redirect('/trackorder')

    return render(request, 'tracker.html')
