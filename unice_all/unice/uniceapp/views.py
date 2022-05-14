from django.shortcuts import render

# Create your views here.

# Home views

def index(request):
    return render(request,'home/index.html')

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
    return render(request,'blog/blog-list-view/blog-list-nosidebar.html')

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

def grid_mix_with_right_sidebar(request):
    return render(request,'blog/blog-mix-layout/blog-grid-mix-with-right-sidebar.html')

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

def masonry_2_columns(request):
    return render(request,'blog/blog-masonry/blog-masonry-left-side.html')

def masonry_3_columns(request):
    return render(request,'blog/blog-masonry/blog-masonry-full-3-col.html')

def masonry_4_columns(request):
    return render(request,'blog/blog-masonry/blog-masonry-full-4-col.html')

def masonry_left_columns(request):
    return render(request,'blog/blog-masonry/blog-masonry-left-side.html')

def masonry_right_sidebar(request):
    return render(request,'blog/blog-masonry/blog-masonry-right-side.html')

def masonry_no_sidebar(request):
    return render(request,'blog/blog-masonry/blog-masonry-no-side.html')

def masonry_grid_list_mix(request):
    return render(request,'blog/blog-masonry/blog-list-full-width-no-sidebar.html')

def masonry_grid_list_creative_mix(request):
    return render(request,'blog/blog-masonry/blog-list-mix-no-sidebar.html')


# pages views 

def pages_404(request):
    return render(request,'pages/404.html')

def faqs(request):
    return render(request,'pages/faq.html')

def collection(request):
    return render(request,'pages/collection.html')

def typography(request):
    return render(request,'pages/typography.html')

def maintenance(request):
    return render(request,'pages/maintenance.html')

def about_us(request):
    return render(request,'pages/about-us.html')

    # team pages views
def team(request):
    return render(request,'pages/team.html')

def team_grid(request):
    return render(request,'pages/team-grid.html')

def team_list(request):
    return render(request,'pages/team-list.html')

    # coming soon pages views

def coming_soon_1(request):
    return render(request,'pages/coming-soon.html')

def coming_soon_2(request):
    return render(request,'pages/coming-soon2.html')

# elements views

def alerts(request):
    return render(request,'elements/alert.html')

def accordion(request):
    return render(request,'elements/accordion.html')

def boxshadow(request):
    return render(request,'elements/boxshadow.html')

def buttons(request):
    return render(request,'elements/button.html')

def contact(request):
    return render(request,'elements/contact.html')

def event_schedule(request):
    return render(request,'elements/event-schedule.html')

def gallery(request):
    return render(request,'elements/gallery.html')

def pricing(request):
    return render(request,'elements/pricing.html')

def counter(request):
    return render(request,'elements/counter.html')

def countdown(request):
    return render(request,'elements/countdown.html')

def progress_bar(request):
    return render(request,'elements/progress.html')

def testimonial(request):
    return render(request,'elements/testimonial.html')

def video(request):
    return render(request,'elements/video.html')

def service(request):
    return render(request,'elements/services.html')

def subscribe(request):
    return render(request,'elements/subscribe.html')

# portfolio views

    # portolio views

def portfolio_2_column(request):
    return render(request,'portfolio/portfolio/portfolio-basic-2-col.html')

def portfolio_3_column(request):
    return render(request,'portfolio/portfolio/portfolio-basic-3-col.html')

def portfolio_4_column(request):
    return render(request,'portfolio/portfolio/portfolio-basic-4-col.html')

def portfolio_3_column_with_title(request):
    return render(request,'portfolio/portfolio/portfolio-title-3-col.html')

def portfolio_4_column_with_title(request):
    return render(request,'portfolio/portfolio/portfolio-title-4-col.html')

def portfolio_with_parallex_effect(request):
    return render(request,'portfolio/portfolio/portfolio-parallex.html')

def portfolio_centered_slides(request):
    return render(request,'portfolio/portfolio/portfolio-centered-slides.html')

def portfolio_vertical_slider(request):
    return render(request,'portfolio/portfolio/portfolio-full-screen-vertical.html')

def portfolio_4_slide_with_center_slider(request):
    return render(request,'portfolio/portfolio/portfolio-multiple-carousel.html')

def portfolio_title_2(request):
    return render(request,'portfolio/portfolio/portfolio-title-2-col.html')

    # porfolio details views

def portfolio_details_container_layout(request):
    return render(request,'portfolio/portfolio-details/portfolio-detail4.html')

def portfolio_details_full_width(request):
    return render(request,'portfolio/portfolio-details/portfolio-detail3.html')

def portfolio_details_with_big_breadcrumb(request):
    return render(request,'portfolio/portfolio-details/portfolio-detail2.html')

def portfolio_details_details_wit_slider(request):
    return render(request,'portfolio/portfolio-details/portfolio-detail.html')

def portfolio_details_video_portfolio(request):
    return render(request,'portfolio/portfolio-details/portfolio-details6.html')

def portfolio_details_two_images_layout(request):
    return render(request,'portfolio/portfolio-details/portfolio-detail5.html')

def portfolio_details_left_side_images(request):
    return render(request,'portfolio/portfolio-details/portfolio-detail7.html')

    # trending layouts views

def trending_layout_1(request):
    return render(request,'portfolio/trending-layouts/portfolio-creative-1.html')

def trending_layout_2(request):
    return render(request,'portfolio/trending-layouts/portfolio-creative-2.html')

def trending_layout_3(request):
    return render(request,'portfolio/trending-layouts/portfolio-creative-3.html')

def trending_layout_4(request):
    return render(request,'portfolio/trending-layouts/portfolio-creative-4.html')

def trending_layout_5(request):
    return render(request,'portfolio/trending-layouts/portfolio-modern-4-col.html')

def trending_layout_6(request):
    return render(request,'portfolio/trending-layouts/portfolio-modern-3-col.html')

def trending_layout_7(request):
    return render(request,'portfolio/trending-layouts/portfolio-modern-2-col.html')

    # masonry style views

def portfolio_masonry_2_column(request):
    return render(request,'portfolio/masonry-style/portfolio-2-col.html')

def portfolio_masonry_3_column(request):
    return render(request,'portfolio/masonry-style/portfolio-3-col.html')

def portfolio_masonry_4_column(request):
    return render(request,'portfolio/masonry-style/portfolio-4-col.html')

def portfolio_masonry_creative_layout_1(request):
    return render(request,'portfolio/masonry-style/portfolio1.html')

def portfolio_masonry_creative_layout_2(request):
    return render(request,'portfolio/masonry-style/portfolio2.html')

def portfolio_masonry_creative_layout_3(request):
    return render(request,'portfolio/masonry-style/portfolio3.html')

# shop views

    # shop categories views:

def shop_categories_left_sidebar(request):
    return render(request,'shop/shop-categories/category-page-leftsidebar(4-grid).html')

def shop_categories_two_sidebar(request):
    return render(request,'shop/shop-categories/category-page-leftsidebar(2-grid).html')

def shop_categories_three_sidebar(request):
    return render(request,'shop/shop-categories/category-page-leftsidebar(3-grid).html')

def shop_categories_six_sidebar(request):
    return render(request,'shop/shop-categories/category-page-leftsidebar(6-grid).html')

def shop_categories_right_sidebar(request):
    return render(request,'shop/shop-categories/category-page-rightsidebar(4-grid).html')

def shop_categories_right_2_grid(request):
    return render(request,'shop/shop-categories/category-page-rightsidebar(2-grid).html')

def shop_categories_right_3_grid(request):
    return render(request,'shop/shop-categories/category-page-rightsidebar(3-grid).html')

def shop_categories_right_6_grid(request):
    return render(request,'shop/shop-categories/category-page-rightsidebar(6-grid).html')

def shop_categories_no_sidebar(request):
    return render(request,'shop/shop-categories/category-page-nosidebar(4-grid).html')

def shop_categories_no_sidebar_2(request):
    return render(request,'shop/shop-categories/category-page-nosidebar(2-grid).html')

def shop_categories_no_sidebar_3(request):
    return render(request,'shop/shop-categories/category-page-nosidebar(3-grid).html')

def shop_categories_no_sidebar_6(request):
    return render(request,'shop/shop-categories/category-page-nosidebar(6-grid).html')

def shop_categories_metro(request):
    return render(request,'shop/shop-categories/category-page(metro).html')

    # product pages views

def shop_product_no_sidebar(request):
    return render(request,'shop/product-pages/product-page(no-sidebar).html')

def shop_product_left_sidebar(request):
    return render(request,'shop/product-pages/product-page(left-sidebar).html')

def shop_product_right_sidebar(request):
    return render(request,'shop/product-pages/product-page(right-sidebar).html')

def shop_product_3_grid(request):
    return render(request,'shop/product-pages/product-page(3-column).html')

def shop_product_3_grid_left(request):
    return render(request,'shop/product-pages/product-page(3-col-left).html')

def shop_product_3_grid_right(request):
    return render(request,'shop/product-pages/product-page(3-col-right).html')

def shop_product_accordian(request):
    return render(request,'shop/product-pages/product-page(accordian).html')

def shop_product_bundle(request):
    return render(request,'shop/product-pages/product-page(bundle).html')

def shop_product_image_swatch(request):
    return render(request,'shop/product-pages/product-page(image-swatch).html')

def shop_product_image_outside(request):
    return render(request,'shop/product-pages/product-page(image-outside).html')

def shop_product_image_sticky(request):
    return render(request,'shop/product-pages/product-page(sticky).html')

    # shop pages views

def shop_pages_cart(request):
    return render(request,'shop/shop-pages/cart.html')

def shop_pages_checkout(request):
    return render(request,'shop/shop-pages/checkout.html')

def shop_pages_compare(request):
    return render(request,'shop/shop-pages/compare.html')

def shop_pages_compare_2(request):
    return render(request,'shop/shop-pages/compare-2.html')

def shop_pages_signup(request):
    return render(request,'shop/shop-pages/signup.html')

def shop_pages_login(request):
    return render(request,'shop/shop-pages/login.html')

def shop_pages_wishlist(request):
    return render(request,'shop/shop-pages/wishlist.html')

# features views

    # header options views

def features_light_header(request):
    return render(request,'features/header-option/header-light.html')

def features_dark_header(request):
    return render(request,'features/header-option/header-dark.html')

def features_glass_header(request):
    return render(request,'features/header-option/header-transparent.html')

def features_logo_center(request):
    return render(request,'features/header-option/header-center-logo.html')

def features_header_right_navigation(request):
    return render(request,'features/header-option/header-right-navigation.html')

    # breadcrumb option views

def features_classic_types(request):
    return render(request,'features/breadcrumb-option/breadcrumb.html')

def features_breadcrumb_left(request):
    return render(request,'features/breadcrumb-option/breadcrumb-left.html')

def features_breadcrumb_right(request):
    return render(request,'features/breadcrumb-option/breadcrumb-right.html')

def features_breadcrumb_center(request):
    return render(request,'features/breadcrumb-option/breadcrumb-center.html')

def features_breadcrumb_dark(request):
    return render(request,'features/breadcrumb-option/breadcrumb-dark.html')

def features_parallex_background(request):
    return render(request,'features/breadcrumb-option/breadcrumb-parallex-background.html')

def features_with_background(request):
    return render(request,'features/breadcrumb-option/breadcrumb-background.html')

def features_gallery_background(request):
    return render(request,'features/breadcrumb-option/breadcrumb-gallery-background.html')

def features_video_background(request):
    return render(request,'features/breadcrumb-option/breadcrumb-video-background.html')

    # footer options views

def features_footer_default(request):
    return render(request,'features/footer-options/footer-default.html')

def features_footer_light(request):
    return render(request,'features/footer-options/footer3-light.html')

def features_footer_dark(request):
    return render(request,'features/footer-options/footer3-dark.html')

def features_footer_dark_light(request):
    return render(request,'features/footer-options/footer1-light.html')

def features_footer_dark_gradient(request):
    return render(request,'features/footer-options/footer1-dark.html')

def features_footer_creative(request):
    return render(request,'features/footer-options/footer2-light.html')

    # gallery types views

def features_zoom_gallery(request):
    return render(request,'features/gallery-types/zoom-gallery.html')

def features_form_in_popup(request):
    return render(request,'features/gallery-types/popup-with-form.html')

def features_modal_in_popup(request):
    return render(request,'features/gallery-types/popup-with-modal.html')

def features_youtube_in_popup(request):
    return render(request,'features/gallery-types/popup-with-youtube.html')

def features_map_in_popup(request):
    return render(request,'features/gallery-types/popup-with-googlemap.html')