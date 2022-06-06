<template>
  <div class="col-lg-4 col-md-6">
    <div class="collection-banner p-bottom p-center text-center">
      <a
        href="shop-left-sidebar.html"
        class="banner-img"
        :class="isLoaded ? 'sliderBackground bg-size' : ''"
        :style="{
          'background-image': 'url(' + image + ')',
        }"
      >
        <img
          :src="image"
          class="bg-img"
          alt=""
          :style="{ display: isLoaded ? 'none' : '' }"
        />
      </a>
      <div class="banner-detail">
        <a href="javacript:void(0)" class="heart-wishlist">
          <i class="far fa-heart"></i>
        </a>
        <span class="font-dark-30" v-if="discount"
          >{{ discount }}% <span>OFF</span></span
        >
      </div>
      <a href="shop-left-sidebar.html" class="contain-banner">
        <div class="banner-content with-big">
          <h2 class="mb-2">{{ productName }}</h2>
          <span>{{ subHeading }}</span>
        </div>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  props: ["image", "discount", "productName", "subHeading"],
  data() {
    return {
      isLoaded: false,
    };
  },
  created() {
    this.isLoaded = true;
  },
};
</script>

<style></style>
