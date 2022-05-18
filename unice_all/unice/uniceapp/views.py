from django.shortcuts import render

# Create your views here.

# Home views
default_layout = 'agency'
default_header = 'dark'
default_header_image = 'static/assets/images/logo/5.png'
header_logos = {
    "black_logo":'static/assets/images/logo/5.png',
    "white_logo": 'static/assets/images/logo/1.png',
    "pink_logo": 'static/assets/images/logo/3.png',
}

def index(request):
    context={"header_classes":"app1 nav-abs custom-scroll","header_image":header_logos["white_logo"]}
    return render(request,'home/index/index.html',context)

def agency(request):
    context = {"header_classes":"agency nav-fix custom-scroll","header_image":"static/assets/images/logo/9.png"}
    return render(request,'home/agency_layout/agency_layout.html',context)

def app_landing_1(request):
    context={"header_classes":"app1 nav-abs custom-scroll","header_image":header_logos["white_logo"]}
    return render(request,'home/index/index.html',context)

def app_landing_2(request):
    context={"header_classes":"app2 loding-header nav-abs custom-scroll","header_image":"static/assets/images/logo/1.png","header_animation":True}
    return render(request,'home/app_landing_layout/app_landing_layout.html',context)

def event(request):
    context={"header_classes":"event loding-header nav-abs custom-scroll nav-lg","header_image":header_logos["white_logo"],"body_classes":"event"}
    return render(request,'home/events_layout/events_layout.html',context)

def gym(request):
    context={'header_classes':"gym loding-header nav-abs custom-scroll nav-lg","header_image":header_logos["white_logo"]}
    return render(request,'home/gym_layout/gym_layout.html',context)

def music(request):
    context={"header_classes":"music loding-header header-fixed","header_image":header_logos["white_logo"],"body_classes":"bg-black music"}
    return render(request,'home/music_layout/music_layout.html',context)

def resume(request):
    context={"header_classes":"resume loding-header nav-abs custom-scroll","header_image":header_logos["black_logo"]}
    return render(request,'home/resume_layout/resume_layout.html',context)

def saas1(request):
    context={"header_classes":"saas1 header-fixed loding-header position-absolute  custom-scroll nav-lg","header_image":header_logos["pink_logo"]}
    return render(request,'home/sass_modern_layout/sass_modern_layout.html',context)

def saas2(request):
    context={"header_classes":"saas2 loding-header nav-abs custom-scroll","header_image":header_logos["white_logo"]}
    return render(request,'home/sass_layout/sass_layout.html',context)

def wedding(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'home/wedding_layout/wedding_layout.html',context)

def yoga(request):
    context ={}
    return render(request,'home/yoga_layout/yoga_layout.html',context)

def ecommerce(request):
    context={'header_classes':'ecommerce nav-fix','header_image':header_logos["black_logo"]}
    return render(request,'home/ecommerce_layout/ecommerce_layout.html',context)

def portfolio_metro(request):
    context={'header_classes':'dark loding-header custom-scroll nav-lg','body_classes':'agency','header_image':header_logos["black_logo"]}
    return render(request,'home/portfolio-metro/portfolio-metro.html',context)


# blog views

# blog grid views

def left_sidebar(request):
    breadcrumb = {"pageName":"blog with left-sidebar","parent":"Blog","child":"Blog Grid View","grandchild":"Left Sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-grid-view/blog-leftsidebar/blog-leftsidebar.html',context)

def right_sidebar(request):
    breadcrumb = {"pageName":"blog with right-sidebar","parent":"Blog","child":"Blog Grid View","grandchild":"right sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-grid-view/blog-rightsidebar/blog-rightsidebar.html',context)

def no_sidebar(request):
    breadcrumb = {"pageName":"blog with no-sidebar","parent":"Blog","child":"Blog Grid View","grandchild":"no sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-grid-view/blog-nosidebar/blog-nosidebar.html',context)

def full_width_left__sidebar(request):
    breadcrumb = {"pageName":"blog with full width left-sidebar","parent":"Blog","child":"Blog Grid View","grandchild":"full width left sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-grid-view/blog-full-width-left-sidebar/blog-full-width-left-sidebar.html',context)

def full_width_right_sidebar(request):
    breadcrumb = {"pageName":"blog with full width right-sidebar","parent":"Blog","child":"Blog Grid View","grandchild":"full width right sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-grid-view/blog-full-width-right-sidebar/blog-full-width-right-sidebar.html',context)

def full_width_no_sidebar(request):
    breadcrumb = {"pageName":"blog with full width no-sidebar","parent":"Blog","child":"Blog Grid View","grandchild":"full width no sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-grid-view/blog-full-width-nosidebar/blog-full-width-nosidebar.html',context)

    # blog list view

def list_view_left_sidebar(request):
    breadcrumb = {"pageName":"blog with left-sidebar","parent":"Blog","child":"blog list view","grandchild":"left sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-list-view/blog-list-leftsidebar/blog-list-leftsidebar.html',context)

def list_view_right_sidebar(request):
    breadcrumb = {"pageName":"blog with right-sidebar","parent":"Blog","child":"blog list view","grandchild":"right sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-list-view/blog-list-rightsidebar/blog-list-rightsidebar.html',context)

def list_view_no_sidebar(request):
    breadcrumb = {"pageName":"blog with no-sidebar","parent":"Blog","child":"blog list view","grandchild":"no sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-list-view/blog-list-nosidebar/blog-list-nosidebar.html',context)

    # blog list creative

def creative_left_sidebar(request):
    breadcrumb = {"pageName":"blog with left-sidebar","parent":"Blog","child":"blog list creative","grandchild":"left sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-list-creative/blog-creative-left-sidebar/blog-creative-left-sidebar.html',context)

def creative_right_sidebar(request):
    breadcrumb = {"pageName":"blog with right-sidebar","parent":"Blog","child":"blog list creative","grandchild":"right sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-list-creative/blog-creative-right-sidebar/blog-creative-right-sidebar.html',context)

def creative_no_sidebar(request):
    breadcrumb = {"pageName":"blog with no-sidebar","parent":"Blog","child":"blog list creative","grandchild":"no sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-list-creative/blog-creative-no-sidebar/blog-creative-no-sidebar.html',context)

    # blog mix layout

def list_mix_with_left_sidebar(request):
    breadcrumb = {"pageName":"list mix with left sidebar","parent":"Blog","child":"blog list creative","grandchild":"left sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-mix-layout/blog-list-mix-left-sidebar/blog-list-mix-left-sidebar.html',context)

def list_mix_with_right_sidebar(request):
    breadcrumb = {"pageName":"list mix with right sidebar","parent":"Blog","child":"blog list creative","grandchild":"right sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-mix-layout/blog-list-mix-right-sidebar/blog-list-mix-right-sidebar.html',context)

def list_mix_with_no_sidebar(request):
    breadcrumb = {"pageName":"list mix with no sidebar","parent":"Blog","child":"blog list creative","grandchild":"no sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-mix-layout/blog-list-mix-no-sidebar/blog-list-mix-no-sidebar.html',context)

def list_full_width_no_sidebar(request):
    breadcrumb = {"pageName":"list full width no sidebar","parent":"Blog","child":"blog list creative","grandchild":"no sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-mix-layout/blog-list-full-width-no-sidebar/blog-list-full-width-no-sidebar.html',context)

def grid_mix_with_right_sidebar(request):
    breadcrumb = {"pageName":"grid mix with right sidebar","parent":"Blog","child":"blog list creative","grandchild":"right sidebar"}
    context = {"header":"dark","layout":"agency"}
    return render(request,'blog/blog-mix-layout/blog-grid-mix-with-right-sidebar/blog-grid-mix-with-right-sidebar.html',context)

def grid_mix_with_no_sidebar(request):
    breadcrumb = {"pageName":"grid mix with no sidebar","parent":"Blog","child":"blog list creative","grandchild":"no sidebar"}
    context = {"header":"dark","layout":"agency"}
    return render(request,'blog/blog-mix-layout/blog-list-post-full-width-no-sidebar/blog-list-post-full-width-no-sidebar.html',context)

    # blog details

def details_left_sidebar(request):
    breadcrumb = {"pageName":"blog with left-sidebar","parent":"Blog","child":"Blog Detail","grandchild":"left sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-details/blog-detail-left-sidebar/blog-detail-left-sidebar.html',context)

def details_right_sidebar(request):
    breadcrumb = {"pageName":"BLOG WITH RIGHT-SIDEBAR","parent":"Blog","child":"Blog Detail","grandchild":"Right Sidebar"}
    context = {"breadcrumb":breadcrumb,"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-details/blog-detail/blog-detail.html',context)

def details_no_sidebar(request):
    breadcrumb = {"pageName":"blog with no-sidebar","parent":"Blog","child":"Blog Detail","grandchild":"no sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-details/blog-detail-no-sidebar/blog-detail-no-sidebar.html',context)

def details_gallery_layout(request):
    breadcrumb = {"pageName":"blog with gallery-layout","parent":"Blog","child":"Blog Detail","grandchild":"gallery layout"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-details/blog-detail-gallery/blog-detail-gallery.html',context)

def details_video_layout(request):
    breadcrumb = {"pageName":"blog with video-layout","parent":"Blog","child":"Blog Detail","grandchild":"video layout"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-details/blog-detail-video/blog-detail-video.html',context)

    # blog masonry

def masonry_2_columns(request):
    breadcrumb = {"pageName":"blog with 2-columns","parent":"Blog","child":"Blog Detail","grandchild":"2 columns"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-masonry/blog-masonry-left-side/blog-masonry-left-side.html',context)

def masonry_3_columns(request):
    breadcrumb = {"pageName":"blog with 3-columns","parent":"Blog","child":"Blog Detail","grandchild":"3 columns"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-masonry/blog-masonry-full-3-col/blog-masonry-full-3-col.html',context)

def masonry_4_columns(request):
    breadcrumb = {"pageName":"blog with 4-columns","parent":"Blog","child":"Blog Detail","grandchild":"4 columns"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-masonry/blog-masonry-full-4-col/blog-masonry-full-4-col.html',context)

def masonry_left_columns(request):
    breadcrumb = {"pageName":"blog with 2-columns","parent":"Blog","child":"Blog Detail","grandchild":"2 columns"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-masonry/blog-masonry-left-side/blog-masonry-left-side.html',context)

def masonry_right_sidebar(request):
    breadcrumb = {"pageName":"blog with right sidebar","parent":"Blog","child":"Blog Detail","grandchild":"right sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-masonry/blog-masonry-right-side/blog-masonry-right-side.html',context)

def masonry_no_sidebar(request):
    breadcrumb = {"pageName":"blog with no sidebar","parent":"Blog","child":"Blog Detail","grandchild":"no sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-masonry/blog-masonry-no-side/blog-masonry-no-side.html',context)

def masonry_grid_list_mix(request):
    breadcrumb = {"pageName":"blog with no side bar","parent":"Blog","child":"Blog Detail","grandchild":"list mix with no sidebar"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-masonry/blog-list-full-width-no-sidebar/blog-list-full-width-no-sidebar.html',context)

def masonry_grid_list_creative_mix(request):
    breadcrumb = {"pageName":"blog with no sidebar","parent":"Blog","child":"Blog Detail","grandchild":"list creative mix"}
    context = {"breadcrumb":breadcrumb,"header":"dark","layout":"agency"}
    return render(request,'blog/blog-masonry/blog-list-mix-no-sidebar/blog-list-mix-no-sidebar.html',context)


# pages views 

def pages_404(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'pages/404/404.html',context)

def faqs(request):
    context={"header":"dark","layout":"agency"}
    return render(request,'pages/faq/faq.html',context)

def collection(request):
    context={"header":"dark","layout":"agency"}
    return render(request,'pages/collection/collection.html',context)

def typography(request):
    context={"header":"dark","layout":"agency"}
    return render(request,'pages/typography/typography.html',context)

def maintenance(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'pages/maintenance/maintenance.html',context)

def about_us(request):
    context={"header":"dark","layout":"agency"} 
    return render(request,'pages/about-us/about-us.html',context)

    # team pages views
def team(request):
    context={"header":"dark","layout":"agency"} 
    return render(request,'pages/team/team/team.html',context)

def team_grid(request):
    context={"header":"dark","layout":"agency"} 
    return render(request,'pages/team/team-grid/team-grid.html',context)

def team_list(request):
    context={"header":"dark","layout":"agency"} 
    return render(request,'pages/team/team-list/team-list.html',context)

    # coming soon pages views

def coming_soon_1(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'pages/coming-soon/coming-soon/coming-soon.html',context)

def coming_soon_2(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'pages/coming-soon/coming-soon2/coming-soon2.html',context)

# elements views

def alerts(request):
    context = {"header":"dark","layout":"agency"}
    return render(request,'elements/alert/alert.html',context)

def accordion(request):
    context = {"header":"dark","layout":"agency"}
    return render(request,'elements/accordion/accordion.html',context)

def boxshadow(request):
    context = {"header":"dark","layout":"agency"}
    return render(request,'elements/boxshadow/boxshadow.html',context)

def buttons(request):
    context = {"header":"dark","layout":"agency"}
    return render(request,'elements/button/button.html',context)

def contact(request):
    context = {"header":"dark","layout":"agency"}
    return render(request,'elements/contact/contact.html',context)

def event_schedule(request):
    context = {"header":"dark","layout":"agency"}
    return render(request,'elements/event-schedule/event-schedule.html',context)

def gallery(request):
    context = {"header":"dark","layout":"agency"}
    return render(request,'elements/gallery/gallery.html',context)

def pricing(request):
    context = {"header":"dark","layout":""}
    return render(request,'elements/pricing/pricing.html',context)

def counter(request):
    context = {"header":"dark","layout":"+ "}
    return render(request,'elements/counter/counter.html',context)

def countdown(request):
    context = {"header":"dark","layout":"agency"}
    return render(request,'elements/countdown/countdown.html',context)

def progress_bar(request):
    context = {"header":"dark","layout":"agency"}
    return render(request,'elements/progress/progress.html',context)

def testimonial(request):
    context = {"header":"dark","layout":""}
    return render(request,'elements/testimonial/testimonial.html',context)

def video(request):
    context = {"header":"header-absolute","layout":"agency"}
    return render(request,'elements/video/video.html',context)

def service(request):
    context = {"header":"dark","layout":"agency"}
    return render(request,'elements/services/services.html',context)

def subscribe(request):
    context = {"header":"dark","layout":"agency"}
    return render(request,'elements/subscribe/subscribe.html',context)

# portfolio views

    # portolio views

def portfolio_2_column(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/portfolio/portfolio-basic-2-col/portfolio-basic-2-col.html',context)

def portfolio_3_column(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/portfolio/portfolio-basic-3-col/portfolio-basic-3-col.html',context)

def portfolio_4_column(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/portfolio/portfolio-basic-4-col/portfolio-basic-4-col.html',context)

def portfolio_3_column_with_title(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/portfolio/portfolio-title-3-col/portfolio-title-3-col.html',context)

def portfolio_4_column_with_title(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/portfolio/portfolio-title-4-col/portfolio-title-4-col.html',context)

def portfolio_with_parallex_effect(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/portfolio/portfolio-parallex/portfolio-parallex.html',context)

def portfolio_centered_slides(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/portfolio/portfolio-centered-slides/portfolio-centered-slides.html',context)

def portfolio_vertical_slider(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/portfolio/portfolio-full-screen-vertical/portfolio-full-screen-vertical.html',context)

def portfolio_4_slide_with_center_slider(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/portfolio/portfolio-multiple-carousel/portfolio-multiple-carousel.html',context)

def portfolio_title_2(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/portfolio/portfolio-title-2-col/portfolio-title-2-col.html',context)

    # porfolio details views

def portfolio_details_container_layout(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/portfolio-details/portfolio-detail4/portfolio-detail4.html',context)

def portfolio_details_full_width(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/portfolio-details/portfolio-detail3/portfolio-detail3.html',context)

def portfolio_details_with_big_breadcrumb(request):
    context = {"header":"position-absolute"}
    return render(request,'portfolio/portfolio-details/portfolio-detail2/portfolio-detail2.html',context)

def portfolio_details_details_wit_slider(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/portfolio-details/portfolio-detail/portfolio-detail.html',context)

def portfolio_details_video_portfolio(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/portfolio-details/portfolio-detail6/portfolio-detail6.html',context)

def portfolio_details_two_images_layout(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/portfolio-details/portfolio-detail5/portfolio-detail5.html',context)

def portfolio_details_left_side_images(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/portfolio-details/portfolio-detail7/portfolio-detail7.html',context)

    # trending layouts views

def trending_layout_1(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/trending-layouts/portfolio-creative-1/portfolio-creative-1.html',context)

def trending_layout_2(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/trending-layouts/portfolio-creative-2/portfolio-creative-2.html',context)

def trending_layout_3(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/trending-layouts/portfolio-creative-3/portfolio-creative-3.html',context)

def trending_layout_4(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/trending-layouts/portfolio-creative-4/portfolio-creative-4.html',context)

def trending_layout_5(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/trending-layouts/portfolio-modern-4-col/portfolio-modern-4-col.html',context)

def trending_layout_6(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/trending-layouts/portfolio-modern-3-col/portfolio-modern-3-col.html',context)

def trending_layout_7(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/trending-layouts/portfolio-modern-2-col/portfolio-modern-2-col.html',context)

    # masonry style views

def portfolio_masonry_2_column(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/masonry-style/portfolio-2-col/portfolio-2-col.html',context)

def portfolio_masonry_3_column(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/masonry-style/portfolio-3-col/portfolio-3-col.html',context)

def portfolio_masonry_4_column(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/masonry-style/portfolio-4-col/portfolio-4-col.html',context)

def portfolio_masonry_creative_layout_1(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/masonry-style/portfolio1/portfolio1.html',context)

def portfolio_masonry_creative_layout_2(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/masonry-style/portfolio2/portfolio2.html',context)

def portfolio_masonry_creative_layout_3(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'portfolio/masonry-style/portfolio3/portfolio3.html',context)

# shop views

    # shop categories views:

def shop_categories_left_sidebar(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-leftsidebar(4-grid)/category-page-leftsidebar(4-grid).html',context)

def shop_categories_two_sidebar(request):
    context = {"layout":default_layout,"header":"dark position-relative"}
    return render(request,'shop/shop-categories/category-page-leftsidebar(2-grid)/category-page-leftsidebar(2-grid).html',context)

def shop_categories_three_sidebar(request):
    context = {"layout":default_layout,"header":"dark position-relative"}
    return render(request,'shop/shop-categories/category-page-leftsidebar(3-grid)/category-page-leftsidebar(3-grid).html',context)

def shop_categories_six_sidebar(request):
    context = {"layout":default_layout,"header":"dark position-relative"}
    return render(request,'shop/shop-categories/category-page-leftsidebar(6-grid)/category-page-leftsidebar(6-grid).html',context)

def shop_categories_right_sidebar(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-rightsidebar(4-grid)/category-page-rightsidebar(4-grid).html',context)

def shop_categories_right_2_grid(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-rightsidebar(2-grid)/category-page-rightsidebar(2-grid).html',context)

def shop_categories_right_3_grid(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-rightsidebar(3-grid)/category-page-rightsidebar(3-grid).html',context)

def shop_categories_right_6_grid(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-rightsidebar(6-grid)/category-page-rightsidebar(6-grid).html',context)

def shop_categories_no_sidebar(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-nosidebar(4-grid)/category-page-nosidebar(4-grid).html',context)

def shop_categories_no_sidebar_2(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-nosidebar(2-grid)/category-page-nosidebar(2-grid).html',context)

def shop_categories_no_sidebar_3(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-nosidebar(3-grid)/category-page-nosidebar(3-grid).html',context)

def shop_categories_no_sidebar_6(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-nosidebar(6-grid)/category-page-nosidebar(6-grid).html',context)

def shop_categories_metro(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page(metro)/category-page(metro).html',context)

    # product pages views

def shop_product_no_sidebar(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(no-sidebar)/product-page(no-sidebar).html',context)

def shop_product_left_sidebar(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(left-sidebar)/product-page(left-sidebar).html',context)

def shop_product_right_sidebar(request):
    context = {"layout":default_layout,"header":"dark nav-lg"}
    return render(request,'shop/product-pages/product-page(right-sidebar)/product-page(right-sidebar).html',context)

def shop_product_3_grid(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(3-column)/product-page(3-column).html',context)

def shop_product_3_grid_left(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(3-col-left)/product-page(3-col-left).html',context)

def shop_product_3_grid_right(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(3-col-right)/product-page(3-col-right).html',context)

def shop_product_accordian(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(accordian)/product-page(accordian).html',context)

def shop_product_bundle(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(bundle)/product-page(bundle).html',context)

def shop_product_image_swatch(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(image-swatch)/product-page(image-swatch).html',context)

def shop_product_image_outside(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(image-outside)/product-page(image-outside).html',context)

def shop_product_image_sticky(request):
    context = {"layout":default_layout,"header":"dark nav-lg"}
    return render(request,'shop/product-pages/product-page(sticky)/product-page(sticky).html',context)

    # shop pages views

def shop_pages_cart(request):
    context = {"layout":default_layout,"header":"dark position-relative"}
    return render(request,'shop/shop-pages/cart/cart.html',context)

def shop_pages_checkout(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-pages/checkout/checkout.html',context)

def shop_pages_compare(request):
    context = {"layout":default_layout,"header":"dark position-relative"}
    return render(request,'shop/shop-pages/compare/compare.html',context)

def shop_pages_compare_2(request):
    context = {"layout":default_layout,"header":"dark position-relative"}
    return render(request,'shop/shop-pages/compare-2/compare-2.html',context)

def shop_pages_signup(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-pages/signup/signup.html',context)

def shop_pages_login(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-pages/login/login.html',context)

def shop_pages_wishlist(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-pages/wishlist/wishlist.html',context)

# features views

    # header options views

def features_light_header(request):
    context = {"header":"dark","layout":""}
    return render(request,'features/header-option/header-light/header-light.html',context)

def features_dark_header(request):
    context = {"header":"header-absolute","layout":""}
    return render(request,'features/header-option/header-dark/header-dark.html',context)

def features_glass_header(request):
    context = {"header":"dark","layout":""}
    return render(request,'features/header-option/header-transparent/header-transparent.html',context)

def features_logo_center(request):
    context = {"header":"yoga nav-abs header-rel","layout":""} 
    return render(request,'features/header-option/header-center-logo/header-center-logo.html',context)

def features_header_right_navigation(request):
    context = {"header":"app1 nav-abs ","layout":""}
    return render(request,'features/header-option/header-right-navigation/header-right-navigation.html',context)

    # breadcrumb option views

def features_classic_types(request):
    context = {"header":"dark","layout":"agency"}
    return render(request,'features/breadcrumb-option/breadcrumb/breadcrumb.html',context)

def features_breadcrumb_left(request):
    context = {"header":"dark","layout":""}
    return render(request,'features/breadcrumb-option/breadcrumb-left/breadcrumb-left.html',context)

def features_breadcrumb_right(request):
    context = {"header":"dark","layout":""}
    return render(request,'features/breadcrumb-option/breadcrumb-right/breadcrumb-right.html',context)

def features_breadcrumb_center(request):
    context = {"header":"dark","layout":""}
    return render(request,'features/breadcrumb-option/breadcrumb-center/breadcrumb-center.html',context)

def features_breadcrumb_dark(request):
    context = {"header":"header-absolute","layout":""}
    return render(request,'features/breadcrumb-option/breadcrumb-dark/breadcrumb-dark.html',context)

def features_parallex_background(request):
    context = {"header":"header-absolute","layout":""}
    return render(request,'features/breadcrumb-option/breadcrumb-parallex-background/breadcrumb-parallex-background.html',context)

def features_with_background(request):
    context = {"header":"header-absolute","layout":""}
    return render(request,'features/breadcrumb-option/breadcrumb-background/breadcrumb-background.html',context)

def features_gallery_background(request):
    context = {"header":"header-absolute","layout":""}
    return render(request,'features/breadcrumb-option/breadcrumb-gallery-background/breadcrumb-gallery-background.html',context)

def features_video_background(request):
    context = {"header":"header-absolute","layout":""}
    return render(request,'features/breadcrumb-option/breadcrumb-video-background/breadcrumb-video-background.html',context)

    # footer options views

def features_footer_default(request):
    context = {"header":"dark","layout":""}
    return render(request,'features/footer-options/footer-default/footer-default.html',context)

def features_footer_light(request):
    context = {"header":"dark","layout":""}
    return render(request,'features/footer-options/footer3-light/footer3-light.html',context)

def features_footer_dark(request):
    context = {"header":"dark","layout":""}
    return render(request,'features/footer-options/footer3-dark/footer3-dark.html',context)

def features_footer_dark_light(request):
    context = {"header":"dark","layout":""}
    return render(request,'features/footer-options/footer1-light/footer1-light.html',context)

def features_footer_dark_gradient(request):
    context = {"header":"dark","layout":""}
    return render(request,'features/footer-options/footer1-dark/footer1-dark.html',context)

def features_footer_creative(request):
    context = {"header":"dark","layout":""}
    return render(request,'features/footer-options/footer2-light/footer2-light.html',context)

    # gallery types views

def features_zoom_gallery(request):
    context = {"header":"dark","layout":"agency"}
    return render(request,'features/gallery-types/zoom-gallery/zoom-gallery.html',context)

def features_form_in_popup(request):
    context = {"header":"dark","layout":"agency"}
    return render(request,'features/gallery-types/popup-with-form/popup-with-form.html',context)

def features_modal_in_popup(request):
    context = {"header":"dark","layout":"agency"}
    return render(request,'features/gallery-types/popup-with-modal/popup-with-modal.html',context)

def features_youtube_in_popup(request):
    context = {"header":"dark","layout":"agency"}
    return render(request,'features/gallery-types/popup-with-youtube/popup-with-youtube.html',context)

def features_map_in_popup(request):
    context = {"header":"dark","layout":"agency"}
    return render(request,'features/gallery-types/popup-with-googlemap/popup-with-googlemap.html',context)