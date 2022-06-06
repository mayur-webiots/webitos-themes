import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _1c6e12bf = () => interopDefault(import('../pages/blog/blog-detail.vue' /* webpackChunkName: "pages/blog/blog-detail" */))
const _325c82f7 = () => interopDefault(import('../pages/blog/blog-leftsidebar.vue' /* webpackChunkName: "pages/blog/blog-leftsidebar" */))
const _12092106 = () => interopDefault(import('../pages/blog/blog-nosidebar.vue' /* webpackChunkName: "pages/blog/blog-nosidebar" */))
const _4a92f7a4 = () => interopDefault(import('../pages/blog/blog-rightsidebar.vue' /* webpackChunkName: "pages/blog/blog-rightsidebar" */))
const _b57c570e = () => interopDefault(import('../pages/collection/full-width.vue' /* webpackChunkName: "pages/collection/full-width" */))
const _3dce61da = () => interopDefault(import('../pages/collection/list-view.vue' /* webpackChunkName: "pages/collection/list-view" */))
const _1a1f5eb8 = () => interopDefault(import('../pages/collection/metro.vue' /* webpackChunkName: "pages/collection/metro" */))
const _61991ec1 = () => interopDefault(import('../pages/collection/no-sidebar.vue' /* webpackChunkName: "pages/collection/no-sidebar" */))
const _939c136c = () => interopDefault(import('../pages/collection/right-sidebar.vue' /* webpackChunkName: "pages/collection/right-sidebar" */))
const _5111149a = () => interopDefault(import('../pages/collection/sidebar-popup.vue' /* webpackChunkName: "pages/collection/sidebar-popup" */))
const _082ecafc = () => interopDefault(import('../pages/collection/six-grid.vue' /* webpackChunkName: "pages/collection/six-grid" */))
const _d67739f4 = () => interopDefault(import('../pages/collection/three-grid.vue' /* webpackChunkName: "pages/collection/three-grid" */))
const _4cac33f0 = () => interopDefault(import('../pages/page/404.vue' /* webpackChunkName: "pages/page/404" */))
const _1ac65fdd = () => interopDefault(import('../pages/page/about.vue' /* webpackChunkName: "pages/page/about" */))
const _02452cfe = () => interopDefault(import('../pages/page/collection.vue' /* webpackChunkName: "pages/page/collection" */))
const _1fe99217 = () => interopDefault(import('../pages/page/coming-soon.vue' /* webpackChunkName: "pages/page/coming-soon" */))
const _f4caee34 = () => interopDefault(import('../pages/page/faq.vue' /* webpackChunkName: "pages/page/faq" */))
const _00aa6568 = () => interopDefault(import('../pages/page/lookbook.vue' /* webpackChunkName: "pages/page/lookbook" */))
const _2a66a558 = () => interopDefault(import('../pages/page/order-success.vue' /* webpackChunkName: "pages/page/order-success" */))
const _7a5c2cb8 = () => interopDefault(import('../pages/page/review.vue' /* webpackChunkName: "pages/page/review" */))
const _7df019f0 = () => interopDefault(import('../pages/page/search.vue' /* webpackChunkName: "pages/page/search" */))
const _7a66430f = () => interopDefault(import('../pages/page/typography.vue' /* webpackChunkName: "pages/page/typography" */))
const _b986e7d8 = () => interopDefault(import('../pages/product/bundle-product.vue' /* webpackChunkName: "pages/product/bundle-product" */))
const _316bb138 = () => interopDefault(import('../pages/product/four-image.vue' /* webpackChunkName: "pages/product/four-image" */))
const _6a687a47 = () => interopDefault(import('../pages/shop/bags/index.vue' /* webpackChunkName: "pages/shop/bags/index" */))
const _76a8c7d8 = () => interopDefault(import('../pages/shop/beauty/index.vue' /* webpackChunkName: "pages/shop/beauty/index" */))
const _6c7c0756 = () => interopDefault(import('../pages/shop/electronics-1/index.vue' /* webpackChunkName: "pages/shop/electronics-1/index" */))
const _e9bb289c = () => interopDefault(import('../pages/shop/fashion/index.vue' /* webpackChunkName: "pages/shop/fashion/index" */))
const _2c8ec552 = () => interopDefault(import('../pages/shop/fashion-2/index.vue' /* webpackChunkName: "pages/shop/fashion-2/index" */))
const _7e9d5018 = () => interopDefault(import('../pages/shop/fashion-3/index.vue' /* webpackChunkName: "pages/shop/fashion-3/index" */))
const _236da6f7 = () => interopDefault(import('../pages/shop/flower/index.vue' /* webpackChunkName: "pages/shop/flower/index" */))
const _2d8a2ca8 = () => interopDefault(import('../pages/shop/furniture/index.vue' /* webpackChunkName: "pages/shop/furniture/index" */))
const _13293f75 = () => interopDefault(import('../pages/shop/gym/index.vue' /* webpackChunkName: "pages/shop/gym/index" */))
const _344858bd = () => interopDefault(import('../pages/shop/jewellery/index.vue' /* webpackChunkName: "pages/shop/jewellery/index" */))
const _8f90566e = () => interopDefault(import('../pages/shop/kids/index.vue' /* webpackChunkName: "pages/shop/kids/index" */))
const _3ac9fe60 = () => interopDefault(import('../pages/shop/pets/index.vue' /* webpackChunkName: "pages/shop/pets/index" */))
const _1bdbc0a2 = () => interopDefault(import('../pages/shop/shoes/index.vue' /* webpackChunkName: "pages/shop/shoes/index" */))
const _4eb99856 = () => interopDefault(import('../pages/shop/tools/index.vue' /* webpackChunkName: "pages/shop/tools/index" */))
const _4d00cfce = () => interopDefault(import('../pages/shop/vegetables/index.vue' /* webpackChunkName: "pages/shop/vegetables/index" */))
const _ecdde46e = () => interopDefault(import('../pages/shop/watch/index.vue' /* webpackChunkName: "pages/shop/watch/index" */))
const _5533b3ac = () => interopDefault(import('../pages/blog/widgets/blog-list.vue' /* webpackChunkName: "pages/blog/widgets/blog-list" */))
const _1b59b684 = () => interopDefault(import('../pages/blog/widgets/blog-sidebar.vue' /* webpackChunkName: "pages/blog/widgets/blog-sidebar" */))
const _d40d5fbc = () => interopDefault(import('../pages/page/account/cart.vue' /* webpackChunkName: "pages/page/account/cart" */))
const _7bf15a48 = () => interopDefault(import('../pages/page/account/checkout.vue' /* webpackChunkName: "pages/page/account/checkout" */))
const _1413040e = () => interopDefault(import('../pages/page/account/contact.vue' /* webpackChunkName: "pages/page/account/contact" */))
const _4bdc7302 = () => interopDefault(import('../pages/page/account/dashboard.vue' /* webpackChunkName: "pages/page/account/dashboard" */))
const _1f1c8a2e = () => interopDefault(import('../pages/page/account/forget-password.vue' /* webpackChunkName: "pages/page/account/forget-password" */))
const _8eb73f52 = () => interopDefault(import('../pages/page/account/login.vue' /* webpackChunkName: "pages/page/account/login" */))
const _6af4c6ed = () => interopDefault(import('../pages/page/account/login-firebase.vue' /* webpackChunkName: "pages/page/account/login-firebase" */))
const _1c3a7d17 = () => interopDefault(import('../pages/page/account/profile.vue' /* webpackChunkName: "pages/page/account/profile" */))
const _820f75b6 = () => interopDefault(import('../pages/page/account/register.vue' /* webpackChunkName: "pages/page/account/register" */))
const _13236b47 = () => interopDefault(import('../pages/page/account/wishlist.vue' /* webpackChunkName: "pages/page/account/wishlist" */))
const _b8d95822 = () => interopDefault(import('../pages/page/compare/compare-1.vue' /* webpackChunkName: "pages/page/compare/compare-1" */))
const _b8bd2920 = () => interopDefault(import('../pages/page/compare/compare-2.vue' /* webpackChunkName: "pages/page/compare/compare-2" */))
const _63051f7f = () => interopDefault(import('../pages/page/element/banner.vue' /* webpackChunkName: "pages/page/element/banner" */))
const _333dbcde = () => interopDefault(import('../pages/page/element/category.vue' /* webpackChunkName: "pages/page/element/category" */))
const _5dfd53b8 = () => interopDefault(import('../pages/page/element/collection-banner.vue' /* webpackChunkName: "pages/page/element/collection-banner" */))
const _400a91cc = () => interopDefault(import('../pages/page/element/home-slider.vue' /* webpackChunkName: "pages/page/element/home-slider" */))
const _5d568980 = () => interopDefault(import('../pages/page/element/logo-slider.vue' /* webpackChunkName: "pages/page/element/logo-slider" */))
const _c426f0f0 = () => interopDefault(import('../pages/page/element/multi-slider.vue' /* webpackChunkName: "pages/page/element/multi-slider" */))
const _72f8615c = () => interopDefault(import('../pages/page/element/product-slider.vue' /* webpackChunkName: "pages/page/element/product-slider" */))
const _016635af = () => interopDefault(import('../pages/page/element/product-tabs.vue' /* webpackChunkName: "pages/page/element/product-tabs" */))
const _0213ab1c = () => interopDefault(import('../pages/page/element/service.vue' /* webpackChunkName: "pages/page/element/service" */))
const _16a89abb = () => interopDefault(import('../pages/page/portfolio/masonary-fullwidth.vue' /* webpackChunkName: "pages/page/portfolio/masonary-fullwidth" */))
const _72063d1a = () => interopDefault(import('../pages/page/portfolio/mesonary-grid-2.vue' /* webpackChunkName: "pages/page/portfolio/mesonary-grid-2" */))
const _71ea0e18 = () => interopDefault(import('../pages/page/portfolio/mesonary-grid-3.vue' /* webpackChunkName: "pages/page/portfolio/mesonary-grid-3" */))
const _71cddf16 = () => interopDefault(import('../pages/page/portfolio/mesonary-grid-4.vue' /* webpackChunkName: "pages/page/portfolio/mesonary-grid-4" */))
const _4d52ac29 = () => interopDefault(import('../pages/page/portfolio/portfolio-2-col.vue' /* webpackChunkName: "pages/page/portfolio/portfolio-2-col" */))
const _3cd1c9ac = () => interopDefault(import('../pages/page/portfolio/portfolio-3-col.vue' /* webpackChunkName: "pages/page/portfolio/portfolio-3-col" */))
const _75db8a2b = () => interopDefault(import('../pages/page/portfolio/portfolio-4-col.vue' /* webpackChunkName: "pages/page/portfolio/portfolio-4-col" */))
const _aad32c5a = () => interopDefault(import('../pages/product/sidebar/no-sidebar.vue' /* webpackChunkName: "pages/product/sidebar/no-sidebar" */))
const _db960c10 = () => interopDefault(import('../pages/product/sidebar/right-sidebar.vue' /* webpackChunkName: "pages/product/sidebar/right-sidebar" */))
const _61b17f54 = () => interopDefault(import('../pages/product/three-column/thumbnail-bottom.vue' /* webpackChunkName: "pages/product/three-column/thumbnail-bottom" */))
const _0e8120f2 = () => interopDefault(import('../pages/product/three-column/thumbnail-left.vue' /* webpackChunkName: "pages/product/three-column/thumbnail-left" */))
const _022fd17e = () => interopDefault(import('../pages/product/three-column/thumbnail-right.vue' /* webpackChunkName: "pages/product/three-column/thumbnail-right" */))
const _6c6456de = () => interopDefault(import('../pages/product/thumbnail-image/image-outside.vue' /* webpackChunkName: "pages/product/thumbnail-image/image-outside" */))
const _2af21e7a = () => interopDefault(import('../pages/product/thumbnail-image/left-image.vue' /* webpackChunkName: "pages/product/thumbnail-image/left-image" */))
const _6e8aa156 = () => interopDefault(import('../pages/product/thumbnail-image/right-image.vue' /* webpackChunkName: "pages/product/thumbnail-image/right-image" */))
const _16eb095c = () => interopDefault(import('../pages/page/account/auth/auth.js' /* webpackChunkName: "pages/page/account/auth/auth" */))
const _402a568c = () => interopDefault(import('../pages/shop/bags/components/banner.vue' /* webpackChunkName: "pages/shop/bags/components/banner" */))
const _14781fb0 = () => interopDefault(import('../pages/shop/bags/components/blog.vue' /* webpackChunkName: "pages/shop/bags/components/blog" */))
const _7ea317e8 = () => interopDefault(import('../pages/shop/bags/components/category.vue' /* webpackChunkName: "pages/shop/bags/components/category" */))
const _5537b6d6 = () => interopDefault(import('../pages/shop/bags/components/category2.vue' /* webpackChunkName: "pages/shop/bags/components/category2" */))
const _41640c8e = () => interopDefault(import('../pages/shop/bags/components/categorytab.vue' /* webpackChunkName: "pages/shop/bags/components/categorytab" */))
const _2d5f4c94 = () => interopDefault(import('../pages/shop/bags/components/instagram.vue' /* webpackChunkName: "pages/shop/bags/components/instagram" */))
const _531115f0 = () => interopDefault(import('../pages/shop/bags/components/productcategoryslider.vue' /* webpackChunkName: "pages/shop/bags/components/productcategoryslider" */))
const _36fb8772 = () => interopDefault(import('../pages/shop/bags/components/productslider.vue' /* webpackChunkName: "pages/shop/bags/components/productslider" */))
const _846fd128 = () => interopDefault(import('../pages/shop/bags/components/services.vue' /* webpackChunkName: "pages/shop/bags/components/services" */))
const _5f57ebef = () => interopDefault(import('../pages/shop/bags/components/slider.vue' /* webpackChunkName: "pages/shop/bags/components/slider" */))
const _ed951484 = () => interopDefault(import('../pages/shop/beauty/components/about.vue' /* webpackChunkName: "pages/shop/beauty/components/about" */))
const _1ff527fe = () => interopDefault(import('../pages/shop/beauty/components/blog.vue' /* webpackChunkName: "pages/shop/beauty/components/blog" */))
const _870bea3a = () => interopDefault(import('../pages/shop/beauty/components/instagram.vue' /* webpackChunkName: "pages/shop/beauty/components/instagram" */))
const _a53616c4 = () => interopDefault(import('../pages/shop/beauty/components/product-slider.vue' /* webpackChunkName: "pages/shop/beauty/components/product-slider" */))
const _e6793000 = () => interopDefault(import('../pages/shop/beauty/components/slider.vue' /* webpackChunkName: "pages/shop/beauty/components/slider" */))
const _01749496 = () => interopDefault(import('../pages/shop/beauty/components/top-product-slider.vue' /* webpackChunkName: "pages/shop/beauty/components/top-product-slider" */))
const _8b79e5e2 = () => interopDefault(import('../pages/shop/beauty/components/video-tutorial.vue' /* webpackChunkName: "pages/shop/beauty/components/video-tutorial" */))
const _78aad8fe = () => interopDefault(import('../pages/shop/electronics-1/components/collection_banner.vue' /* webpackChunkName: "pages/shop/electronics-1/components/collection_banner" */))
const _03883e4e = () => interopDefault(import('../pages/shop/electronics-1/components/product_tab.vue' /* webpackChunkName: "pages/shop/electronics-1/components/product_tab" */))
const _15a8c8fd = () => interopDefault(import('../pages/shop/electronics-1/components/slider.vue' /* webpackChunkName: "pages/shop/electronics-1/components/slider" */))
const _8d62406c = () => interopDefault(import('../pages/shop/fashion-2/components/banner.vue' /* webpackChunkName: "pages/shop/fashion-2/components/banner" */))
const _65f8933c = () => interopDefault(import('../pages/shop/fashion-2/components/collection.vue' /* webpackChunkName: "pages/shop/fashion-2/components/collection" */))
const _25b1f2e6 = () => interopDefault(import('../pages/shop/fashion-2/components/collection-banner.vue' /* webpackChunkName: "pages/shop/fashion-2/components/collection-banner" */))
const _2e82a784 = () => interopDefault(import('../pages/shop/fashion-2/components/instagram.vue' /* webpackChunkName: "pages/shop/fashion-2/components/instagram" */))
const _e826667e = () => interopDefault(import('../pages/shop/fashion-2/components/product.vue' /* webpackChunkName: "pages/shop/fashion-2/components/product" */))
const _38bbf6ff = () => interopDefault(import('../pages/shop/fashion-2/components/slider.vue' /* webpackChunkName: "pages/shop/fashion-2/components/slider" */))
const _0380790b = () => interopDefault(import('../pages/shop/fashion-3/components/banner.vue' /* webpackChunkName: "pages/shop/fashion-3/components/banner" */))
const _9ea472e0 = () => interopDefault(import('../pages/shop/fashion-3/components/product_slider.vue' /* webpackChunkName: "pages/shop/fashion-3/components/product_slider" */))
const _42302b76 = () => interopDefault(import('../pages/shop/fashion-3/components/product_tab.vue' /* webpackChunkName: "pages/shop/fashion-3/components/product_tab" */))
const _fa24df80 = () => interopDefault(import('../pages/shop/fashion-3/components/slider.vue' /* webpackChunkName: "pages/shop/fashion-3/components/slider" */))
const _85f204b6 = () => interopDefault(import('../pages/shop/fashion/components/banner.vue' /* webpackChunkName: "pages/shop/fashion/components/banner" */))
const _2c60f14a = () => interopDefault(import('../pages/shop/fashion/components/blog.vue' /* webpackChunkName: "pages/shop/fashion/components/blog" */))
const _a063a8f8 = () => interopDefault(import('../pages/shop/fashion/components/collection_banner.vue' /* webpackChunkName: "pages/shop/fashion/components/collection_banner" */))
const _0546106e = () => interopDefault(import('../pages/shop/fashion/components/instagram.vue' /* webpackChunkName: "pages/shop/fashion/components/instagram" */))
const _45527ccc = () => interopDefault(import('../pages/shop/fashion/components/logo_slider.vue' /* webpackChunkName: "pages/shop/fashion/components/logo_slider" */))
const _02c9ddac = () => interopDefault(import('../pages/shop/fashion/components/product_slider.vue' /* webpackChunkName: "pages/shop/fashion/components/product_slider" */))
const _5a3311c8 = () => interopDefault(import('../pages/shop/fashion/components/product_tab.vue' /* webpackChunkName: "pages/shop/fashion/components/product_tab" */))
const _77049cd2 = () => interopDefault(import('../pages/shop/fashion/components/services.vue' /* webpackChunkName: "pages/shop/fashion/components/services" */))
const _3c7414da = () => interopDefault(import('../pages/shop/fashion/components/slider.vue' /* webpackChunkName: "pages/shop/fashion/components/slider" */))
const _919d9f40 = () => interopDefault(import('../pages/shop/flower/components/blog.vue' /* webpackChunkName: "pages/shop/flower/components/blog" */))
const _fa68e2dc = () => interopDefault(import('../pages/shop/flower/components/category_tab.vue' /* webpackChunkName: "pages/shop/flower/components/category_tab" */))
const _3b7c129f = () => interopDefault(import('../pages/shop/flower/components/collection_banner.vue' /* webpackChunkName: "pages/shop/flower/components/collection_banner" */))
const _5fb5ac38 = () => interopDefault(import('../pages/shop/flower/components/instagram.vue' /* webpackChunkName: "pages/shop/flower/components/instagram" */))
const _2934f7ef = () => interopDefault(import('../pages/shop/flower/components/product_slider.vue' /* webpackChunkName: "pages/shop/flower/components/product_slider" */))
const _4729501c = () => interopDefault(import('../pages/shop/flower/components/services.vue' /* webpackChunkName: "pages/shop/flower/components/services" */))
const _380f909f = () => interopDefault(import('../pages/shop/flower/components/slider.vue' /* webpackChunkName: "pages/shop/flower/components/slider" */))
const _5c5e5468 = () => interopDefault(import('../pages/shop/flower/components/top_products.vue' /* webpackChunkName: "pages/shop/flower/components/top_products" */))
const _c6f35656 = () => interopDefault(import('../pages/shop/furniture/components/blog.vue' /* webpackChunkName: "pages/shop/furniture/components/blog" */))
const _b3f923f2 = () => interopDefault(import('../pages/shop/furniture/components/category_tab.vue' /* webpackChunkName: "pages/shop/furniture/components/category_tab" */))
const _5a02d76c = () => interopDefault(import('../pages/shop/furniture/components/collection_banner.vue' /* webpackChunkName: "pages/shop/furniture/components/collection_banner" */))
const _7e267cf1 = () => interopDefault(import('../pages/shop/furniture/components/parallax_banner.vue' /* webpackChunkName: "pages/shop/furniture/components/parallax_banner" */))
const _1cad6bd4 = () => interopDefault(import('../pages/shop/furniture/components/slider.vue' /* webpackChunkName: "pages/shop/furniture/components/slider" */))
const _e8427944 = () => interopDefault(import('../pages/shop/gym/components/blog.vue' /* webpackChunkName: "pages/shop/gym/components/blog" */))
const _ab623aa2 = () => interopDefault(import('../pages/shop/gym/components/collection-banner.vue' /* webpackChunkName: "pages/shop/gym/components/collection-banner" */))
const _96dc74b4 = () => interopDefault(import('../pages/shop/gym/components/instagram.vue' /* webpackChunkName: "pages/shop/gym/components/instagram" */))
const _243f4492 = () => interopDefault(import('../pages/shop/gym/components/logo-slider.vue' /* webpackChunkName: "pages/shop/gym/components/logo-slider" */))
const _074fd578 = () => interopDefault(import('../pages/shop/gym/components/product-list.vue' /* webpackChunkName: "pages/shop/gym/components/product-list" */))
const _d0b747c6 = () => interopDefault(import('../pages/shop/gym/components/slider.vue' /* webpackChunkName: "pages/shop/gym/components/slider" */))
const _42697ed2 = () => interopDefault(import('../pages/shop/gym/components/top-collection.vue' /* webpackChunkName: "pages/shop/gym/components/top-collection" */))
const _0994cc02 = () => interopDefault(import('../pages/shop/jewellery/components/category.vue' /* webpackChunkName: "pages/shop/jewellery/components/category" */))
const _0143f35e = () => interopDefault(import('../pages/shop/jewellery/components/instagram.vue' /* webpackChunkName: "pages/shop/jewellery/components/instagram" */))
const _635ae8ce = () => interopDefault(import('../pages/shop/jewellery/components/parallax-banner.vue' /* webpackChunkName: "pages/shop/jewellery/components/parallax-banner" */))
const _971fbdfa = () => interopDefault(import('../pages/shop/jewellery/components/product-slider.vue' /* webpackChunkName: "pages/shop/jewellery/components/product-slider" */))
const _2f021de3 = () => interopDefault(import('../pages/shop/jewellery/components/product-tab.vue' /* webpackChunkName: "pages/shop/jewellery/components/product-tab" */))
const _06ae6f62 = () => interopDefault(import('../pages/shop/jewellery/components/services.vue' /* webpackChunkName: "pages/shop/jewellery/components/services" */))
const _3a806d36 = () => interopDefault(import('../pages/shop/jewellery/components/slider.vue' /* webpackChunkName: "pages/shop/jewellery/components/slider" */))
const _3a530ee6 = () => interopDefault(import('../pages/shop/kids/components/collection_banner.vue' /* webpackChunkName: "pages/shop/kids/components/collection_banner" */))
const _62438fc2 = () => interopDefault(import('../pages/shop/kids/components/collection_slider.vue' /* webpackChunkName: "pages/shop/kids/components/collection_slider" */))
const _7bc35dd2 = () => interopDefault(import('../pages/shop/kids/components/instagram.vue' /* webpackChunkName: "pages/shop/kids/components/instagram" */))
const _7890f6d6 = () => interopDefault(import('../pages/shop/kids/components/logo_slider.vue' /* webpackChunkName: "pages/shop/kids/components/logo_slider" */))
const _242095f4 = () => interopDefault(import('../pages/shop/kids/components/parallax_banner.vue' /* webpackChunkName: "pages/shop/kids/components/parallax_banner" */))
const _a4bfee7e = () => interopDefault(import('../pages/shop/kids/components/product_slider.vue' /* webpackChunkName: "pages/shop/kids/components/product_slider" */))
const _c50cd91e = () => interopDefault(import('../pages/shop/kids/components/slider.vue' /* webpackChunkName: "pages/shop/kids/components/slider" */))
const _4bc2620e = () => interopDefault(import('../pages/shop/pets/components/blog.vue' /* webpackChunkName: "pages/shop/pets/components/blog" */))
const _65fc6a18 = () => interopDefault(import('../pages/shop/pets/components/collection-banner.vue' /* webpackChunkName: "pages/shop/pets/components/collection-banner" */))
const _ac37c488 = () => interopDefault(import('../pages/shop/pets/components/logo-slider.vue' /* webpackChunkName: "pages/shop/pets/components/logo-slider" */))
const _0aa3caca = () => interopDefault(import('../pages/shop/pets/components/parallax-banner.vue' /* webpackChunkName: "pages/shop/pets/components/parallax-banner" */))
const _56390196 = () => interopDefault(import('../pages/shop/pets/components/product-slider.vue' /* webpackChunkName: "pages/shop/pets/components/product-slider" */))
const _560fecf8 = () => interopDefault(import('../pages/shop/pets/components/slider.vue' /* webpackChunkName: "pages/shop/pets/components/slider" */))
const _8a5ff6a6 = () => interopDefault(import('../pages/shop/pets/components/top-collection.vue' /* webpackChunkName: "pages/shop/pets/components/top-collection" */))
const _3b23fab4 = () => interopDefault(import('../pages/shop/shoes/components/about.vue' /* webpackChunkName: "pages/shop/shoes/components/about" */))
const _4857704b = () => interopDefault(import('../pages/shop/shoes/components/blog.vue' /* webpackChunkName: "pages/shop/shoes/components/blog" */))
const _5c1095ae = () => interopDefault(import('../pages/shop/shoes/components/brand.vue' /* webpackChunkName: "pages/shop/shoes/components/brand" */))
const _5cedff27 = () => interopDefault(import('../pages/shop/shoes/components/category.vue' /* webpackChunkName: "pages/shop/shoes/components/category" */))
const _40e98f1b = () => interopDefault(import('../pages/shop/shoes/components/category2.vue' /* webpackChunkName: "pages/shop/shoes/components/category2" */))
const _40f7a69c = () => interopDefault(import('../pages/shop/shoes/components/category3.vue' /* webpackChunkName: "pages/shop/shoes/components/category3" */))
const _05714b1a = () => interopDefault(import('../pages/shop/shoes/components/collectionbanner.vue' /* webpackChunkName: "pages/shop/shoes/components/collectionbanner" */))
const _7cb471a8 = () => interopDefault(import('../pages/shop/shoes/components/collectionslider.vue' /* webpackChunkName: "pages/shop/shoes/components/collectionslider" */))
const _b4b1d144 = () => interopDefault(import('../pages/shop/shoes/components/collectiontab.vue' /* webpackChunkName: "pages/shop/shoes/components/collectiontab" */))
const _191124d9 = () => interopDefault(import('../pages/shop/shoes/components/instagram.vue' /* webpackChunkName: "pages/shop/shoes/components/instagram" */))
const _409f9157 = () => interopDefault(import('../pages/shop/shoes/components/productSlider.vue' /* webpackChunkName: "pages/shop/shoes/components/productSlider" */))
const _e1a77bc8 = () => interopDefault(import('../pages/shop/shoes/components/service.vue' /* webpackChunkName: "pages/shop/shoes/components/service" */))
const _18a581ca = () => interopDefault(import('../pages/shop/shoes/components/slider.vue' /* webpackChunkName: "pages/shop/shoes/components/slider" */))
const _3caaccbe = () => interopDefault(import('../pages/shop/tools/components/about.vue' /* webpackChunkName: "pages/shop/tools/components/about" */))
const _28e65d1a = () => interopDefault(import('../pages/shop/tools/components/category.vue' /* webpackChunkName: "pages/shop/tools/components/category" */))
const _ff26c1ee = () => interopDefault(import('../pages/shop/tools/components/logo_slider.vue' /* webpackChunkName: "pages/shop/tools/components/logo_slider" */))
const _9fb2ffca = () => interopDefault(import('../pages/shop/tools/components/product-slider.vue' /* webpackChunkName: "pages/shop/tools/components/product-slider" */))
const _ab7ea75a = () => interopDefault(import('../pages/shop/tools/components/product-tab-slider.vue' /* webpackChunkName: "pages/shop/tools/components/product-tab-slider" */))
const _0d6a10ae = () => interopDefault(import('../pages/shop/tools/components/select-vehical.vue' /* webpackChunkName: "pages/shop/tools/components/select-vehical" */))
const _a2f24c6e = () => interopDefault(import('../pages/shop/tools/components/service.vue' /* webpackChunkName: "pages/shop/tools/components/service" */))
const _42f2c07d = () => interopDefault(import('../pages/shop/tools/components/slider.vue' /* webpackChunkName: "pages/shop/tools/components/slider" */))
const _3277d07e = () => interopDefault(import('../pages/shop/vegetables/components/banner.vue' /* webpackChunkName: "pages/shop/vegetables/components/banner" */))
const _0d047877 = () => interopDefault(import('../pages/shop/vegetables/components/blog.vue' /* webpackChunkName: "pages/shop/vegetables/components/blog" */))
const _461a4f46 = () => interopDefault(import('../pages/shop/vegetables/components/product_slider.vue' /* webpackChunkName: "pages/shop/vegetables/components/product_slider" */))
const _735cb4b3 = () => interopDefault(import('../pages/shop/vegetables/components/services.vue' /* webpackChunkName: "pages/shop/vegetables/components/services" */))
const _66312ef6 = () => interopDefault(import('../pages/shop/vegetables/components/slider.vue' /* webpackChunkName: "pages/shop/vegetables/components/slider" */))
const _278b5902 = () => interopDefault(import('../pages/shop/vegetables/components/special_products.vue' /* webpackChunkName: "pages/shop/vegetables/components/special_products" */))
const _5067b8b2 = () => interopDefault(import('../pages/shop/watch/components/blog.vue' /* webpackChunkName: "pages/shop/watch/components/blog" */))
const _4d7487e4 = () => interopDefault(import('../pages/shop/watch/components/category.vue' /* webpackChunkName: "pages/shop/watch/components/category" */))
const _0c2754e8 = () => interopDefault(import('../pages/shop/watch/components/categorytabs.vue' /* webpackChunkName: "pages/shop/watch/components/categorytabs" */))
const _fb9f27ee = () => interopDefault(import('../pages/shop/watch/components/collectionbanners.vue' /* webpackChunkName: "pages/shop/watch/components/collectionbanners" */))
const _27b104d2 = () => interopDefault(import('../pages/shop/watch/components/instagram.vue' /* webpackChunkName: "pages/shop/watch/components/instagram" */))
const _2ad76b95 = () => interopDefault(import('../pages/shop/watch/components/logo_slider.vue' /* webpackChunkName: "pages/shop/watch/components/logo_slider" */))
const _6722c1c1 = () => interopDefault(import('../pages/shop/watch/components/product_slider.vue' /* webpackChunkName: "pages/shop/watch/components/product_slider" */))
const _53414124 = () => interopDefault(import('../pages/shop/watch/components/services.vue' /* webpackChunkName: "pages/shop/watch/components/services" */))
const _5dc54c71 = () => interopDefault(import('../pages/shop/watch/components/slider.vue' /* webpackChunkName: "pages/shop/watch/components/slider" */))
const _91928714 = () => interopDefault(import('../pages/shop/watch/components/timer_banner.vue' /* webpackChunkName: "pages/shop/watch/components/timer_banner" */))
const _a42a27c4 = () => interopDefault(import('../pages/shop/watch/components/top_products.vue' /* webpackChunkName: "pages/shop/watch/components/top_products" */))
const _42f70b7f = () => interopDefault(import('../pages/collection/leftsidebar/_id.vue' /* webpackChunkName: "pages/collection/leftsidebar/_id" */))
const _3b1645c7 = () => interopDefault(import('../pages/product/sidebar/_id.vue' /* webpackChunkName: "pages/product/sidebar/_id" */))
const _73d0d09c = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

const emptyFn = () => {}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/multikart/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/blog/blog-detail",
    component: _1c6e12bf,
    name: "blog-blog-detail"
  }, {
    path: "/blog/blog-leftsidebar",
    component: _325c82f7,
    name: "blog-blog-leftsidebar"
  }, {
    path: "/blog/blog-nosidebar",
    component: _12092106,
    name: "blog-blog-nosidebar"
  }, {
    path: "/blog/blog-rightsidebar",
    component: _4a92f7a4,
    name: "blog-blog-rightsidebar"
  }, {
    path: "/collection/full-width",
    component: _b57c570e,
    name: "collection-full-width"
  }, {
    path: "/collection/list-view",
    component: _3dce61da,
    name: "collection-list-view"
  }, {
    path: "/collection/metro",
    component: _1a1f5eb8,
    name: "collection-metro"
  }, {
    path: "/collection/no-sidebar",
    component: _61991ec1,
    name: "collection-no-sidebar"
  }, {
    path: "/collection/right-sidebar",
    component: _939c136c,
    name: "collection-right-sidebar"
  }, {
    path: "/collection/sidebar-popup",
    component: _5111149a,
    name: "collection-sidebar-popup"
  }, {
    path: "/collection/six-grid",
    component: _082ecafc,
    name: "collection-six-grid"
  }, {
    path: "/collection/three-grid",
    component: _d67739f4,
    name: "collection-three-grid"
  }, {
    path: "/page/404",
    component: _4cac33f0,
    name: "page-404"
  }, {
    path: "/page/about",
    component: _1ac65fdd,
    name: "page-about"
  }, {
    path: "/page/collection",
    component: _02452cfe,
    name: "page-collection"
  }, {
    path: "/page/coming-soon",
    component: _1fe99217,
    name: "page-coming-soon"
  }, {
    path: "/page/faq",
    component: _f4caee34,
    name: "page-faq"
  }, {
    path: "/page/lookbook",
    component: _00aa6568,
    name: "page-lookbook"
  }, {
    path: "/page/order-success",
    component: _2a66a558,
    name: "page-order-success"
  }, {
    path: "/page/review",
    component: _7a5c2cb8,
    name: "page-review"
  }, {
    path: "/page/search",
    component: _7df019f0,
    name: "page-search"
  }, {
    path: "/page/typography",
    component: _7a66430f,
    name: "page-typography"
  }, {
    path: "/product/bundle-product",
    component: _b986e7d8,
    name: "product-bundle-product"
  }, {
    path: "/product/four-image",
    component: _316bb138,
    name: "product-four-image"
  }, {
    path: "/shop/bags",
    component: _6a687a47,
    name: "shop-bags"
  }, {
    path: "/shop/beauty",
    component: _76a8c7d8,
    name: "shop-beauty"
  }, {
    path: "/shop/electronics-1",
    component: _6c7c0756,
    name: "shop-electronics-1"
  }, {
    path: "/shop/fashion",
    component: _e9bb289c,
    name: "shop-fashion"
  }, {
    path: "/shop/fashion-2",
    component: _2c8ec552,
    name: "shop-fashion-2"
  }, {
    path: "/shop/fashion-3",
    component: _7e9d5018,
    name: "shop-fashion-3"
  }, {
    path: "/shop/flower",
    component: _236da6f7,
    name: "shop-flower"
  }, {
    path: "/shop/furniture",
    component: _2d8a2ca8,
    name: "shop-furniture"
  }, {
    path: "/shop/gym",
    component: _13293f75,
    name: "shop-gym"
  }, {
    path: "/shop/jewellery",
    component: _344858bd,
    name: "shop-jewellery"
  }, {
    path: "/shop/kids",
    component: _8f90566e,
    name: "shop-kids"
  }, {
    path: "/shop/pets",
    component: _3ac9fe60,
    name: "shop-pets"
  }, {
    path: "/shop/shoes",
    component: _1bdbc0a2,
    name: "shop-shoes"
  }, {
    path: "/shop/tools",
    component: _4eb99856,
    name: "shop-tools"
  }, {
    path: "/shop/vegetables",
    component: _4d00cfce,
    name: "shop-vegetables"
  }, {
    path: "/shop/watch",
    component: _ecdde46e,
    name: "shop-watch"
  }, {
    path: "/blog/widgets/blog-list",
    component: _5533b3ac,
    name: "blog-widgets-blog-list"
  }, {
    path: "/blog/widgets/blog-sidebar",
    component: _1b59b684,
    name: "blog-widgets-blog-sidebar"
  }, {
    path: "/page/account/cart",
    component: _d40d5fbc,
    name: "page-account-cart"
  }, {
    path: "/page/account/checkout",
    component: _7bf15a48,
    name: "page-account-checkout"
  }, {
    path: "/page/account/contact",
    component: _1413040e,
    name: "page-account-contact"
  }, {
    path: "/page/account/dashboard",
    component: _4bdc7302,
    name: "page-account-dashboard"
  }, {
    path: "/page/account/forget-password",
    component: _1f1c8a2e,
    name: "page-account-forget-password"
  }, {
    path: "/page/account/login",
    component: _8eb73f52,
    name: "page-account-login"
  }, {
    path: "/page/account/login-firebase",
    component: _6af4c6ed,
    name: "page-account-login-firebase"
  }, {
    path: "/page/account/profile",
    component: _1c3a7d17,
    name: "page-account-profile"
  }, {
    path: "/page/account/register",
    component: _820f75b6,
    name: "page-account-register"
  }, {
    path: "/page/account/wishlist",
    component: _13236b47,
    name: "page-account-wishlist"
  }, {
    path: "/page/compare/compare-1",
    component: _b8d95822,
    name: "page-compare-compare-1"
  }, {
    path: "/page/compare/compare-2",
    component: _b8bd2920,
    name: "page-compare-compare-2"
  }, {
    path: "/page/element/banner",
    component: _63051f7f,
    name: "page-element-banner"
  }, {
    path: "/page/element/category",
    component: _333dbcde,
    name: "page-element-category"
  }, {
    path: "/page/element/collection-banner",
    component: _5dfd53b8,
    name: "page-element-collection-banner"
  }, {
    path: "/page/element/home-slider",
    component: _400a91cc,
    name: "page-element-home-slider"
  }, {
    path: "/page/element/logo-slider",
    component: _5d568980,
    name: "page-element-logo-slider"
  }, {
    path: "/page/element/multi-slider",
    component: _c426f0f0,
    name: "page-element-multi-slider"
  }, {
    path: "/page/element/product-slider",
    component: _72f8615c,
    name: "page-element-product-slider"
  }, {
    path: "/page/element/product-tabs",
    component: _016635af,
    name: "page-element-product-tabs"
  }, {
    path: "/page/element/service",
    component: _0213ab1c,
    name: "page-element-service"
  }, {
    path: "/page/portfolio/masonary-fullwidth",
    component: _16a89abb,
    name: "page-portfolio-masonary-fullwidth"
  }, {
    path: "/page/portfolio/mesonary-grid-2",
    component: _72063d1a,
    name: "page-portfolio-mesonary-grid-2"
  }, {
    path: "/page/portfolio/mesonary-grid-3",
    component: _71ea0e18,
    name: "page-portfolio-mesonary-grid-3"
  }, {
    path: "/page/portfolio/mesonary-grid-4",
    component: _71cddf16,
    name: "page-portfolio-mesonary-grid-4"
  }, {
    path: "/page/portfolio/portfolio-2-col",
    component: _4d52ac29,
    name: "page-portfolio-portfolio-2-col"
  }, {
    path: "/page/portfolio/portfolio-3-col",
    component: _3cd1c9ac,
    name: "page-portfolio-portfolio-3-col"
  }, {
    path: "/page/portfolio/portfolio-4-col",
    component: _75db8a2b,
    name: "page-portfolio-portfolio-4-col"
  }, {
    path: "/product/sidebar/no-sidebar",
    component: _aad32c5a,
    name: "product-sidebar-no-sidebar"
  }, {
    path: "/product/sidebar/right-sidebar",
    component: _db960c10,
    name: "product-sidebar-right-sidebar"
  }, {
    path: "/product/three-column/thumbnail-bottom",
    component: _61b17f54,
    name: "product-three-column-thumbnail-bottom"
  }, {
    path: "/product/three-column/thumbnail-left",
    component: _0e8120f2,
    name: "product-three-column-thumbnail-left"
  }, {
    path: "/product/three-column/thumbnail-right",
    component: _022fd17e,
    name: "product-three-column-thumbnail-right"
  }, {
    path: "/product/thumbnail-image/image-outside",
    component: _6c6456de,
    name: "product-thumbnail-image-image-outside"
  }, {
    path: "/product/thumbnail-image/left-image",
    component: _2af21e7a,
    name: "product-thumbnail-image-left-image"
  }, {
    path: "/product/thumbnail-image/right-image",
    component: _6e8aa156,
    name: "product-thumbnail-image-right-image"
  }, {
    path: "/page/account/auth/auth",
    component: _16eb095c,
    name: "page-account-auth-auth"
  }, {
    path: "/shop/bags/components/banner",
    component: _402a568c,
    name: "shop-bags-components-banner"
  }, {
    path: "/shop/bags/components/blog",
    component: _14781fb0,
    name: "shop-bags-components-blog"
  }, {
    path: "/shop/bags/components/category",
    component: _7ea317e8,
    name: "shop-bags-components-category"
  }, {
    path: "/shop/bags/components/category2",
    component: _5537b6d6,
    name: "shop-bags-components-category2"
  }, {
    path: "/shop/bags/components/categorytab",
    component: _41640c8e,
    name: "shop-bags-components-categorytab"
  }, {
    path: "/shop/bags/components/instagram",
    component: _2d5f4c94,
    name: "shop-bags-components-instagram"
  }, {
    path: "/shop/bags/components/productcategoryslider",
    component: _531115f0,
    name: "shop-bags-components-productcategoryslider"
  }, {
    path: "/shop/bags/components/productslider",
    component: _36fb8772,
    name: "shop-bags-components-productslider"
  }, {
    path: "/shop/bags/components/services",
    component: _846fd128,
    name: "shop-bags-components-services"
  }, {
    path: "/shop/bags/components/slider",
    component: _5f57ebef,
    name: "shop-bags-components-slider"
  }, {
    path: "/shop/beauty/components/about",
    component: _ed951484,
    name: "shop-beauty-components-about"
  }, {
    path: "/shop/beauty/components/blog",
    component: _1ff527fe,
    name: "shop-beauty-components-blog"
  }, {
    path: "/shop/beauty/components/instagram",
    component: _870bea3a,
    name: "shop-beauty-components-instagram"
  }, {
    path: "/shop/beauty/components/product-slider",
    component: _a53616c4,
    name: "shop-beauty-components-product-slider"
  }, {
    path: "/shop/beauty/components/slider",
    component: _e6793000,
    name: "shop-beauty-components-slider"
  }, {
    path: "/shop/beauty/components/top-product-slider",
    component: _01749496,
    name: "shop-beauty-components-top-product-slider"
  }, {
    path: "/shop/beauty/components/video-tutorial",
    component: _8b79e5e2,
    name: "shop-beauty-components-video-tutorial"
  }, {
    path: "/shop/electronics-1/components/collection_banner",
    component: _78aad8fe,
    name: "shop-electronics-1-components-collection_banner"
  }, {
    path: "/shop/electronics-1/components/product_tab",
    component: _03883e4e,
    name: "shop-electronics-1-components-product_tab"
  }, {
    path: "/shop/electronics-1/components/slider",
    component: _15a8c8fd,
    name: "shop-electronics-1-components-slider"
  }, {
    path: "/shop/fashion-2/components/banner",
    component: _8d62406c,
    name: "shop-fashion-2-components-banner"
  }, {
    path: "/shop/fashion-2/components/collection",
    component: _65f8933c,
    name: "shop-fashion-2-components-collection"
  }, {
    path: "/shop/fashion-2/components/collection-banner",
    component: _25b1f2e6,
    name: "shop-fashion-2-components-collection-banner"
  }, {
    path: "/shop/fashion-2/components/instagram",
    component: _2e82a784,
    name: "shop-fashion-2-components-instagram"
  }, {
    path: "/shop/fashion-2/components/product",
    component: _e826667e,
    name: "shop-fashion-2-components-product"
  }, {
    path: "/shop/fashion-2/components/slider",
    component: _38bbf6ff,
    name: "shop-fashion-2-components-slider"
  }, {
    path: "/shop/fashion-3/components/banner",
    component: _0380790b,
    name: "shop-fashion-3-components-banner"
  }, {
    path: "/shop/fashion-3/components/product_slider",
    component: _9ea472e0,
    name: "shop-fashion-3-components-product_slider"
  }, {
    path: "/shop/fashion-3/components/product_tab",
    component: _42302b76,
    name: "shop-fashion-3-components-product_tab"
  }, {
    path: "/shop/fashion-3/components/slider",
    component: _fa24df80,
    name: "shop-fashion-3-components-slider"
  }, {
    path: "/shop/fashion/components/banner",
    component: _85f204b6,
    name: "shop-fashion-components-banner"
  }, {
    path: "/shop/fashion/components/blog",
    component: _2c60f14a,
    name: "shop-fashion-components-blog"
  }, {
    path: "/shop/fashion/components/collection_banner",
    component: _a063a8f8,
    name: "shop-fashion-components-collection_banner"
  }, {
    path: "/shop/fashion/components/instagram",
    component: _0546106e,
    name: "shop-fashion-components-instagram"
  }, {
    path: "/shop/fashion/components/logo_slider",
    component: _45527ccc,
    name: "shop-fashion-components-logo_slider"
  }, {
    path: "/shop/fashion/components/product_slider",
    component: _02c9ddac,
    name: "shop-fashion-components-product_slider"
  }, {
    path: "/shop/fashion/components/product_tab",
    component: _5a3311c8,
    name: "shop-fashion-components-product_tab"
  }, {
    path: "/shop/fashion/components/services",
    component: _77049cd2,
    name: "shop-fashion-components-services"
  }, {
    path: "/shop/fashion/components/slider",
    component: _3c7414da,
    name: "shop-fashion-components-slider"
  }, {
    path: "/shop/flower/components/blog",
    component: _919d9f40,
    name: "shop-flower-components-blog"
  }, {
    path: "/shop/flower/components/category_tab",
    component: _fa68e2dc,
    name: "shop-flower-components-category_tab"
  }, {
    path: "/shop/flower/components/collection_banner",
    component: _3b7c129f,
    name: "shop-flower-components-collection_banner"
  }, {
    path: "/shop/flower/components/instagram",
    component: _5fb5ac38,
    name: "shop-flower-components-instagram"
  }, {
    path: "/shop/flower/components/product_slider",
    component: _2934f7ef,
    name: "shop-flower-components-product_slider"
  }, {
    path: "/shop/flower/components/services",
    component: _4729501c,
    name: "shop-flower-components-services"
  }, {
    path: "/shop/flower/components/slider",
    component: _380f909f,
    name: "shop-flower-components-slider"
  }, {
    path: "/shop/flower/components/top_products",
    component: _5c5e5468,
    name: "shop-flower-components-top_products"
  }, {
    path: "/shop/furniture/components/blog",
    component: _c6f35656,
    name: "shop-furniture-components-blog"
  }, {
    path: "/shop/furniture/components/category_tab",
    component: _b3f923f2,
    name: "shop-furniture-components-category_tab"
  }, {
    path: "/shop/furniture/components/collection_banner",
    component: _5a02d76c,
    name: "shop-furniture-components-collection_banner"
  }, {
    path: "/shop/furniture/components/parallax_banner",
    component: _7e267cf1,
    name: "shop-furniture-components-parallax_banner"
  }, {
    path: "/shop/furniture/components/slider",
    component: _1cad6bd4,
    name: "shop-furniture-components-slider"
  }, {
    path: "/shop/gym/components/blog",
    component: _e8427944,
    name: "shop-gym-components-blog"
  }, {
    path: "/shop/gym/components/collection-banner",
    component: _ab623aa2,
    name: "shop-gym-components-collection-banner"
  }, {
    path: "/shop/gym/components/instagram",
    component: _96dc74b4,
    name: "shop-gym-components-instagram"
  }, {
    path: "/shop/gym/components/logo-slider",
    component: _243f4492,
    name: "shop-gym-components-logo-slider"
  }, {
    path: "/shop/gym/components/product-list",
    component: _074fd578,
    name: "shop-gym-components-product-list"
  }, {
    path: "/shop/gym/components/slider",
    component: _d0b747c6,
    name: "shop-gym-components-slider"
  }, {
    path: "/shop/gym/components/top-collection",
    component: _42697ed2,
    name: "shop-gym-components-top-collection"
  }, {
    path: "/shop/jewellery/components/category",
    component: _0994cc02,
    name: "shop-jewellery-components-category"
  }, {
    path: "/shop/jewellery/components/instagram",
    component: _0143f35e,
    name: "shop-jewellery-components-instagram"
  }, {
    path: "/shop/jewellery/components/parallax-banner",
    component: _635ae8ce,
    name: "shop-jewellery-components-parallax-banner"
  }, {
    path: "/shop/jewellery/components/product-slider",
    component: _971fbdfa,
    name: "shop-jewellery-components-product-slider"
  }, {
    path: "/shop/jewellery/components/product-tab",
    component: _2f021de3,
    name: "shop-jewellery-components-product-tab"
  }, {
    path: "/shop/jewellery/components/services",
    component: _06ae6f62,
    name: "shop-jewellery-components-services"
  }, {
    path: "/shop/jewellery/components/slider",
    component: _3a806d36,
    name: "shop-jewellery-components-slider"
  }, {
    path: "/shop/kids/components/collection_banner",
    component: _3a530ee6,
    name: "shop-kids-components-collection_banner"
  }, {
    path: "/shop/kids/components/collection_slider",
    component: _62438fc2,
    name: "shop-kids-components-collection_slider"
  }, {
    path: "/shop/kids/components/instagram",
    component: _7bc35dd2,
    name: "shop-kids-components-instagram"
  }, {
    path: "/shop/kids/components/logo_slider",
    component: _7890f6d6,
    name: "shop-kids-components-logo_slider"
  }, {
    path: "/shop/kids/components/parallax_banner",
    component: _242095f4,
    name: "shop-kids-components-parallax_banner"
  }, {
    path: "/shop/kids/components/product_slider",
    component: _a4bfee7e,
    name: "shop-kids-components-product_slider"
  }, {
    path: "/shop/kids/components/slider",
    component: _c50cd91e,
    name: "shop-kids-components-slider"
  }, {
    path: "/shop/pets/components/blog",
    component: _4bc2620e,
    name: "shop-pets-components-blog"
  }, {
    path: "/shop/pets/components/collection-banner",
    component: _65fc6a18,
    name: "shop-pets-components-collection-banner"
  }, {
    path: "/shop/pets/components/logo-slider",
    component: _ac37c488,
    name: "shop-pets-components-logo-slider"
  }, {
    path: "/shop/pets/components/parallax-banner",
    component: _0aa3caca,
    name: "shop-pets-components-parallax-banner"
  }, {
    path: "/shop/pets/components/product-slider",
    component: _56390196,
    name: "shop-pets-components-product-slider"
  }, {
    path: "/shop/pets/components/slider",
    component: _560fecf8,
    name: "shop-pets-components-slider"
  }, {
    path: "/shop/pets/components/top-collection",
    component: _8a5ff6a6,
    name: "shop-pets-components-top-collection"
  }, {
    path: "/shop/shoes/components/about",
    component: _3b23fab4,
    name: "shop-shoes-components-about"
  }, {
    path: "/shop/shoes/components/blog",
    component: _4857704b,
    name: "shop-shoes-components-blog"
  }, {
    path: "/shop/shoes/components/brand",
    component: _5c1095ae,
    name: "shop-shoes-components-brand"
  }, {
    path: "/shop/shoes/components/category",
    component: _5cedff27,
    name: "shop-shoes-components-category"
  }, {
    path: "/shop/shoes/components/category2",
    component: _40e98f1b,
    name: "shop-shoes-components-category2"
  }, {
    path: "/shop/shoes/components/category3",
    component: _40f7a69c,
    name: "shop-shoes-components-category3"
  }, {
    path: "/shop/shoes/components/collectionbanner",
    component: _05714b1a,
    name: "shop-shoes-components-collectionbanner"
  }, {
    path: "/shop/shoes/components/collectionslider",
    component: _7cb471a8,
    name: "shop-shoes-components-collectionslider"
  }, {
    path: "/shop/shoes/components/collectiontab",
    component: _b4b1d144,
    name: "shop-shoes-components-collectiontab"
  }, {
    path: "/shop/shoes/components/instagram",
    component: _191124d9,
    name: "shop-shoes-components-instagram"
  }, {
    path: "/shop/shoes/components/productSlider",
    component: _409f9157,
    name: "shop-shoes-components-productSlider"
  }, {
    path: "/shop/shoes/components/service",
    component: _e1a77bc8,
    name: "shop-shoes-components-service"
  }, {
    path: "/shop/shoes/components/slider",
    component: _18a581ca,
    name: "shop-shoes-components-slider"
  }, {
    path: "/shop/tools/components/about",
    component: _3caaccbe,
    name: "shop-tools-components-about"
  }, {
    path: "/shop/tools/components/category",
    component: _28e65d1a,
    name: "shop-tools-components-category"
  }, {
    path: "/shop/tools/components/logo_slider",
    component: _ff26c1ee,
    name: "shop-tools-components-logo_slider"
  }, {
    path: "/shop/tools/components/product-slider",
    component: _9fb2ffca,
    name: "shop-tools-components-product-slider"
  }, {
    path: "/shop/tools/components/product-tab-slider",
    component: _ab7ea75a,
    name: "shop-tools-components-product-tab-slider"
  }, {
    path: "/shop/tools/components/select-vehical",
    component: _0d6a10ae,
    name: "shop-tools-components-select-vehical"
  }, {
    path: "/shop/tools/components/service",
    component: _a2f24c6e,
    name: "shop-tools-components-service"
  }, {
    path: "/shop/tools/components/slider",
    component: _42f2c07d,
    name: "shop-tools-components-slider"
  }, {
    path: "/shop/vegetables/components/banner",
    component: _3277d07e,
    name: "shop-vegetables-components-banner"
  }, {
    path: "/shop/vegetables/components/blog",
    component: _0d047877,
    name: "shop-vegetables-components-blog"
  }, {
    path: "/shop/vegetables/components/product_slider",
    component: _461a4f46,
    name: "shop-vegetables-components-product_slider"
  }, {
    path: "/shop/vegetables/components/services",
    component: _735cb4b3,
    name: "shop-vegetables-components-services"
  }, {
    path: "/shop/vegetables/components/slider",
    component: _66312ef6,
    name: "shop-vegetables-components-slider"
  }, {
    path: "/shop/vegetables/components/special_products",
    component: _278b5902,
    name: "shop-vegetables-components-special_products"
  }, {
    path: "/shop/watch/components/blog",
    component: _5067b8b2,
    name: "shop-watch-components-blog"
  }, {
    path: "/shop/watch/components/category",
    component: _4d7487e4,
    name: "shop-watch-components-category"
  }, {
    path: "/shop/watch/components/categorytabs",
    component: _0c2754e8,
    name: "shop-watch-components-categorytabs"
  }, {
    path: "/shop/watch/components/collectionbanners",
    component: _fb9f27ee,
    name: "shop-watch-components-collectionbanners"
  }, {
    path: "/shop/watch/components/instagram",
    component: _27b104d2,
    name: "shop-watch-components-instagram"
  }, {
    path: "/shop/watch/components/logo_slider",
    component: _2ad76b95,
    name: "shop-watch-components-logo_slider"
  }, {
    path: "/shop/watch/components/product_slider",
    component: _6722c1c1,
    name: "shop-watch-components-product_slider"
  }, {
    path: "/shop/watch/components/services",
    component: _53414124,
    name: "shop-watch-components-services"
  }, {
    path: "/shop/watch/components/slider",
    component: _5dc54c71,
    name: "shop-watch-components-slider"
  }, {
    path: "/shop/watch/components/timer_banner",
    component: _91928714,
    name: "shop-watch-components-timer_banner"
  }, {
    path: "/shop/watch/components/top_products",
    component: _a42a27c4,
    name: "shop-watch-components-top_products"
  }, {
    path: "/collection/leftsidebar/:id?",
    component: _42f70b7f,
    name: "collection-leftsidebar-id"
  }, {
    path: "/product/sidebar/:id?",
    component: _3b1645c7,
    name: "product-sidebar-id"
  }, {
    path: "/",
    component: _73d0d09c,
    name: "index"
  }],

  fallback: false
}

export function createRouter (ssrContext, config) {
  const base = (config._app && config._app.basePath) || routerOptions.base
  const router = new Router({ ...routerOptions, base  })

  // TODO: remove in Nuxt 3
  const originalPush = router.push
  router.push = function push (location, onComplete = emptyFn, onAbort) {
    return originalPush.call(this, location, onComplete, onAbort)
  }

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    return resolve(to, current, append)
  }

  return router
}
