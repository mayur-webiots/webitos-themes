<template>
  <div>
    <header1 />
    <homeSlider />
    <banner />
    <newArrival />
    <dealDayBanner />
    <carousels />
    <ourProducts />
    <hurryUp />
    <instagramShop />
    <service />
    <footerSection />
  </div>
</template>

<script>
import header1 from "~/components/header/header-1";
import homeSlider from "./components/homeSlider.vue";
import banner from "./components/banner.vue";
import newArrival from "./components/newArrival.vue";
import dealDayBanner from "./components/dealDayBanner.vue";
import carousels from "./components/carousels.vue";
import ourProducts from "./components/ourProducts.vue";
import hurryUp from "./components/hurryUp.vue";
import instagramShop from "./components/instagramShop.vue";
import service from "./components/service.vue";
import footerSection from "./components/footer.vue";
export default {
  components: {
    header1,
    homeSlider,
    banner,
    dealDayBanner,
    newArrival,
    carousels,
    ourProducts,
    hurryUp,
    instagramShop,
    service,
    footerSection,
  },
};
</script>

<style lang="scss">
@import "~assets/scss/demo4.scss";
</style>
