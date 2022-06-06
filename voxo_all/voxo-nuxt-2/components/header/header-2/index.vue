<template>
  <header id="home">
    <div class="header-style-3">
      <div class="main-header navbar-searchbar">
        <div class="container-fluid-lg">
          <div class="row">
            <div class="col-lg-12">
              <div class="main-menu common-menu">
                <div class="top-header top-comman-header text-center ms-0">
                  <div class="brand-logo">
                    <a href="index.html">
                      <svg class="svg-icon">
                        <use
                          class="fill-color"
                          xlink:href="~assets/svg/icons.svg#logo"
                        ></use>
                      </svg>
                      <img
                        src="~assets/images/logo.png"
                        class="img-fluid"
                        alt="logo"
                      />
                    </a>
                  </div>
                </div>
                <category-menu />
                <mainNavbar />
                <menuSideIcons @openSearchBar="openSearchBar($event)" />
                <headerSearchBar
                  :isopen="this.searchBarIsOpen"
                  @closeSearchBar="closeSearchBar($event)"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>
<script>
import mainNavbar from "./components/mainNavbar.vue";
import categoryMenu from "./components/categoryMenu.vue";
import menuSideIcons from "~/components/widgets/menuSideIcons.vue";
import headerSearchBar from "~/components/widgets/headerSearchBar.vue";
export default {
  components: {
    mainNavbar,
    categoryMenu,
    menuSideIcons,
    headerSearchBar,
  },
  data() {
    return {
      searchBarIsOpen: false,
    };
  },
  methods: {
    openSearchBar(changeStatus) {
      this.searchBarIsOpen = changeStatus;
    },
    closeSearchBar(changeStatus) {
      this.searchBarIsOpen = changeStatus;
    },
  },
};
</script>

<style lang="scss">
@import "~assets/scss/demo5.scss";
</style>
