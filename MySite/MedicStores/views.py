from django.shortcuts import render
from django.core.mail import send_mail
from MedicStores.forms import UserForm, UserInfoForm
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import models
# Create your views here.
def index(request):
    return render(request,"index.html")

def checkout(request):
    return render(request,"checkout.html")

def cart(request):
    return render(request,"cart.html")

def about(request):
    return render(request,"about.html")

def disclaimer(request):
    return render(request,"disclaimer.html")

def shipping(request):
    return render(request,"shipping.html")

def privacy(request):
    return render(request,"privacyPolicy.html")

def term(request):
    return render(request,"term.html")

def contact(request):
    form = contactusform(request.POST)
    if request.method == "POST":
        form = contactusform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['fullname']
            email=form.cleaned_data['email']
            contact_no=form.cleaned_data['contact_no']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            full_message="Name= " +name+"\n Email="+email+"\nContact No= "+contact_no+"\nSubject= "+subject+"\n Message= "+message
            send_mail("Message from visitor",full_message,"manthanm008@gmail.com",['manthanm008@gmail.com'],fail_silently=False)
        else:
            form = contactusform()
    else:
        return render(request,'contact.html',{ 'form':form })

def sitemap(request):
    return render(request,"sitemap.html")

def client_register(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form= UserInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.is_staff=False
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            registered=True
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form= UserInfoForm()
    return render(request,'registration.html',
        {'user_form':user_form,
        'profile_form':profile_form,
        'registered':registered})
def client_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account is not active')
        else:
            print("Someone tried to login and failed")
            return HttpResponse('Invalid Login Details')
    else:
        return render(request,'login.html',{})
def client_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
