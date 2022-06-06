<template>
  <div class="product-box">
    <div class="img-wrapper">
      <div class="front">
        <a
          href="product-left-sidebar.html"
          :class="isLoaded ? 'sliderBackground bg-size' : ''"
          :style="{
            'background-image': 'url(' + imageFront + ')',
          }"
        >
          <img
            :src="imageFront"
            class="bg-img"
            alt=""
            :style="{ display: isLoaded ? 'none' : '' }"
          />
        </a>
      </div>
      <div class="back">
        <a
          href="product-left-sidebar.html"
          :class="isLoaded ? 'sliderBackground bg-size' : ''"
          :style="{
            'background-image': 'url(' + imageBack + ')',
          }"
        >
          <img
            :src="imageBack"
            class="bg-img"
            alt=""
            :style="{ display: isLoaded ? 'none' : '' }"
          />
        </a>
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
    <productDetails />
  </div>
</template>

<script>
import VueFeather from "vue-feather";
import productDetails from "./components/productDetails.vue";
export default {
  props: ["imageFront", "imageBack"],
  components: {
    productDetails,
    VueFeather,
  },
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
