from django.urls import path
from . import views



urlpatterns = [
    
    # home paths

    path('',views.index,name='index'),
    path('agency',views.agency,name='agency'),
    path('app_landing_1',views.app_landing_1,name='app_landing_1'),
    path('app_landing_2',views.app_landing_2,name='app_landing_2'),
    path('event',views.event,name='event'),
    path('gym',views.gym,name='gym'),
    path('music',views.music,name='music'),
    path('resume',views.resume,name='resume'),
    path('saas1',views.saas1,name='saas1'),
    path('saas2',views.saas2,name='saas2'),
    path('wedding',views.wedding,name='wedding'),
    path('yoga',views.yoga,name='yoga'),
    path('ecommerce',views.ecommerce,name='ecommerce'),
    path('portfolio_metro',views.portfolio_metro,name='portfolio_metro'),

    # blog paths
        # blog grid paths

    path('left_sidebar',views.left_sidebar,name='left_sidebar'),
    path('right_sidebar',views.right_sidebar,name='right_sidebar'),
    path('no_sidebar',views.no_sidebar,name='no_sidebar'),
    path('full_width_left__sidebar',views.full_width_left__sidebar,name='full_width_left__sidebar'),
    path('full_width_right_sidebar',views.full_width_right_sidebar,name='full_width_right_sidebar'),
    path('full_width_no_sidebar',views.full_width_no_sidebar,name='full_width_no_sidebar'),
    
        # blog list paths

    path('list_view_left_sidebar',views.list_view_left_sidebar,name='list_view_left_sidebar'),
    path('list_view_right_sidebar',views.list_view_right_sidebar,name='list_view_right_sidebar'),
    path('list_view_no_sidebar',views.list_view_no_sidebar,name='list_view_no_sidebar'),

        # blog list creative paths

    path('creative_left_sidebar',views.creative_left_sidebar,name='creative_left_sidebar'),
    path('creative_right_sidebar',views.creative_right_sidebar,name='creative_right_sidebar'),
    path('creative_no_sidebar',views.creative_no_sidebar,name='creative_no_sidebar'),

        # blog mix layout paths

    path('list_mix_with_left_sidebar',views.list_mix_with_left_sidebar,name='list_mix_with_left_sidebar'),
    path('list_mix_with_right_sidebar',views.list_mix_with_right_sidebar,name='list_mix_with_right_sidebar'),
    path('list_mix_with_no_sidebar',views.list_mix_with_no_sidebar,name='list_mix_with_no_sidebar'),
    path('list_full_width_no_sidebar',views.list_full_width_no_sidebar,name='list_full_width_no_sidebar'),
    path('grid_mix_with_right_sidebar',views.grid_mix_with_right_sidebar,name='grid_mix_with_right_sidebar'),
    path('grid_mix_with_no_sidebar',views.grid_mix_with_no_sidebar,name='grid_mix_with_no_sidebar'),
    
        # blog details paths
    
    path('details_left_sidebar',views.details_left_sidebar,name='details_left_sidebar'),
    path('details_right_sidebar',views.details_right_sidebar,name='details_right_sidebar'),
    path('details_no_sidebar',views.details_no_sidebar,name='details_no_sidebar'),
    path('details_gallery_layout',views.details_gallery_layout,name='details_gallery_layout'),
    path('details_video_layout',views.details_video_layout,name='details_video_layout'),

        # blog masonry paths

    path('masonry_2_columns',views.masonry_2_columns,name='masonry_2_columns'),
    path('masonry_3_columns',views.masonry_3_columns,name='masonry_3_columns'),
    path('masonry_4_columns',views.masonry_4_columns,name='masonry_4_columns'),
    path('masonry_left_columns',views.masonry_left_columns,name='masonry_left_columns'),
    path('masonry_right_sidebar',views.masonry_right_sidebar,name='masonry_right_sidebar'),
    path('masonry_no_sidebar',views.masonry_no_sidebar,name='masonry_no_sidebar'),
    path('masonry_grid_list_mix',views.masonry_grid_list_mix,name='masonry_grid_list_mix'),
    path('masonry_grid_list_creative_mix',views.masonry_grid_list_creative_mix,name='masonry_grid_list_creative_mix'),

    # pages paths

    path('pages_404',views.pages_404,name='pages_404'),
    path('faqs',views.faqs,name='faqs'),
    path('collection',views.collection,name='collection'),
    path('typography',views.typography,name='typography'),
    path('maintenance',views.maintenance,name='maintenance'),
    path('about_us',views.about_us,name='about_us'),

        # team paths

    path('team',views.team,name='team'),
    path('team_grid',views.team_grid,name='team_grid'),
    path('team_list',views.team_list,name='team_list'),

        # coming soon paths

    path('coming_soon_1',views.coming_soon_1,name='coming_soon_1'),
    path('coming_soon_2',views.coming_soon_2,name='coming_soon_2'),

    # elements paths

    path('alerts',views.alerts,name='alerts'),
    path('accordion',views.accordion,name='accordion'),
    path('boxshadow',views.boxshadow,name='boxshadow'),
    path('buttons',views.buttons,name='buttons'),
    path('contact',views.contact,name='contact'),
    path('event_schedule',views.event_schedule,name='event_schedule'),
    path('gallery',views.gallery,name='gallery'),
    path('pricing',views.pricing,name='pricing'),
    path('counter',views.counter,name='counter'),
    path('countdown',views.countdown,name='countdown'),
    path('progress_bar',views.progress_bar,name='progress_bar'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('video',views.video,name='video'),
    path('service',views.service,name='service'),
    path('subscribe',views.subscribe,name='subscribe'),

    # portfolio paths

    path('portfolio_2_column',views.portfolio_2_column,name='portfolio_2_column'),
    path('portfolio_3_column',views.portfolio_3_column,name='portfolio_3_column'),
    path('portfolio_4_column',views.portfolio_4_column,name='portfolio_4_column'),
    path('portfolio_3_column_with_title',views.portfolio_3_column_with_title,name='portfolio_3_column_with_title'),
    path('portfolio_4_column_with_title',views.portfolio_4_column_with_title,name='portfolio_4_column_with_title'),
    path('portfolio_with_parallex_effect',views.portfolio_with_parallex_effect,name='portfolio_with_parallex_effect'),
    path('portfolio_centered_slides',views.portfolio_centered_slides,name='portfolio_centered_slides'),
    path('portfolio_vertical_slider',views.portfolio_vertical_slider,name='portfolio_vertical_slider'),
    path('portfolio_4_slide_with_center_slider',views.portfolio_4_slide_with_center_slider,name='portfolio_4_slide_with_center_slider'),
    path('portfolio_title_2',views.portfolio_title_2,name='portfolio_title_2'),

    # portfolio details paths

    path('portfolio_details_container_layout',views.portfolio_details_container_layout,name='portfolio_details_container_layout'),
    path('portfolio_details_full_width',views.portfolio_details_full_width,name='portfolio_details_full_width'),
    path('portfolio_details_with_big_breadcrumb',views.portfolio_details_with_big_breadcrumb,name='portfolio_details_with_big_breadcrumb'),
    path('portfolio_details_details_wit_slider',views.portfolio_details_details_wit_slider,name='portfolio_details_details_wit_slider'),
    path('portfolio_details_video_portfolio',views.portfolio_details_video_portfolio,name='portfolio_details_video_portfolio'),
    path('portfolio_details_two_images_layout',views.portfolio_details_two_images_layout,name='portfolio_details_two_images_layout'),
    path('portfolio_details_left_side_images',views.portfolio_details_left_side_images,name='portfolio_details_left_side_images'),

    # porfolio trending layouts paths

    path('trending_layout_1',views.trending_layout_1,name='trending_layout_1'),
    path('trending_layout_2',views.trending_layout_2,name='trending_layout_2'),
    path('trending_layout_3',views.trending_layout_3,name='trending_layout_3'),
    path('trending_layout_4',views.trending_layout_4,name='trending_layout_4'),
    path('trending_layout_5',views.trending_layout_5,name='trending_layout_5'),
    path('trending_layout_6',views.trending_layout_6,name='trending_layout_6'),
    path('trending_layout_7',views.trending_layout_7,name='trending_layout_7'),

    # masonry style paths

    path('portfolio_masonry_2_column',views.portfolio_masonry_2_column,name='portfolio_masonry_2_column'),
    path('portfolio_masonry_3_column',views.portfolio_masonry_3_column,name='portfolio_masonry_3_column'),
    path('portfolio_masonry_4_column',views.portfolio_masonry_4_column,name='portfolio_masonry_4_column'),
    path('portfolio_masonry_creative_layout_1',views.portfolio_masonry_creative_layout_1,name='portfolio_masonry_creative_layout_1'),
    path('portfolio_masonry_creative_layout_2',views.portfolio_masonry_creative_layout_2,name='portfolio_masonry_creative_layout_2'),
    path('portfolio_masonry_creative_layout_3',views.portfolio_masonry_creative_layout_3,name='portfolio_masonry_creative_layout_3'),

    # shop categories paths

    path('shop_categories_left_sidebar',views.shop_categories_left_sidebar,name='shop_categories_left_sidebar'),
    path('shop_categories_two_sidebar',views.shop_categories_two_sidebar,name='shop_categories_two_sidebar'),
    path('shop_categories_three_sidebar',views.shop_categories_three_sidebar,name='shop_categories_three_sidebar'),
    path('shop_categories_six_sidebar',views.shop_categories_six_sidebar,name='shop_categories_six_sidebar'),
    path('shop_categories_right_sidebar',views.shop_categories_right_sidebar,name='shop_categories_right_sidebar'),
    path('shop_categories_right_2_grid',views.shop_categories_right_2_grid,name='shop_categories_right_2_grid'),
    path('shop_categories_right_3_grid',views.shop_categories_right_3_grid,name='shop_categories_right_3_grid'),
    path('shop_categories_right_6_grid',views.shop_categories_right_6_grid,name='shop_categories_right_6_grid'),
    path('shop_categories_no_sidebar',views.shop_categories_no_sidebar,name='shop_categories_no_sidebar'),
    path('shop_categories_no_sidebar_2',views.shop_categories_no_sidebar_2,name='shop_categories_no_sidebar_2'),
    path('shop_categories_no_sidebar_3',views.shop_categories_no_sidebar_3,name='shop_categories_no_sidebar_3'),
    path('shop_categories_no_sidebar_6',views.shop_categories_no_sidebar_6,name='shop_categories_no_sidebar_6'),
    path('shop_categories_metro',views.shop_categories_metro,name='shop_categories_metro'),

    # product page paths

    path('shop_product_no_sidebar',views.shop_product_no_sidebar,name='shop_product_no_sidebar'),
    path('shop_product_left_sidebar',views.shop_product_left_sidebar,name='shop_product_left_sidebar'),
    path('shop_product_right_sidebar',views.shop_product_right_sidebar,name='shop_product_right_sidebar'),
    path('shop_product_3_grid',views.shop_product_3_grid,name='shop_product_3_grid'),
    path('shop_product_3_grid_left',views.shop_product_3_grid_left,name='shop_product_3_grid_left'),
    path('shop_product_3_grid_right',views.shop_product_3_grid_right,name='shop_product_3_grid_right'),
    path('shop_product_accordian',views.shop_product_accordian,name='shop_product_accordian'),
    path('shop_product_bundle',views.shop_product_bundle,name='shop_product_bundle'),
    path('shop_product_image_swatch',views.shop_product_image_swatch,name='shop_product_image_swatch'),
    path('shop_product_image_outside',views.shop_product_image_outside,name='shop_product_image_outside'),
    path('shop_product_image_sticky',views.shop_product_image_sticky,name='shop_product_image_sticky'),

    # shop pages paths

    path('shop_pages_cart',views.shop_pages_cart,name='shop_pages_cart'),
    path('shop_pages_checkout',views.shop_pages_checkout,name='shop_pages_checkout'),
    path('shop_pages_compare',views.shop_pages_compare,name='shop_pages_compare'),
    path('shop_pages_compare_2',views.shop_pages_compare_2,name='shop_pages_compare_2'),
    path('shop_pages_signup',views.shop_pages_signup,name='shop_pages_signup'),
    path('shop_pages_login',views.shop_pages_login,name='shop_pages_login'),
    path('shop_pages_wishlist',views.shop_pages_wishlist,name='shop_pages_wishlist'),

    # header options paths

    path('features_light_header',views.features_light_header,name='features_light_header'),
    path('features_dark_header',views.features_dark_header,name='features_dark_header'),
    path('features_glass_header',views.features_glass_header,name='features_glass_header'),
    path('features_logo_center',views.features_logo_center,name='features_logo_center'),
    path('features_header_right_navigation',views.features_header_right_navigation,name='features_header_right_navigation'),

    # bradcrumb paths

    path('features_classic_types',views.features_classic_types,name='features_classic_types'),
    path('features_breadcrumb_left',views.features_breadcrumb_left,name='features_breadcrumb_left'),
    path('features_breadcrumb_right',views.features_breadcrumb_right,name='features_breadcrumb_right'),
    path('features_breadcrumb_center',views.features_breadcrumb_center,name='features_breadcrumb_center'),
    path('features_breadcrumb_dark',views.features_breadcrumb_dark,name='features_breadcrumb_dark'),
    path('features_parallex_background',views.features_parallex_background,name='features_parallex_background'),
    path('features_with_background',views.features_with_background,name='features_with_background'),
    path('features_gallery_background',views.features_gallery_background,name='features_gallery_background'),
    path('features_video_background',views.features_video_background,name='features_video_background'),

    # footer options paths

    path('features_footer_default',views.features_footer_default,name='features_footer_default'),
    path('features_footer_light',views.features_footer_light,name='features_footer_light'),
    path('features_footer_dark',views.features_footer_dark,name='features_footer_dark'),
    path('features_footer_dark_light',views.features_footer_dark_light,name='features_footer_dark_light'),
    path('features_footer_dark_gradient',views.features_footer_dark_gradient,name='features_footer_dark_gradient'),
    path('features_footer_creative',views.features_footer_creative,name='features_footer_creative'),

    # gallery types paths

    path('features_zoom_gallery',views.features_zoom_gallery,name='features_zoom_gallery'),
    path('features_form_in_popup',views.features_form_in_popup,name='features_form_in_popup'),
    path('features_modal_in_popup',views.features_modal_in_popup,name='features_modal_in_popup'),
    path('features_youtube_in_popup',views.features_youtube_in_popup,name='features_youtube_in_popup'),
    path('features_map_in_popup',views.features_map_in_popup,name='features_map_in_popup'),

    # documentation path

    path('documentation',views.documentation,name='documentation'),

]
