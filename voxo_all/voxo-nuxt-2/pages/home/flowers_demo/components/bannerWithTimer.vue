<template>
  <section class="deal-section">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <div class="discount-image-details-2">
            <div class="discount-images">
              <img
                src="~assets/images/flower/offer-1/2.png"
                class="img-fluid flower-images-1"
                alt=""
              />
              <img
                src="~assets/images/flower/offer-1/1.png"
                class="img-fluid flower-images-2"
                alt=""
              />
            </div>

            <div class="discunt-details mt-lg-0 mt-4">
              <div>
                <div class="heart-button heart-button-light">
                  <i data-feather="heart"></i>
                  <vue-feather type="heart"></vue-feather>
                </div>

                <div class="discount-shop">
                  <h2>Shop Now</h2>
                  <h6>BUY ONE GET ONE FREE</h6>
                </div>

                <h5 class="mt-3">
                  Special Discount <span class="theme-color">70% OFF</span>
                </h5>
                <h2 class="mt-3 deal-text">
                  Deal Of The Day <br />from
                  <span class="theme-color">$75</span>
                </h2>
                <div
                  class="timer-style-2 mt-xl-1 my-2 justify-content-center d-flex"
                >
                  <ul>
                    <li>
                      <div class="counter">
                        <div>
                          <h2 id="days1" class="theme-color">{{ days }}</h2>
                          Days
                        </div>
                      </div>
                    </li>
                    <li>
                      <div class="counter">
                        <div>
                          <h2 id="hours1" class="theme-color">{{ hours }}</h2>
                          Hour
                        </div>
                      </div>
                    </li>
                    <li>
                      <div class="counter">
                        <div>
                          <h2 id="minutes1" class="theme-color">
                            {{ minutes }}
                          </h2>
                          Min
                        </div>
                      </div>
                    </li>
                    <li>
                      <div class="counter">
                        <div>
                          <h2 id="seconds1" class="theme-color">
                            {{ seconds }}
                          </h2>
                          Sec
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
                <button
                  type="button"
                  onclick="location.href='shop-left-sidebar.html';"
                  class="btn default-light-theme default-theme mt-2"
                >
                  Shop Now
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import VueFeather from "vue-feather";
export default {
  components: {
    VueFeather,
  },
  data() {
    return {
      isLoaded: false,
      days: 0,
      hours: 0,
      minutes: 0,
      seconds: 0,
    };
  },
  created() {
    this.isLoaded = true;
  },
  mounted() {
    var second = 1000,
      minute = second * 60,
      hour = minute * 60,
      day = hour * 24;
    var countDown = new Date("Aug 21, 2023 00:00:00").getTime();
    setInterval(() => {
      var now = new Date().getTime();
      this.days = Math.floor((countDown - now) / day);
      this.hours = Math.floor(((countDown - now) % day) / hour);
      this.minutes = Math.floor(((countDown - now) % hour) / minute);
      this.seconds = Math.floor(((countDown - now) % minute) / second);
    }, second);
  },
};
</script>

<style></style>
