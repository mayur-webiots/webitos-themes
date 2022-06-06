<template>
  <header class="header-style-2" id="home">
    <div class="main-header navbar-searchbar">
      <div class="container-fluid-lg">
        <div class="row">
          <div class="col-lg-12">
            <div class="main-menu">
              <div class="menu-left">
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
                <categoryList />
              </div>
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
  </header>
</template>
<script>
import menuSideIcons from "../../widgets/menuSideIcons.vue";
import categoryList from "../../widgets/categoryList.vue";
import headerSearchBar from "../../widgets/headerSearchBar.vue";
import mainNavbar from "./components/mainNavbar.vue";
export default {
  components: {
    menuSideIcons,
    categoryList,
    headerSearchBar,
    mainNavbar,
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
