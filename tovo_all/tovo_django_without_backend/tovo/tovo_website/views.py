from django.shortcuts import render

# Create your views here.

def index(request):
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
    return render(request,'tovo_website/other_page/sign-in.html')

def other_page_sign_up(request):
    return render(request,'tovo_website/other_page/sign-up.html')

def other_page_thank_you(request):
    return render(request,'tovo_website/other_page/thank-you.html')