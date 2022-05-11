from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import re
# Create your views here.

def index(request):

    #subscribe
    if 'btn_subscribe' in request.POST:
        email = request.POST['EMAIL']
        if email == '':
            messages.error(request,'Please enter you email to continue!')
        else:
            email_is_valid = re.search("^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$", email)
            if email_is_valid:
                subscribe = subscription.objects.filter(email=email)
                if subscribe.exists():
                    messages.info(request,'You are already subscribed!')
                    return redirect('index')
                else:
                    subscribe = subscription(email = email)
                    messages.success(request,'Subscribed successfully!')
                    subscribe.save()
            else:
                messages.error(request,'Enter a valid email address!')

    #contact us

    if 'btn_contactus' in request.POST:
        
        username = request.POST['username']
        email = request.POST['email']
        message = request.POST['message']

        if username == '' or email == '' or message == '':
            messages.error(request,'Some fields are empty! Please fill all the fields and try again!')
            return redirect('index')
        else:
            email_is_valid = re.search("^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$", email)
            if email_is_valid:
                user_message = contactUs(name=username,email = email,message=message)
                user_message.save()
                messages.success(request,'Your message have been received!')
                return redirect('index')

            else:
                messages.error(request,'Please enter a valid email!')
        

    return render(request,'chatloopapp/index.html')


#blog pages views

def blog_details_with_leftsidebar(request):
    return render(request,'chatloopapp/blog/blog-details-with-leftsidebar.html')

def blog_details_with_rightsidebar(request):
    return render(request,'chatloopapp/blog/blog-details-with-rightsidebar.html')

def blog_details(request):
    return render(request,'chatloopapp/blog/blog-details.html')

def blog(request):
    return render(request,'chatloopapp/blog/blog.html')

def blogs_leftside(request):
    return render(request,'chatloopapp/blog/blogs-leftside.html')

def blogs_rightside(request):
    return render(request,'chatloopapp/blog/blogs-rightside.html')


# views for other pages

def other_page_404(request):
    return render(request,'chatloopapp/other_page/404.html')

def other_page_coming_soon(request):
    return render(request,'chatloopapp/other_page/coming-soon.html')

def other_page_download(request):
    return render(request,'chatloopapp/other_page/download.html')

def other_page_faq(request):
    return render(request,'chatloopapp/other_page/faq.html')

def other_page_forgot_pass(request):
    return render(request,'chatloopapp/other_page/forgot-pass.html')

def other_page_request(request):
    return render(request,'chatloopapp/other_page/request.html')

def other_page_review(request):
    return render(request,'chatloopapp/other_page/review.html')

def other_page_sign_in(request):

    if 'btn_login' in request.POST:
        loginEmail = request.POST['loginEmail']
        loginPassword = request.POST['loginPassword']

        if loginEmail == '' or loginPassword == '':
            messages.error(request,'Some fields are empty! Please fill all the fields and try again!')
            return redirect('other_page_sign_in')
        else:
            email_is_valid = re.search("^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$", loginEmail)
            if email_is_valid:

                # autherticate the user 
                # log the user in and redirect to the other page
                # remove pass from below
                pass
            else:
                messages.error(request,'Please enter a valid Email!')
                return redirect('other_page_sign_in')
    return render(request,'chatloopapp/other_page/sign-in.html')

def other_page_sign_up(request):

    if 'btn_signUp' in request.POST:
        signUpName = request.POST['signUpName']
        signUpPhone = request.POST['signUpPhone']
        signUpEmail = request.POST['signUpEmail']
        signUpPassword = request.POST['signUpPassword']

        if signUpName == '' or signUpPhone == '' or signUpEmail == '' or signUpPassword == '':
            messages.error(request,'Some fields are empty! Please fill all the fields and try again!')
            return redirect('other_page_sign_up')

        else:
            phone_number_is_valid = re.search("^(\+\d{1,3})?,?\s?\d{8,13}", signUpPhone)
            if phone_number_is_valid:
                email_is_valid = re.search("^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$", signUpEmail)
                if email_is_valid:
                    
                    # check if re-password has been added or not if yes than add validation for it as well.
                    # enter value into database
                    # remove pass from below
                    # return redirect('other_page_thank_you')
                    pass

                else:
                    messages.error(request,'Please enter a valid email and try again!')
                    return redirect('other_page_sign_up')
            else:
                messages.error(request,'Invalid phone Number! Please enter a valid number and try again.')
                return redirect('other_page_sign_up')

    return render(request,'chatloopapp/other_page/sign-up.html')

def other_page_thank_you(request):
    return render(request,'chatloopapp/other_page/thank-you.html')