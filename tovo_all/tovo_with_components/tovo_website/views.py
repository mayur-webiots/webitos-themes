from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

import re
# Create your views here.

# Home Page:
# @login_required(login_url='/login')
def index(request):

    # contact us 

    if 'send' in request.POST:
        user_name = request.POST['fullname']
        user_phone_number = request.POST['phone']
        user_email = request.POST['email']
        user_message = request.POST['message']
        
        if user_name == '' or user_phone_number == '' or user_email == '' or user_message == '':
            messages.error(request,'Some fields are empty! Please fill all the fields and try again!')
        else:
            phone_number_is_valid = re.search("^(\+\d{1,3})?,?\s?\d{8,13}", user_phone_number)
            if phone_number_is_valid:
                email_is_valid = re.search("^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$", user_email)
                if email_is_valid:
                    
                    tbl_contact_us = contact_us(user_name = user_name,user_phone_number=user_phone_number,user_email=user_email,user_message=user_message)
                    tbl_contact_us.save()
                    
                    
                else:
                    messages.error(request,'Invalid Email!')
            else:
                messages.error(request,'Invalid Phone Number!')
            
    
    #subscribe

    if 'btn_subscribe' in request.POST:
        email = request.POST['EMAIL']
        if email == '':
            messages.error(request,'Please enter your email!')
        else:
            email_is_valid = re.search("^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$", email)
            if email_is_valid:
                subscribe = subscription.objects.filter(email=email)
                if subscribe.exists():
                    messages.info(request,'You are already subscribed!')
                else:
                    subscribe = subscription(email=email)
                    subscribe.save()
                    return redirect('other_page_thank_you')
            else:
                messages.error(request,'Invalid Email! Please enter a valid email.')

    return render(request,'tovo_website/index.html')

# blog pages --->

def blog(request):
    return render(request,'tovo_website/blog/blog.html')

def blog_details(request):
    return render(request,'tovo_website/blog/blog-details.html')

def blog_details_with_leftsidebar(request):
    return render(request,'tovo_website/blog/blog-details-with-leftsidebar.html')

def blog_details_with_rightsidebar(request):
    return render(request,'tovo_website/blog/blog-details-with-rightsidebar.html')

def blogs_leftside(request):
    return render(request,'tovo_website/blog/blogs-leftside.html')

def blogs_rightside(request):
    return render(request,'tovo_website/blog/blogs-rightside.html')


# Other Page Pages --->

def other_page_404(request):
    return render(request,'tovo_website/other_page/404.html')

def other_page_download(request):
    return render(request,'tovo_website/other_page/download.html')

def other_page_faq(request):
    return render(request,'tovo_website/other_page/faq.html')

def other_page_forget_pwd(request):
    return render(request,'tovo_website/other_page/forget-pwd.html')

def other_page_review(request):
    return render(request,'tovo_website/other_page/review.html')

def other_page_sign_in(request):

    if 'btn_sign_in' in request.POST:

        email = request.POST['email']
        password = request.POST['password']

        if email == '' or password == '':
            messages.error(request,'ome fields are empty! Please fill all the fields and try again!')
        else:
            email_is_valid = re.search("^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$", email)
            if email_is_valid:

                # authenticate User And log User in, add redirect page and remove pass from below
                # return redirect('index')
                pass
            else:
                messages.error(request,'Invalid Email!')

    return render(request,'tovo_website/other_page/sign-in.html')

def other_page_sign_up(request):

    # sign up
    if 'btn_sign_up' in request.POST:

        name = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if name == '' or phone == '' or email == '' or password == '' or confirm_password == '':
            messages.error(request,'Some fields are empty! Please fill all the fields and try again!')
            return redirect('other_page_sign_up')
        else:
            phone_number_is_valid = re.search("^(\+\d{1,3})?,?\s?\d{8,13}", phone)
            if phone_number_is_valid:
                email_is_valid = re.search("^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$", email)
                if email_is_valid:
                    if password == confirm_password:

                        # Insert Data into Database and remove pass
                        # return redirect('index')
                        pass
                    else:
                        messages.error(request,'Passwords do not match!')
                else:
                    messages.error(request,'Invalid Email!')
            else:
                messages.error(request,'Invalid Phone Number1')

    return render(request,'tovo_website/other_page/sign-up.html')

def other_page_thank_you(request):
    return render(request,'tovo_website/other_page/thank-you.html')