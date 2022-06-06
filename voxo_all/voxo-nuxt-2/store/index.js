import Vue from "vue";
import Vuex from "vuex";
import menu from "./modules/menu";
import cart from "./modules/cart";
import links from "./modules/footerLinks";
import categoryMenu from "./modules/categoryMenu";
import arrivalCards from "./modules/arrivalCards";
import popularCards from "./modules/popularCards";
import tabList from "./modules/tabList";
Vue.use(Vuex);
const createStore = () => {
  return new Vuex.Store({
    modules: {
      menu,
      cart,
      links,
      categoryMenu,
      arrivalCards,
      popularCards,
      tabList,
    },
  });
};
export default createStore;
