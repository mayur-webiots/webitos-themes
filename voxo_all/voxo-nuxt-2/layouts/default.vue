<template>
  <div>
    <nuxt id="body-content" />
    <theme-settings />
    <div class="tap-to-top" v-scroll-to="'#body-content'">
      <a href="#home">
        <i class="fas fa-chevron-up"></i>
      </a>
    </div>
  </div>
</template>
<script>
import themeSettings from "~/components/elements/themeSettings.vue";
export default {
  components: {
    themeSettings,
  },
};
</script>
