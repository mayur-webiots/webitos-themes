<template>
    <section class="section-b-space">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <div class="title-3 text-center">
                        <h2>Our News & Update</h2>
                        <h5>Our Blog</h5>
                    </div>
                </div>

                <div class="slide-3">
                    <vue-slick-carousel v-bind="settings" ref="brandCarousel">
                        <div class="product-style-4 ratio2_3" v-for="i in 3">
                            <div class="blog-header">
                                <div class="blog-image" :class="isLoaded ? 'sliderBackground bg-size' : ''" :style="{
                    'background-image': 'url(' + image + ')',
                  }">
                                    <img src="~assets/images/flower/new/1.jpg" class="img-fluid bg-img" alt=""
                                        :style="{ display: isLoaded ? 'none' : '' }" />
                                    <div class="blog-date">
                                        <div class="date-hover">
                                            <div>
                                                <h2>16</h2>
                                                <h3>MAY</h3>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="blog-footer">
                                <h2 class="theme-color">Flowers</h2>
                                <h5 class="theme-color">New Offer -56% Discount</h5>
                                <h4>Fresh</h4>
                                <h4 class="brand-name">Latest Night Lamp From $35</h4>
                                <button onclick="location.href='blog-details.html';" type="button"
                                    class="btn default-theme">
                                    Read More <i class="fas fa-chevron-right ms-2"></i>
                                </button>
                            </div>
                        </div>
                    </vue-slick-carousel>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
    import VueSlickCarousel from "vue-slick-carousel";
    export default {
        components: {
            "vue-slick-carousel": VueSlickCarousel,
        },
        data() {
            return {
                image: "/_nuxt/assets/images/flower/new/1.jpg",
                isLoaded: false,

                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: "10px",

                    // focusOnSelect: true,
                    infinite: true,
                    slidesToShow: 3,
                    speed: 500,
                    dots: true,
                    responsive: [
                        {
                            breakpoint: 1200,
                            settings: {
                                slidesToShow: 2,
                                slidesToScroll: 2,
                                infinite: true,
                                dots: true,
                            },
                        },
                        {
                            breakpoint: 750,
                            settings: {
                                slidesToShow: 1,
                                slidesToScroll: 1,
                                initialSlide: 1,
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