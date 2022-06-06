<template>
  <div class="menu-right">
    <ul>
      <li>
        <div class="search-box">
          <vue-feather type="search"></vue-feather>
        </div>
      </li>
      <li class="onhover-dropdown">
        <div class="cart-media">
          <vue-feather type="user"></vue-feather>
        </div>
        <div class="onhover-div profile-dropdown">
          <ul>
            <li>
              <a href="log-in.html" class="d-block">Login</a>
            </li>
            <li>
              <a href="sign-up.html" class="d-block">Register</a>
            </li>
          </ul>
        </div>
      </li>
      <li class="onhover-dropdown wislist-dropdown">
        <div class="cart-media">
          <a href="wishlist.html">
            <vue-feather type="heart"></vue-feather>
            <span class="label label-theme rounded-pill">5</span>
          </a>
        </div>
        <div class="onhover-div">
          <a href="wishlist.html">
            <div class="wislist-empty">
              <i class="fab fa-gratipay"></i>
              <h6 class="mb-1">Your wislist empty !!</h6>
              <p class="font-light mb-0">explore more and shortlist items.</p>
            </div>
          </a>
        </div>
      </li>
      <li class="onhover-dropdown cart-dropdown" v-for="(list, index) in cartlist" :key="index">
        <button type="button" class="btn btn-solid-default btn-spacing">
          <vue-feather type="shopping-cart"></vue-feather>
          <span>${{ list.cartTotal }}</span>
        </button>
        <div class="onhover-div">
          <div class="cart-menu">
            <div class="cart-title">
              <h6>
                <vue-feather type="shopping-bag"></vue-feather>
                <span class="label label-theme rounded-pill">5</span>
              </h6>
              <span class="d-md-none d-block">
                <i class="fas fa-arrow-right back-cart"></i>
              </span>
            </div>
            <ul class="custom-scroll">
              <li v-for="(item, index) in list.items" :key="index">
                <div class="media">
                  <img :src="item.image" class="img-fluid" alt="no image" />
                  <div class="media-body">
                    <h6>{{ item.itemName }}</h6>
                    <div class="qty-with-price">
                      <span>${{ item.price }}</span>
                      <span>
                        <input type="number" class="form-control" :value="item.quantity" />
                      </span>
                    </div>
                  </div>
                  <button type="button" class="btn-close d-block d-md-none" aria-label="Close">
                    <i class="fas fa-times"></i>
                  </button>
                </div>
              </li>
            </ul>
          </div>
          <div class="cart-btn">
            <h6 class="cart-total"><span>Total:</span> $ 542.00</h6>
            <nuxt-link to="/page/cart" class="btn btn-solid-default btn-block" style="color: white">Proceed to payment
            </nuxt-link>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>
<script>
  import { mapState } from "vuex";
  import VueFeather from "vue-feather";
  export default {
    components: {
      VueFeather,
    },
    computed: {
      ...mapState({
        cartlist: (state) => state.cart.data,
      }),
    },
  };
</script>