<template>
  <nav class="navigationbar">
    <div class="main-navbar">
      <div id="mainnav">
        <div class="toggle-nav ms-sm-3 ms-0" @click="mobileNav">
          <i class="fa fa-bars sidebar-bar"></i>
        </div>
        <ul class="nav-menu" :style="{ right: openMobileNav ? '0px' : '-410px' }">
          <li class="back-btn d-xl-none" @click="closeMobileNav">
            <div class="close-btn">
              Menu back<span>
                <i class="fa fa-angle-left"></i>
              </span>
            </div>
          </li>

          <li v-for="(menuItem, index) in menulist" :key="index" class="dropdown" :class="getMenuClass(menuItem.title)">
            <a href="javascript:void(0)" class="nav-link menu-title">
              <div v-if="menuItem.title == 'VOXO PLUS'" class="gradient-title">
                {{ menuItem.title }}
              </div>
              <p v-else>{{ menuItem.title }}</p>
            </a>
            <div class="mega-menu-container menu-content" v-if="menuItem.title == 'HOME'">
              <div class="container-fluid">
                <div class="row">
                  <div class="col mega-box" v-for="(childrenItem, index) in menuItem.children" :key="index">
                    <div class="link-section">
                      <div class="opensubmegamenu">
                        <ul>
                          <li>
                            <nuxt-link :to="{ path: childrenItem.path }">
                              <img :src="childrenItem.imagePath" class="img-fluid" alt="ss" />
                            </nuxt-link>
                          </li>
                        </ul>
                      </div>

                      <div class="megamenu-image-title pb-0">
                        <h5 class="mb-0">
                          {{ childrenItem.title }}
                        </h5>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div v-else-if="menuItem.title == 'VOXO PLUS'" class="mega-menu-container poster-bg-image menu-content">
              <div class="container-fluid">
                <div class="row row-cols-5">
                  <div class="col mega-box" v-for="(childrenItem, index) in menuItem.children" :key="index">
                    <div class="link-section" v-for="(row, index) in childrenItem.rows" :key="index">
                      <div class="submenu-title">
                        <h5>{{ row.title }}</h5>
                      </div>
                      <div class="submenu-content opensubmegamenu">
                        <ul class="list">
                          <li v-for="(subChildren, index) in row.children" :key="index">
                            <nuxt-link :to="{ path: subChildren.path }">
                              {{ subChildren.title }}
                            </nuxt-link>
                          </li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <ul v-else class="nav-submenu menu-content">
              <li v-for="(childrenItem, index) in menuItem.children" :key="index">
                <nuxt-link :to="{ path: childrenItem.path }">{{ childrenItem.title }}
                  <span v-if="childrenItem.badge" :class="childrenItem.badgeClass">{{ childrenItem.badge }}</span>
                </nuxt-link>
              </li>
            </ul>
          </li>
          <li class="mobile-poster d-flex d-xl-none" :style="{ right: openMobileNav ? '0px' : '-410px' }">
            <img src="~assets/images/pwa.png" class="img-fluid" alt="" />
            <div class="mobile-contain">
              <h5>Enjoy app-like experience</h5>
              <p class="font-light">
                With this Screen option you can use Website like an App.
              </p>
              <a href="javascript:void(0)" id="installApp" class="btn btn-solid-default btn-spacing w-100">ADD TO
                HOMESCREEN</a>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
  import { mapState } from "vuex";

  export default {
    data() {
      return {
        openMobileNav: false,
      };
    },
    computed: {
      ...mapState({
        menulist: (state) => state.menu.data,
      }),
    },
    methods: {
      getMenuClass(title) {
        if (title === "HOME") {
          return "mega-menu home-menu";
        } else if (title === "VOXO PLUS") {
          return "mega-menu ratio_40";
        }
      },
      mobileNav() {
        this.openMobileNav = true;
      },
      closeMobileNav() {
        this.openMobileNav = false;
      },
    },
  };
</script>

<style></style>