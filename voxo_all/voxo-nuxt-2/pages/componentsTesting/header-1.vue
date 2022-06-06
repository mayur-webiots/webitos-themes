<template>
  <!-- <div>hello this is fashion demo</div> -->
  <div>
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
                <nav>
                  <div class="main-navbar">
                    <div id="mainnav">
                      <div class="toggle-nav">
                        <i class="fa fa-bars sidebar-bar"></i>
                      </div>
                      <ul class="nav-menu">
                        <li class="back-btn d-xl-none">
                          <div class="close-btn">
                            Menu
                            <span class="mobile-back"
                              ><i class="fa fa-angle-left"></i>
                            </span>
                          </div>
                        </li>

                        <li
                          v-for="(menuItem, index) in menulist"
                          :key="index"
                          class="dropdown"
                          :class="getMenuClass(menuItem.title)"
                        >
                          <a
                            href="javascript:void(0)"
                            class="nav-link menu-title"
                          >
                            <div
                              v-if="menuItem.title == 'VOXO PLUS'"
                              class="gradient-title"
                            >
                              {{ menuItem.title }}
                            </div>
                            <p v-else>{{ menuItem.title }}</p>
                          </a>
                          <div
                            class="mega-menu-container menu-content"
                            v-if="menuItem.title == 'HOME'"
                          >
                            <div class="container-fluid">
                              <div class="row">
                                <div
                                  class="col mega-box"
                                  v-for="(
                                    childrenItem, index
                                  ) in menuItem.children"
                                  :key="index"
                                >
                                  <div class="link-section">
                                    <div class="opensubmegamenu">
                                      <ul>
                                        <li>
                                          <nuxt-link
                                            :to="{ path: childrenItem.path }"
                                          >
                                            <img
                                              :src="childrenItem.imagePath"
                                              class="img-fluid"
                                              alt="ss"
                                            />
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
                          <div
                            v-else-if="menuItem.title == 'VOXO PLUS'"
                            class="mega-menu-container poster-bg-image menu-content"
                          >
                            <div class="container-fluid">
                              <div class="row row-cols-5">
                                <div
                                  class="col mega-box"
                                  v-for="(
                                    childrenItem, index
                                  ) in menuItem.children"
                                  :key="index"
                                >
                                  <div
                                    class="link-section"
                                    v-for="(row, index) in childrenItem.rows"
                                    :key="index"
                                  >
                                    <div class="submenu-title">
                                      <h5>{{ row.title }}</h5>
                                    </div>
                                    <div
                                      class="submenu-content opensubmegamenu"
                                    >
                                      <ul class="list">
                                        <li
                                          v-for="(
                                            subChildren, index
                                          ) in row.children"
                                          :key="index"
                                        >
                                          <nuxt-link
                                            :to="{ path: subChildren.path }"
                                          >
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
                            <li
                              v-for="(childrenItem, index) in menuItem.children"
                              :key="index"
                            >
                              <nuxt-link :to="{ path: childrenItem.path }"
                                >{{ childrenItem.title
                                }}<span
                                  v-if="childrenItem.badge"
                                  :class="childrenItem.badgeClass"
                                  >{{ childrenItem.badge }}</span
                                ></nuxt-link
                              >
                            </li>
                          </ul>
                        </li>
                      </ul>
                    </div>
                  </div>
                </nav>
                <menuSideIcons />
                <div class="search-full">
                  <div class="input-group">
                    <span class="input-group-text">
                      <!-- <i data-feather="search" class="font-light"></i> -->
                      <vue-feather type="search"></vue-feather>
                    </span>
                    <input
                      type="text"
                      class="form-control search-type"
                      placeholder="Search here.."
                    />
                    <span class="input-group-text close-search">
                      <!-- <i data-feather="x" class="font-light"></i> -->
                      <vue-feather type="x"></vue-feather>
                    </span>
                  </div>
                  <div class="search-suggestion">
                    <ul class="custom-scroll">
                      <li>
                        <div class="product-cart media">
                          <img
                            src="~assets/images/electronics/product/1.jpg"
                            class="img-fluid"
                            alt=""
                          />
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
                          <img
                            src="~assets/images/electronics/product/5.jpg"
                            class="img-fluid"
                            alt=""
                          />
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
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
    <div v-for="(menuItem, index) in menulist" :key="index">
      {{ menuItem.title }}
      <div v-for="(childrenItem, index) in menuItem.children" :key="index">
        -{{ childrenItem.title }} classes are:
        {{ getMenuClass(menuItem.title) }}
        <h3>image is:</h3>
        <img :src="childrenItem.imagePath" alt="" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import VueFeather from "vue-feather";
import menuSideIcons from "./menuSideIcons.vue";
import categoryList from "./categoryList.vue";
export default {
  components: {
    VueFeather,
    menuSideIcons,
    categoryList,
  },
  methods: {
    getMenuClass(title) {
      if (title === "HOME") {
        return "mega-menu home-menu";
      } else if (title === "VOXO PLUS") {
        return "mega-menu ratio_40";
      }
    },
  },
  computed: {
    ...mapState({
      menulist: (state) => state.menu.data,
    }),
  },
  mounted() {
    console.log(this.menulist);
  },
};
</script>
