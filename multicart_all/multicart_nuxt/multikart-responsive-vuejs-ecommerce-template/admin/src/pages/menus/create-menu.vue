<template>
  <div>
    <!-- Container-fluid starts-->
    <div class="container-fluid">
      <div class="page-header">
        <Breadcrumbs main="Menus" title="Create Menu" />
      </div>
      <div class="row">
        <div class="col-sm-12">
          <div class="card">
            <div class="card-header">
              <h5>Add Menu</h5>
            </div>
            <div class="card-body">
              <form class="needs-validation">
                <div class="form-group row">
                  <label for="validationCustom0" class="col-xl-3 col-md-4"
                    ><span>*</span>Menu Name</label
                  >
                  <input
                    class="form-control col-md-8"
                    id="validationCustom0"
                    type="text"
                    required=""
                  />
                </div>
                <div class="form-group row">
                  <label class="col-xl-3 col-md-4">Status</label>
                  <!-- <div class="checkbox checkbox-primary col-xl-9 col-md-8">
                    <input
                      id="checkbox-primary-2"
                      type="checkbox"
                      data-original-title=""
                      title=""
                    />
                    <label for="checkbox-primary-2">Enable the Menu</label>
                  </div> -->
                  <label class="d-block" for="chk-ani">
                          <input
                            class="checkbox_animated"
                            id="chk-ani"
                            type="checkbox"
                          />
                          Enable the Menu
                  </label>
                </div>
                <button type="button" class="btn btn-primary d-block">
                  Save
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Container-fluid Ends-->
  </div>
</template>