<template>
  <section class="ratio_asos overflow-hidden">
    <div class="container p-sm-0">
      <div class="row m-0">
        <div class="col-12 p-0">
          <div class="title-3 text-center">
            <h2>New Arrival</h2>
            <h5 class="theme-color">Our Collection</h5>
          </div>
        </div>
      </div>
      <!-- col-xl-3 col-lg-4 col-6 -->
      <div class="row g-sm-4 g-3">
        <arrivalCard v-for="(card, index) in cards" :key="index" :card="card" cardClasses="col-xl-3 col-lg-4 col-6" />
      </div>
    </div>
  </section>
</template>

<script>
  import { mapState } from "vuex";
  import VueFeather from "vue-feather";
  import arrivalCard from "~/components/elements/cards/furniture_arrival_card/index.vue";

  export default {
    components: { VueFeather, arrivalCard },
    data() {
      return {
        isLoaded: false,
      };
    },
    computed: {
      ...mapState({
        cards: (state) => state.arrivalCards.data,
      }),
    },
    mounted() {
      console.log("calls shou;d be added");
      this.isLoaded = true;
    },
  };
</script>

<style></style>