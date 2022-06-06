<template>
  <footer class="footer-sm-space">
    <div class="main-footer">
      <div class="container">
        <div class="row gy-4">
          <div class="col-xl-3 col-lg-4 col-md-6">
            <div class="footer-contact">
              <brandLogo />
              <ul class="contact-lists">
                <li>
                  <span>
                    <b>phone:</b>
                    <span class="font-light"> + 185659635</span>
                  </span>
                </li>
                <li>
                  <span>
                    <b>Address:</b>
                    <span class="font-light">
                      1418 Riverwood Drive, Suite 3245 Cottonwood, CA 96052,
                      United States</span
                    >
                  </span>
                </li>
                <li>
                  <span>
                    <b>Email:</b>
                    <span class="font-light"> Voxo123@gmail.com</span>
                  </span>
                </li>
              </ul>
            </div>
          </div>
          <div
            class="col-xl-2 col-lg-2 col-md-4 col-sm-6"
            v-for="(headings, index) in links"
            :key="index"
          >
            <div class="footer-links">
              <div class="footer-title">
                <h3>{{ headings.title }}</h3>
              </div>
              <div class="footer-content">
                <ul>
                  <li v-for="(links, index) in headings.items" :key="index">
                    <nuxt-link :to="{ path: links.path }" class="font-dark">{{
                      links.title
                    }}</nuxt-link>
                  </li>
                </ul>
              </div>
            </div>
          </div>

          <slot></slot>
        </div>
      </div>
    </div>
    <subFooter />
  </footer>
</template>

<script>
import { mapState } from "vuex";
import brandLogo from "~/components/elements/brandLogo.vue";
import subFooter from "~/components/widgets/subFooter.vue";
export default {
  components: {
    brandLogo,
    subFooter,
  },
  computed: {
    ...mapState({
      links: (state) => state.links.data,
    }),
  },
};
</script>

<style></style>
