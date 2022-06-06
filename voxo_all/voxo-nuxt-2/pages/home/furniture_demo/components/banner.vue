<template>
  <section class="banner-section pt-4">
    <div>
      <div class="container-fluid">
        <div class="row g-3">
          <div
            class="col-lg-4 col-md-6"
            v-for="(banner, index) in banners"
            :key="index"
          >
            <div class="banner-image">
              <a href="shop-left-sidebar.html">
                <img
                  src="~assets/images/furniture-images/banner/1.jpg"
                  class="w-100"
                  alt=""
                />
              </a>
              <div class="banner-details">
                <a href="wishlist.html" class="heart-button">
                  <i data-feather="heart"></i>
                  <vue-feather type="heart"></vue-feather>
                </a>
                <h4>
                  {{ banner.discount }}% <span class="theme-color">OFF</span>
                </h4>
                <div class="banner-price">
                  <h2>${{ banner.price }}.00</h2>
                  <h5 class="theme-color">
                    <del>${{ banner.mrp }}.00</del>
                  </h5>
                </div>
              </div>

              <a href="shop-left-sidebar.html" class="banner-shop text-center">
                <div>
                  <h5>{{ banner.title }}</h5>
                  <p class="mb-0 mt-2">{{ banner.subHeading }}</p>
                </div>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import VueFeather from "vue-feather";
export default {
  components: { VueFeather },
  data() {
    return {
      banners: [
        {
          title: "SHOP NOW",
          subHeading: "BUY ONE GET ONE FREE",
          mrp: "65",
          price: "79",
          discount: "26",
        },
        {
          title: "SHOP NOW",
          subHeading: "BUY ONE GET ONE FREE",
          mrp: "40",
          price: "42",
          discount: "45",
        },
        {
          title: "SHOP NOW",
          subHeading: "BUY ONE GET ONE FREE",
          mrp: "45",
          price: "50",
          discount: "15",
        },
      ],
    };
  },
};
</script>

<style></style>
