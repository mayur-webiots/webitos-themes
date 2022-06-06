<template>
  <div>
    <header1 />
    <!-- Add mobile view side menu -->
    <!-- <h3>mobile view side menu</h3> -->
    <heroCarousel />
    <fashionDemoBanner />
    <newArrivalCarousel />
    <ourCategory />
    <newOffers />
    <newArrivals />
    <bannerWithTimer />
    <instagramShop />
    <serviceSection />
    <footerSection />
    <!-- <cookieSection /                         > -->

    <div class="bg-overlay"></div>
  </div>
</template>

<script>
import header1 from "~/components/header/header-1";
import heroCarousel from "./components/fashionDemoHeroCarousel.vue";
import fashionDemoBanner from "./components/fashionDemoBanner.vue";
import newOffers from "./components/newOffers.vue";
import bannerWithTimer from "./components/bannerWithTimer.vue";
import serviceSection from "./components/serviceSection.vue";
import footerSection from "./components/footerSection.vue";
import cookieSection from "./components/cookieSection.vue";
import newArrivals from "./components/newArrivals.vue";
import instagramShop from "./components/instagramShop.vue";
import newArrivalCarousel from "./components/newArrivalCarousel.vue";
import ourCategory from "./components/ourCategory.vue";
// import tapToTop from "./components/tapToTop.vue";

export default {
  components: {
    ourCategory,
    heroCarousel,
    header1,
    fashionDemoBanner,
    newOffers,
    bannerWithTimer,
    serviceSection,
    footerSection,
    cookieSection,
    newArrivals,
    instagramShop,
    newArrivalCarousel,
    // tapToTop,
  },
};
</script>

<style lang="scss">
// @import "~assets/scss/demo2.scss";
// @import "~assets/scss/demo2_dark.scss";
</style>
