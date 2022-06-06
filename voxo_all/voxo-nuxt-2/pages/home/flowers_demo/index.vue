<template>
  <div>
    <!-- header start -->
    <header2 />
    <!-- header end -->
    <homeSlider />
    <topBanner />
    <latest-products />
    <ourCategory />
    <newOffers />
    <ourProducts />
    <bannerWithTimer />
    <newsAndUpdate />
    <subscribe />
    <brand />
    <footer1> hello </footer1>
    <!-- tap to top Section Start -->
    <div class="tap-to-top">
      <a href="#home">
        <i class="fas fa-chevron-up"></i>
      </a>
    </div>
    <!-- tap to top Section End -->

    <div class="bg-overlay"></div>
  </div>
</template>

<script>
import homeSlider from "./components/homeSlider.vue";
import header2 from "~/components/header/header-2";
import topBanner from "./components/topBanner.vue";
import LatestProducts from "./components/latestProducts.vue";
import ourCategory from "./components/ourCategory.vue";
import newOffers from "./components/newOffers.vue";
import ourProducts from "./components/ourProducts.vue";
import bannerWithTimer from "./components/bannerWithTimer.vue";
import newsAndUpdate from "./components/newsAndUpdate.vue";
import subscribe from "./components/subscribe.vue";
import brand from "./components/brand.vue";
import footer1 from "./components/footer.vue";
export default {
  components: {
    footer1,
    brand,
    subscribe,
    newsAndUpdate,
    bannerWithTimer,
    topBanner,
    ourProducts,
    newOffers,
    homeSlider,
    header2,
    LatestProducts,
    ourCategory,
  },
};
</script>

<style lang="scss">
@import "~assets/scss/demo5.scss";
</style>
