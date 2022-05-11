from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),

    #paths blog pages
    path('blog',views.blog,name='blog'),
    path('blog_details',views.blog_details,name='blog_details'),
    path('blogs_leftside',views.blogs_leftside,name='blogs_leftside'),
    path('blogs_rightside',views.blogs_rightside,name='blogs_rightside'),
    path('blog_details_with_leftsidebar',views.blog_details_with_leftsidebar,name='blog_details_with_leftsidebar'),
    path('blog_details_with_rightsidebar',views.blog_details_with_rightsidebar,name='blog_details_with_rightsidebar'),

    # paths for other pages

    path('other_page_404',views.other_page_404,name='other_page_404'),
    path('other_page_coming_soon',views.other_page_coming_soon,name='other_page_coming_soon'),
    path('other_page_download',views.other_page_download,name='other_page_download'),
    path('other_page_faq',views.other_page_faq,name='other_page_faq'),
    path('other_page_forgot_pass',views.other_page_forgot_pass,name='other_page_forgot_pass'),
    path('other_page_request',views.other_page_request,name='other_page_request'),
    path('other_page_review',views.other_page_review,name='other_page_review'),
    path('other_page_sign_in',views.other_page_sign_in,name='other_page_sign_in'),
    path('other_page_sign_up',views.other_page_sign_up,name='other_page_sign_up'),
    path('other_page_thank_you',views.other_page_thank_you,name='other_page_thank_you'),

]
