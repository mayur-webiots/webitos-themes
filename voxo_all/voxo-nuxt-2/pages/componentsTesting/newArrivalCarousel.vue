<template>
  <section class="ratio_asos">
    <div class="container">
      <div class="row m-0">
        <div class="col-sm-12 p-0">
          <div class="title title-2 text-center">
            <h2>New Arrival</h2>
            <h5 class="text-color">Our collection</h5>
          </div>
          <div
            class="product-wrapper product-style-2 slide-4 p-0 light-arrow bottom-space"
          >
            <vue-slick-carousel v-bind="settings" ref="brandCarousel">
              <div v-for="i in 5">
                <div class="product-box">
                  <div class="img-wrapper">
                    <div class="front">
                      <a href="product-left-sidebar.html">
                        <img
                          src="~assets/images/fashion/product/front/1.jpg"
                          class="bg-img"
                          alt=""
                        />
                      </a>
                    </div>
                    <div class="back">
                      <a href="product-left-sidebar.html">
                        <img
                          src="~assets/images/fashion/product/back/1.jpg"
                          class="bg-img"
                          alt=""
                        />
                      </a>
                    </div>
                    <div class="cart-wrap">
                      <ul>
                        <li>
                          <a
                            href="javascript:void(0)"
                            class="addtocart-btn"
                            data-bs-toggle="modal"
                            data-bs-target="#addtocart"
                          >
                            <!-- <i data-feather="shopping-bag"></i> -->
                            <vue-feather type="shopping-bag"></vue-feather>
                          </a>
                        </li>
                        <li>
                          <a
                            href="javascript:void(0)"
                            data-bs-toggle="modal"
                            data-bs-target="#quick-view"
                          >
                            <!-- <i data-feather="eye"></i> -->
                            <vue-feather type="eye"></vue-feather>
                          </a>
                        </li>
                        <li>
                          <a href="compare.html">
                            <!-- <i data-feather="refresh-cw"></i> -->
                            <vue-feather type="refresh-cw"></vue-feather>
                          </a>
                        </li>
                        <li>
                          <a href="wishlist.html" class="wishlist">
                            <!-- <i data-feather="heart"></i> -->
                            <vue-feather type="heart"></vue-feather>
                          </a>
                        </li>
                      </ul>
                    </div>
                  </div>
                  <div class="product-details">
                    <div class="rating-details">
                      <span class="font-light grid-content">B&Y Jacket</span>
                      <ul class="rating mt-0">
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
                        <li>
                          <i class="fas fa-star"></i>
                        </li>
                      </ul>
                    </div>
                    <div class="main-price">
                      <a href="product-left-sidebar.html" class="font-default">
                        <h5>Slim Fit Plastic Coat</h5>
                      </a>
                      <div class="listing-content">
                        <span class="font-light">Regular Fit</span>
                        <p class="font-light">
                          Lorem ipsum, dolor sit amet consectetur adipisicing
                          elit. Sit, deserunt? Asperiores aliquam voluptatum
                          culpa aliquid ab ducimus eaque illum, quibusdam
                          reiciendis id ad consectetur quis, animi qui, minus
                          quidem eveniet! Dolorum magnam numquam, asperiores
                          accusantium architecto placeat quam officia, tempore
                          repellendus.
                        </p>
                      </div>
                      <h3 class="theme-color">$78.00</h3>
                      <button
                        onclick="location.href = 'cart.html';"
                        class="btn listing-content"
                      >
                        Add To Cart
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </vue-slick-carousel>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";
import VueFeather from "vue-feather";
export default {
  components: {
    VueFeather,
    "vue-slick-carousel": VueSlickCarousel,
  },
  data() {
    return {
      settings: {
        centerMode: true,
        // centerPadding: "20px",
        focusOnSelect: true,
        infinite: true,
        slidesToShow: 4,
        speed: 500,
        dots: true,
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 4,
              slidesToScroll: 4,
              infinite: true,
              dots: true,
            },
          },
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2,
              initialSlide: 2,
            },
          },
          {
            breakpoint: 480,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
            },
          },
        ],
      },
    };
  },
};
</script>

<style></style>
