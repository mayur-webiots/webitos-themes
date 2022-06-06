<template>
  <div class="search-full" id="suggestions" :class="isopen ? 'open' : 'close'">
    <div class="input-group">
      <span class="input-group-text">
        <vue-feather type="search"></vue-feather>
      </span>
      <input type="text" class="form-control search-type" placeholder="Search here.." @click="showSuggestions" />
      <span class="input-group-text close-search" @click="closeSearchBar">
        <vue-feather type="x"></vue-feather>
      </span>
    </div>
    <div class="search-suggestion">
      <ul class="custom-scroll">
        <li>
          <div class="product-cart media">
            <img src="~assets/images/electronics/product/1.jpg" class="img-fluid" alt="" />
            <div class="media-body">
              <a href="javascript:void(0)">
                <h6 class="mb-1">New Smart Watch 4 ERT2</h6>
              </a>
              <ul class="rating p-0">
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
                <li>
                  <i class="fas fa-star"></i>
                </li>
              </ul>
              <p class="mb-0 mt-1">$28.00</p>
            </div>
          </div>
        </li>
        <li>
          <div class="product-cart media">
            <img src="~assets/images/electronics/product/5.jpg" class="img-fluid" alt="" />
            <div class="media-body">
              <a href="javascript:void(0)">
                <h6 class="mb-1">Powermatic 900 W Juicer</h6>
              </a>
              <ul class="rating m-0 p-0">
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
                  <i class="fas fa-star theme-color"></i>
                </li>
              </ul>
              <p class="mb-0 mt-1">$35.00</p>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>
<script>
  import VueFeather from "vue-feather";
  export default {
    props: ["isopen"],
    data() {
      return {
        suggestions: false,
      };
    },
    components: { VueFeather },
    methods: {
      closeSearchBar() {
        this.$emit("closeSearchBar", false);
      },
      showSuggestions() {
        this.suggestions = true;
        document.getElementById("suggestions").classList.add("show");
      },
    },
  };
</script>

<style></style>