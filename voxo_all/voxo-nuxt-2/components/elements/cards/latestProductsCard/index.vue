<template>
  <div>
    <div class="product-box">
      <div class="img-wrapper">
        <a href="product-left-sidebar.html" :class="isLoaded ? 'sliderBackground bg-size' : ''" :style="{
            'background-image': 'url(' + image + ')',
          }">
          <img :src="image" class="img-fluid bg-img" alt="" :style="{ display: isLoaded ? 'none' : '' }" />
        </a>
        <div class="label-block">
          <span class="label label-black">New</span>
          <span class="label label-theme">50% Off</span>
        </div>
        <div class="cart-wrap">
          <ul>
            <li>
              <a href="javascript:void(0)" class="addtocart-btn" data-bs-toggle="modal" data-bs-target="#addtocart">
                <vue-feather type="shopping-bag"></vue-feather>
              </a>
            </li>
            <li>
              <a href="javascript:void(0)" data-bs-toggle="modal" data-bs-target="#quick-view">
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
      <div class="product-details text-center">
        <h3 class="theme-color">
          $49.00
          <span class="font-light ml-1">$52.00</span>
        </h3>
        <a href="product-left-sidebar.html" class="font-default">
          <h5>Beautiful and Fresh Bookey</h5>
        </a>
        <ul class="rating">
          <li>
            <i class="fas fa-star theme-color"></i>
          </li>
          <li>
            <i class="fas fa-star theme-color"></i>
          </li>
          <li>
            <i class="fas fa-star theme-color"></i>
          </li>
          <li>
            <i class="fas fa-star"></i>
          </li>
          <li>
            <i class="fas fa-star"></i>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
  import VueFeather from "vue-feather";

  export default {
    props: ["image"],
    components: {
      VueFeather,
    },
    data() {
      return {
        isLoaded: false,
      };
    },
    mounted() {
      this.isLoaded = true;
      console.log("coming to mounted", this.isLoaded);
    },
  };
</script>

<style></style>