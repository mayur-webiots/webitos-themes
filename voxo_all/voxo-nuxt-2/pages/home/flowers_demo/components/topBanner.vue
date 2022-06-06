<template>
  <section class="ratio2_1 banner-style-2">
    <div class="container">
      <div class="row gy-4">
        <div
          class="col-lg-4 col-md-6"
          v-for="(banner, index) in banners"
          :key="index"
        >
          <div class="collection-banner p-bottom p-center text-center">
            <a
              href="shop-left-sidebar.html"
              class="banner-img"
              :class="isLoaded ? 'sliderBackground bg-size' : ''"
              :style="{
                'background-image': 'url(' + banner.image + ')',
              }"
            >
              <img
                :src="banner.image"
                class="bg-img blur-up lazyload"
                alt=""
                :style="{ display: isLoaded ? 'none' : '' }"
              />
            </a>
            <div class="banner-detail">
              <a href="javacript:void(0)" class="heart-wishlist">
                <i class="far fa-heart"></i>
              </a>
              <span class="font-dark-30"
                >{{ banner.discount }}% <span>OFF</span></span
              >
            </div>
            <a
              href="shop-left-sidebar.html"
              class="contain-banner contain-center"
            >
              <div class="banner-content banner-center with-bg">
                <h2 class="mb-2">{{ banner.title }}</h2>
                <span>{{ banner.subHeading }}</span>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      image: "/_nuxt/assets/images/flower/banner/2.jpg",
      banners: [
        {
          image: "/_nuxt/assets/images/flower/banner/1.jpg",
          title: "Pink Flower",
          subHeading: "BUY ONE GET ONE FREE",
          discount: "26",
        },
        {
          image: "/_nuxt/assets/images/flower/banner/2.jpg",
          title: "Yellow Flower",
          subHeading: "BUY ONE GET ONE FREE",
          discount: "26",
        },
        {
          image: "/_nuxt/assets/images/flower/banner/3.jpg",
          title: "Orange Flower",
          subHeading: "BUY ONE GET ONE FREE",
          discount: "26",
        },
      ],
      isLoaded: false,
    };
  },
  created() {
    this.isLoaded = true;
  },
};
</script>

<style></style>
