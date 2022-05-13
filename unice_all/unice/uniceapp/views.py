from django.shortcuts import render

# Create your views here.

# Home views

def agency(request):
    return render(request,'home/agency_layout.html')

def app_landing_1(request):
    return render(request,'home/index.html')

def app_landing_2(request):
    return render(request,'home/app_landing_layout.html')

def event(request):
    return render(request,'home/events_layout.html')

def gym(request):
    return render(request,'home/gym_layout.html')

def music(request):
    return render(request,'home/music_layout.html')

def resume(request):
    return render(request,'home/resume_layout.html')

def saas1(request):
    return render(request,'home/sass_modern_layout.html')

def saas2(request):
    return render(request,'home/sass_layout.html')

def wedding(request):
    return render(request,'home/wedding_layout.html')

def yoga(request):
    return render(request,'home/yoga_layout.html')

def ecommerce(request):
    return render(request,'home/ecommerce_layout.html')

def portfolio_metro(request):
    return render(request,'home/portfolio-metro.html')


# blog views

# blog grid views

def left_sidebar(request):
    return render(request,'blog/blog-grid-view/blog-leftsidebar.html')

def right_sidebar(request):
    return render(request,'blog/blog-grid-view/blog-rightsidebar.html')

def no_sidebar(request):
    return render(request,'blog/blog-grid-view/blog-nosidebar.html')

def full_width_left__sidebar(request):
    return render(request,'blog/blog-grid-view/blog-full-width-left-sidebar.html')

def full_width_right_sidebar(request):
    return render(request,'blog/blog-grid-view/blog-full-width-right-sidebar.html')

def full_width_no_sidebar(request):
    return render(request,'blog/blog-grid-view/blog-full-width-nosidebar.html')

    # blog list view

def list_view_left_sidebar(request):
    return render(request,'blog/blog-list-view/blog-list-leftsidebar.html')

def list_view_right_sidebar(request):
    return render(request,'blog/blog-list-view/blog-list-rightsidebar.html')

def list_view_no_sidebar(request):
    return render(request,'blog/blog-list-view/blog-list-rightsidebar.html')

    # blog list creative

def creative_left_sidebar(request):
    return render(request,'blog/blog-list-creative/blog-creative-left-sidebar.html')

def creative_right_sidebar(request):
    return render(request,'blog/blog-list-creative/blog-creative-right-sidebar.html')

def creative_no_sidebar(request):
    return render(request,'blog/blog-list-creative/blog-creative-no-sidebar.html')

    # blog mix layout

def list_mix_with_left_sidebar(request):
    return render(request,'blog/blog-mix-layout/blog-list-mix-left-sidebar.html')

def list_mix_with_right_sidebar(request):
    return render(request,'blog/blog-mix-layout/blog-list-mix-right-sidebar.html')

def list_mix_with_no_sidebar(request):
    return render(request,'blog/blog-mix-layout/blog-list-mix-no-sidebar.html')

def list_full_width_no_sidebar(request):
    return render(request,'blog/blog-mix-layout/blog-list-full-width-no-sidebar.html')

def grid_mix_with_no_sidebar(request):
    return render(request,'blog/blog-mix-layout/blog-list-post-full-width-no-sidebar.html')

    # blog details

def details_left_sidebar(request):
    return render(request,'blog/blog-details/blog-detail-left-sidebar.html')

def details_right_sidebar(request):
    return render(request,'blog/blog-details/blog-detail.html')

def details_no_sidebar(request):
    return render(request,'blog/blog-details/blog-detail-no-sidebar.html')

def details_gallery_layout(request):
    return render(request,'blog/blog-details/blog-detail-gallery.html')

def details_video_layout(request):
    return render(request,'blog/blog-details/blog-detail-video.html')

    # blog masonry