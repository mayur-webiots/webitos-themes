<template>
  <section class="ratio_asos">
    <div class="container">
      <div class="row m-0">
        <div class="col-sm-12 p-0">
          <div class="title title-2 text-center">
            <h2>New Arrival</h2>
            <h5 class="text-color">Our collection</h5>
          </div>
          <div class="product-wrapper product-style-2 row g-sm-4 g-3">
            <div class="col-xl-3 col-lg-4 col-6" v-for="i in 8" :key="i">
              <arrivalProductCard
                :imageBack="imageBack"
                :imageFront="imageFront"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import VueFeather from "vue-feather";
import arrivalProductCard from "~/components/elements/cards/arrivalProductsCard/index.vue";
export default {
  components: {
    VueFeather,
    arrivalProductCard,
  },
  data() {
    return {
      isLoaded: false,
      imageFront: "/_nuxt/assets/images/fashion/product/front/1.jpg",
      imageBack: "/_nuxt/assets/images/fashion/product/back/1.jpg",
    };
  },
  created() {
    this.isLoaded = true;
  },
};
</script>

<style></style>
