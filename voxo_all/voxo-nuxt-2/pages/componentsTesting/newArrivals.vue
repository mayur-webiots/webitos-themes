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
              <div class="product-box">
                <div class="img-wrapper">
                  <div class="front">
                    <a href="product-left-sidebar.html">
                      <img
                        src="~assets/images/fashion/product/front/5.jpg"
                        class="bg-img"
                        alt=""
                      />
                    </a>
                  </div>
                  <div class="back">
                    <a href="product-left-sidebar.html">
                      <img
                        src="~assets/images/fashion/product/back/5.jpg"
                        class="bg-img"
                        alt=""
                      />
                    </a>
                  </div>
                  <div class="label-block">
                    <span class="label label-black">New</span>
                    <span class="label label-theme">50% Off</span>
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
                          <i data-feather="eye"></i>
                          <vue-feather type="eye"></vue-feather>
                        </a>
                      </li>
                      <li>
                        <a href="compare.html">
                          <i data-feather="refresh-cw"></i>
                          <vue-feather type="refresh-cw"></vue-feather>
                        </a>
                      </li>
                      <li>
                        <a href="wishlist.html" class="wishlist">
                          <i data-feather="heart"></i>
                          <vue-feather type="heart"></vue-feather>
                        </a>
                      </li>
                    </ul>
                  </div>
                </div>
                <div class="product-details">
                  <div class="rating-details">
                    <span class="font-light grid-content">Jacket</span>
                    <ul class="rating mt-0">
                      <li>
                        <i class="fas fa-star theme-color"></i>
                      </li>
                      <li>
                        <i class="fas fa-star theme-color"></i>
                      </li>
                      <li>
                        <i class="fas fa-star theme-color"></i>
                      </li>
                      <li>
                        <i class="fas fa-star theme-color"></i>
                      </li>
                      <li>
                        <i class="fas fa-star"></i>
                      </li>
                    </ul>
                  </div>
                  <div class="main-price">
                    <a href="product-left-sidebar.html" class="font-default">
                      <h5>Full Jacket Ladies</h5>
                    </a>
                    <div class="listing-content">
                      <span class="font-light">Jacket</span>
                      <p class="font-light">
                        Lorem ipsum, dolor sit amet consectetur adipisicing
                        elit. Sit, deserunt? Asperiores aliquam voluptatum culpa
                        aliquid ab ducimus eaque illum, quibusdam reiciendis id
                        ad consectetur quis, animi qui, minus quidem eveniet!
                        Dolorum magnam numquam, asperiores accusantium
                        architecto placeat quam officia, tempore repellendus.
                      </p>
                    </div>
                    <h3 class="theme-color">$40.00</h3>
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
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import VueFeather from "vue-feather";
export default {
  components: {
    VueFeather,
  },
};
</script>

<style></style>
