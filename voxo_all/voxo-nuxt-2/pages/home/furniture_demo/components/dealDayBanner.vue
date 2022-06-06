<template>
  <section class="deal-section">
    <div class="container">
      <div class="row">
        <div class="col-md-12 px-0">
          <div class="discount-image-details-1">
            <div class="discount-images">
              <div class="theme-circle"></div>
              <img
                src="~assets/images/furniture-images/deal/1.png"
                class="img-fluid shoes-images"
                alt=""
              />
            </div>

            <div class="discunt-details mt-xl-0 mt-4">
              <div>
                <div class="heart-button">
                  <i data-feather="heart"></i>
                </div>

                <div class="discount-shop">
                  <h2 class="text-spacing">Shop Now</h2>
                  <h6>BUY ONE GET ONE FREE</h6>
                </div>

                <h5 class="mt-3">
                  Special Discount <span class="theme-color">70% OFF</span>
                </h5>
                <h2 class="my-2 deal-text">
                  Deal Of The Day <br />from
                  <span class="theme-color">$75</span>
                </h2>
                <div class="timer-style-2 my-2 justify-content-center d-flex">
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
                  onclick="location.href = 'shop-left-sidebar.html';"
                  type="button"
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
export default {
  data() {
    return {
      isLoaded: false,
      image: "/_nuxt/assets/images/fashion/banner/8.jpg",
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
