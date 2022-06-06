<template>
  <section class="ratio2_1 banner-style-2">
    <div class="container">
      <div class="row gy-4">
        <products-banner-card
          v-for="(product, index) in products"
          :key="index"
          :image="product.image"
          :discount="product.dicount"
          :productName="product.productName"
          :subHeading="product.subHeading"
        />
      </div>
    </div>
  </section>
</template>

<script>
import productsBannerCard from "~/components/elements/cards/productsBannerCard.vue";
export default {
  components: {
    productsBannerCard,
  },
  data() {
    return {
      isLoaded: false,
      products: [
        {
          productName: "New Hoddie",
          subHeading: "BUY ONE GET ONE FREE",
          image: "/_nuxt/assets/images/fashion/banner/1.jpg",
          discount: "26",
        },
        {
          productName: "Women Fashion",
          subHeading: "NEW OFFER 50% OFF",
          image: "/_nuxt/assets/images/fashion/banner/2.jpg",
          discount: "50",
        },
        {
          productName: "New Jacket",
          subHeading: "BUY ONE GET ONE FREE",
          image: "/_nuxt/assets/images/fashion/banner/3.jpg",
          discount: "36",
        },
      ],
    };
  },
  created() {
    this.isLoaded = true;
  },
};
</script>

<style></style>
