<template>
    <section class="ratio_asos overflow-hidden">
        <div class="px-0 container-fluid p-sm-0">
            <div class="row m-0">
                <div class="col-12 p-0">
                    <div class="title-3 text-center">
                        <h2>Our Product</h2>
                        <h5 class="theme-color">Our Collection</h5>
                    </div>
                </div>

                <div class="our-product">
                    <vue-slick-carousel v-bind="settings" ref="brandCarousel">
                        <arrivalCard v-for="(card, index) in cards" :key="index" :card="card" />
                    </vue-slick-carousel>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
    import { mapState } from "vuex";
    import VueSlickCarousel from "vue-slick-carousel";
    import arrivalCard from "~/components/elements/cards/furniture_arrival_card/index.vue";
    export default {
        components: {
            "vue-slick-carousel": VueSlickCarousel,
            arrivalCard,
        },
        computed: {
            ...mapState({ cards: (state) => state.arrivalCards.data }),
        },
        data() {
            return {
                isLoaded: false,

                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: "10px",

                    // focusOnSelect: true,
                    infinite: true,
                    slidesToShow: 5,
                    speed: 500,
                    dots: true,
                    responsive: [
                        {
                            breakpoint: 1200,
                            settings: {
                                slidesToShow: 3,
                                slidesToScroll: 3,
                                infinite: true,
                                dots: true,
                            },
                        },
                        {
                            breakpoint: 700,
                            settings: {
                                slidesToShow: 2,
                                slidesToScroll: 2,
                                initialSlide: 2,
                            },
                        },
                    ],
                },
            };
        },
        created() {
            this.isLoaded = true;
        },
    };
</script>

<style></style>