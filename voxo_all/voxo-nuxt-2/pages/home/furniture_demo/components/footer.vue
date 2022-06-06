<template>
  <footer1>
    <div class="col-xl-3 col-lg-4 col-sm-6 d-none d-sm-block">
      <div class="footer-newsletter">
        <h3>Let’s stay in touch</h3>
        <div class="form-newsletter">
          <div class="input-group mb-4">
            <input
              type="text"
              class="form-control color-4"
              placeholder="Your Email Address"
            />
            <span class="input-group-text" id="basic-addon4"
              ><i class="fas fa-arrow-right"></i
            ></span>
          </div>
          <p class="font-dark mb-0">
            Keep up to date with our latest news and special offers.
          </p>
        </div>
      </div>
    </div>
  </footer1>
</template>

<script>
import footer1 from "~/components/footers/footer-1.vue";

export default {
  components: {
    footer1,
  },
};
</script>

<style></style>
