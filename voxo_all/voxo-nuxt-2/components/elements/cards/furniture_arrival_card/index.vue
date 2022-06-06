<template>
  <div :class="cardClasses">
    <div class="product-box">
      <div class="img-wrapper">
        <a
          href="product-left-sidebar.html"
          :class="isLoaded ? 'sliderBackground bg-size' : ''"
          :style="{
            'background-image':
              'url(/_nuxt/assets/images/furniture-images/new-arrival/' +
              card.image +
              ')',
          }"
        >
          <img
            :src="
              require(`../../../../assets/images/furniture-images/new-arrival/${card.image}`)
            "
            class="w-100 bg-img"
            alt=""
            :style="{ display: isLoaded ? 'none' : '' }"
          />
        </a>
        <div class="circle-shape"></div>
        <span class="background-text">Furniture</span>
        <div class="label-block">
          <span class="label label-black" v-if="card.leftBadge">{{
            card.leftBadge
          }}</span>
          <span class="label label-theme" v-if="card.rightBadge">{{
            card.rightBadge
          }}</span>
        </div>
        <div class="cart-wrap">
          <ul>
            <li>
              <a
                href="javascript:void(0)"
                class="addtocart-btn"
                data-bs-toggle="modal"
                data-bs-target="#addtocart"
              >
                <vue-feather type="shopping-bag"></vue-feather>
              </a>
            </li>
            <li>
              <a
                href="javascript:void(0)"
                data-bs-toggle="modal"
                data-bs-target="#quick-view"
              >
                <vue-feather type="eye"></vue-feather>
              </a>
            </li>
            <li>
              <a href="compare.html">
                <vue-feather type="refresh-cw"></vue-feather>
              </a>
            </li>
            <li>
              <a href="wishlist.html" class="wishlist">
                <vue-feather type="heart"></vue-feather>
              </a>
            </li>
          </ul>
        </div>
      </div>
      <div class="product-style-3 product-style-chair">
        <div class="product-title d-block mb-0">
          <p class="font-light mb-sm-2 mb-0">{{ card.subHeading }}</p>
          <a href="product-left-sidebar.html" class="font-default">
            <h5>{{ card.productName }}</h5>
          </a>
        </div>
        <div class="main-price">
          <ul class="rating mb-1 mt-0">
            <li v-for="(star, index2) in card.stars" :key="'A' + index2">
              <i class="fas fa-star theme-color"></i>
            </li>

            <li v-for="(noStar, index3) in 5 - card.stars" :key="'B' + index3">
              <i class="fas fa-star"></i>
            </li>
          </ul>
          <h3 class="theme-color">${{ card.price }}</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import VueFeather from "vue-feather";
export default {
  props: ["card", "cardClasses"],
  components: { VueFeather },
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
