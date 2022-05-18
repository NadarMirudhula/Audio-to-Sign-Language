from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.views.generic import CreateView
from .models import ContactUs, User3

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext as _

class MessageCreateView(CreateView):
    model = ContactUs
    fields = ('name', 'email', 'subject', 'message')
# Create your views here.

def contactus(request):
    #print("Helllo")
    cs_name = request.POST.get("name")
    cs_email = request.POST.get("email")
    cs_subject = request.POST.get("subject")
    cs_comment = request.POST.get("comment")
    c = ContactUs(name = cs_name, email = cs_email, subject = cs_subject, message = cs_comment )
    c.save()
    return render(request,"contact.html",{"msg":"Thank You for your Feedback "})

def user_signup(request):
    if request.method == "POST":
        sp_username = request.POST.get("username")
        sp_name = request.POST.get("name")
        sp_email = request.POST.get("email")
        pw1 = request.POST.get("password")
        pw2 = request.POST.get("cpassword")
        if pw1 == pw2:
            val = True
            try:
                min_length = 8
                SpecialSym =['$', '@', '#', '%']
                if(len(pw1) < min_length):
                    val = False
                    return render(request,"signup.html",{"msg":"Length of password should be greater than 8"})
                if not any(char.isdigit() for char in pw1):
                    val = False
                    return render(request,"signup.html",{"msg":"Password should have at least one numeral"})
                if not any(char.isupper() for char in pw1):
                    val = False
                    return render(request,"signup.html",{"msg":"Password should have at least one uppercase letter"})
                if not any(char.islower() for char in pw1):
                    val = False
                    return render(request,"signup.html",{"msg":"Password should have at least one lowercase letter"})
                if not any(char in SpecialSym for char in pw1):
                    val = False
                    return render(request,"signup.html",{"msg":"Password should have at least one of the symbols $@#"})
                usr=User3.objects.get(username=sp_username,name=sp_name,email=sp_email,password=pw1)
                return render(request,"signup.html",{"msg":"User already exists"})

            except User3.DoesNotExist:
                usr=User3(username=sp_username,password=pw1,name=sp_name,email=sp_email)
                usr.save()
                return redirect("login")
        else:
            return render(request,"signup.html",{"msg":"passwords did not match"})
    else:
        return render(request,"signup.html")

def user_login(request):
    un = "DWFVS"
    pwd = "Dabcd@1234"
    if request.method == "POST":
        ln_username = request.POST.get("username")
        ln_password = request.POST.get("password")
        try:
            usr = User3.objects.get(username=ln_username,password=ln_password)
            return redirect("home")
        except ObjectDoesNotExist:
            return render(request,"login.html",{"msg":"Invalid Login"})
    else:
        return render(request,"login.html")


def user_logout(request):
	logout(request)
	return redirect("login")