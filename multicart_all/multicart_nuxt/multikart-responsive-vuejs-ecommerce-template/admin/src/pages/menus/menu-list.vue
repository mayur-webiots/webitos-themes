<template>
  <div>
    <div class="container-fluid">
      <div class="page-header">
        <Breadcrumbs main="Menus" title="Menu Lists" />
      </div>
    </div>
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-12">
          <div class="card">
            <div class="card-header">
              <h5>Menu List</h5>
            </div>
            <div class="card-body">
              <div class="table-responsive datatable-vue">
                <div>
                  <b-modal id="modal-1" title="Confirmation">
                    <p class="my-4">Are you sure!</p>
                  </b-modal>
                </div>

                <b-table
                  class="text-center table-bordered"
                  striped
                  hover
                  head-variant="light"
                  show-empty
                  stacked="md"
                  :items="items"
                  :fields="tablefields"
                  :filter="filter"
                  :current-page="currentPage"
                  :per-page="perPage"
                  @filtered="onFiltered"
                  @row-selected="rowSelected"
                >
                  <template v-slot:head(delete)>
                    <b-button
                      variant="danger"
                      :disabled="selectedRows.length === 0"
                      @click="showMsgBoxTwo"
                      >Delete</b-button
                    >
                  </template>
                  <template v-slot:cell(delete)="{ item, field: { key } }">
                    <b-checkbox
                      v-model="item[key]"
                      @change="deleteSelected(item)"
                    ></b-checkbox>
                  </template>
                  <template #cell(status)="field">
                    <statusIcon :field="field"></statusIcon>
                  </template>
                </b-table>
              </div>
              <b-col md="12" class="my-1 p-0 pagination-justify">
                <b-pagination
                  v-model="currentPage"
                  :total-rows="totalRows"
                  :per-page="perPage"
                  aria-controls="my-table"
                  class="mt-4"
                ></b-pagination>
              </b-col>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import statusIcon from "../../components/featherIcons/status-icon.vue";

export default {
  components: { statusIcon },
  data() {
    return {
      modes: ["multi", "single", "range"],
      tablefields: [
        { key: "delete" },
        { key: "name", label: "Name", sortable: false },
        { key: "status", label: "Status", sortable: false },
        { key: "createdOn", label: "createdOn", sortable: false }
      ],

      filter: null,
      totalRows: 1,
      currentPage: 1,
      perPage: 10,
      pageOptions: [5, 10, 15],
      selectMode: "multi",
      selected:[]
    };
  },
  created() {
    this.$store.dispatch("pages/getMenus");
  },

  mounted() {
    // Set the initial number of items
    this.totalRows = this.items.length;
  },
  computed: {
    ...mapGetters({
      items: "pages/getMenus"
    }),
    selectedRows() {
      return this.items.filter(item => item.delete);
    },
    sortOptions() {
      // Create an options list from our fields
      return this.tablefields
        .filter(f => f.sortable)
        .map(f => {
          return { text: f.label, value: f.key };
        });
    }
  },
  methods: {
    deleteSelected(item) {
      let objIndex = this.selected.findIndex((obj => obj.id == item.id));
      if (objIndex > -1) {
        this.selected.splice(objIndex, 1);
      } else {
        this.selected.push(item)
      }
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    rowSelected(item) {
      this.selected = item;
    },
    deleteRow() {
      for( var i=this.items.length - 1; i>=0; i--){
        for( var j=0; j<this.selected.length; j++){
          if(this.items[i] && (this.items[i].id === this.selected[j].id)){
            this.items.splice(i, 1);
          }
        }
      }
    },
    deleteBatchRow() {
      for (var i = 0; i < this.selected.length; i++) {
        if (this.items[i].id == this.selected[i].id) {
          this.items.splice(this.items[i], 1);
        }
      }
    },
    showMsgBoxTwo() {
        this.$bvModal.msgBoxConfirm('Are you sure!', {
          title: 'Confirmation',
          size: 'md',
          buttonSize: 'sm',
          okVariant: 'primary',
          okTitle: 'YES',
          cancelTitle: 'CANCLE',
          footerClass: 'p-2',
          hideHeaderClose: false,
          // centered: true
        })
          .then(value => {
            this.deleteRow();
            this.selected = [];
          })
          .catch(err => {
            // An error occurred
          })
      }
  }
};
</script>

<style lang="scss" scoped>
table.text-center * {
  text-align: center;
}
</style>