<template>
  <div>
      <!-- Container-fluid starts-->
      <div class="container-fluid">
        <div class="page-header">
          <Breadcrumbs main="Physical" title="Product List" />
        </div>
      </div>
      <!-- Container-fluid Ends-->

      <!-- Container-fluid starts-->
      <div class="container-fluid">
        <div class="row products-admin ratio_asos">
          <div
            class="col-xl-3 col-sm-6"
            v-for="(product, index) in products"
            :key="index"
          >
            <div class="card">
              <div class="card-body product-box ">
                <div class="img-wrapper">
                  <div class="front">
                    <a href="#">
                      <img
                        :src="getImgUrl(product.image)"
                        class="img-fluid blur-up lazyload bg-img"
                        alt=""
                      />
                    </a>
                    <div class="product-hover">
                      <ul>
                        <li>
                          <button
                            class="btn"
                            type="button"
                            data-original-title=""
                            title=""
                          >
                            <i class="ti-pencil-alt">
                              <feather type="edit"></feather>
                            </i>
                          </button>
                        </li>
                        <li>
                          <button
                            class="btn"
                            type="button"
                            data-toggle="modal"
                            data-target="#exampleModalCenter"
                            data-original-title=""
                            title=""
                          >
                            <i class="ti-trash">
                              <feather type="trash-2"></feather>
                            </i>
                          </button>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div class="product-detail">
                  <div class="rating">
                  <StarRating
                    :show-rating="false"
                    :star-size="15"
                    :rounded-corners="true"
                    :padding="4"
                    :rating="2"
                    :read-only="true"
                  ></StarRating>
                   
                  </div>
                  <a href="#">
                    <h6>{{ product.name }}</h6>
                  </a>
                  <h4>
                    {{ product.price }} <del>{{ product.salePrice }}</del>
                  </h4>
                  <ul class="color-variant">
                    <li class="bg-light0"></li>
                    <li class="bg-light1"></li>
                    <li class="bg-light2"></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Container-fluid Ends-->
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  created() {
    this.$store.dispatch("product/getProductList");
  },
  computed: {
    ...mapGetters({
      products: "product/getProductList"
    })
  },
  methods: {
      getImgUrl(path) {
      return require("@/assets/images/pro3/" + path);
    },
  }
};
</script>

<style>

</style>