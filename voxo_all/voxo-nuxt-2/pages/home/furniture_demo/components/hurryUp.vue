<template>
    <section class="tab-section">
        <div class="container">
            <div class="row">
                <div class="col">
                    <div class="title-3 text-center">
                        <h2>Hurry up!</h2>
                        <h5 class="theme-color">Special Offer</h5>
                    </div>
                    <div class="tab-wrap">
                        <ul class="nav nav-tabs" id="myTab">
                            <li class="nav-item" v-for="(tab, index) in tabList" :key="index"
                                @click="setActive(tab.name)">
                                <button class="nav-link" :class="tab.active ? 'active' : ''" :id="tab.linkId"
                                    data-bs-toggle="tab" :data-bs-target="tab.target" type="button">
                                    {{ tab.displayTitle }}
                                </button>
                            </li>
                        </ul>
                        <div class="tab-content" id="myTabContent">
                            <hurryUpCard v-for="(tab, index) in tabList" :key="index" :tabId="tab.name"
                                :isActive="tab.active" />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<script>
    import hurryUpCard from "~/components/elements/cards/hurryUpCard.vue";
    import { mapState } from "vuex"
    export default {
        components: {
            hurryUpCard,
        },
        computed: {
            ...mapState({ tabList: (state) => state.tabList.data })
        },
        methods: {
            setActive(activeTab) {
                console.log("set active method is working", this.tabList);
                for (var i = 0; i < this.tabList.length; i++) {
                    if (activeTab === this.tabList[i].name) {
                        this.tabList[i].active = true;
                    } else {
                        this.tabList[i].active = false;
                    }
                }
            },
        },
    };
</script>

<style></style>