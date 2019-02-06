<template>
  <b-container>

    <br  />
    <b-card bg-variant="light">
      <b-form-file v-model="selFile" ref="form" placeholder="Upload a file..."></b-form-file>

      <b-button @click="submitFile">Submit</b-button>
    </b-card>

    <br />

    <b-card bg-variant="light">

    <b-button @click="getSelectedRows()">Show Details</b-button>
    <b-button @click="deleteFile()">Delete File</b-button>

    <hr />

    <ag-grid-vue style="width: 100%; height: 500px; border: 1px solid #e7e9ea; border-radius: 4px;"
                 class="ag-theme-material"
                 :row-height=60
                 :columnDefs="columnDefs"
                 :gridOptions="gridOptions"


                 :autoGroupColumnDef="autoGroupColumnDef"

                 :suppressRowClickSelection="true"
                 :groupSelectsChildren="true"
                 :debug="true"
                 :rowSelection="rowSelection"

                 :defaultColDef="{
                            enableValue: true,
                            sortable: true,
                            resizable: true,
                            filter: true
                            }"


                 :enableRangeSelection="true"
                 animateRows
                 :paginationAutoPageSize="true"
                 :pagination="true"

                 @gridReady="onGridReady"
                 :rowData="rowData">
    </ag-grid-vue>

  </b-card>

  </b-container>

</template>

<script>
import axios from 'axios'
import {AgGridVue} from "ag-grid-vue"

import { mapState } from 'vuex'
import { wait } from '../utils'

export default {
  data () {
    return {
      message: 'Welcome to Your Vue.js App!',
      selFile: null,
      columnDefs: null,
      autoGroupColumnDef: null,
      rowSelection: null,
      gridOptions: {}
    }
  },
  components: {
      AgGridVue
  },

  beforeMount() {
    this.columnDefs = [
        {
          headerName: 'Name',
          field: 'name',
          width: 250,
          // checkboxSelection: true,
          filterParams: { newRowsAction: "keep" },
          checkboxSelection: params => {
            return params.columnApi.getRowGroupColumns().length === 0;
          },
          headerCheckboxSelection: function(params) {
            return params.columnApi.getRowGroupColumns().length === 0;
          },
        },
        {headerName: 'Size', field: 'size', width: 75, filterParams: { newRowsAction: "keep" } },
        {headerName: 'Filetype', field: 'filetype', width: 75, filterParams: { newRowsAction: "keep" }},
        {headerName: 'Added', field: 'since_added', width: 100, sort: "asc", filterParams: { newRowsAction: "keep" } }

    ];

    this.autoGroupColumnDef = {
      headerName: "Group",
      width: 250,
      field: "name",
      valueGetter: params => {
        if (params.node.group) {
          return params.node.key;
        } else {
          return params.data[params.colDef.field];
        }
      },
      headerCheckboxSelection: true,
      cellRenderer: "agGroupCellRenderer",
      cellRendererParams: { checkbox: true }
    };

    this.rowSelection = "multiple";

  },
  mounted () {
    this.$store.dispatch('loadFiles')
    this.gridOApi = this.gridOptions.api;

  },
  computed: {
    ...mapState([
      'rowData'
    ])

  },
  methods: {

    onGridReady(params) {
      this.gridApi = params.api;
      this.columnApi = params.columnApi;
      params.api.sizeColumnsToFit();

    },
    getSelectedRows () {
      const selectedNodes = this.gridApi.getSelectedNodes();
      console.log(selectedNodes)
      // alert(`Selected Files:  ${selectedNodes}`)
      const selectedData = selectedNodes.map( node => node.data );
      const selectedDataStringPresentation = selectedData.map( node => node.name + ' ' + node.file_id).join(', ');
      alert(`Selected nodes: ${selectedDataStringPresentation}`);
    },
    fileUpload () {
      this.selFile = this.$refs.form.files[0]
    },
    submitFile () {
      // console.log(this.selFile)
      var vm = this
      const fd = new FormData()

      fd.append('file', vm.selFile)

      try {
        axios.post('api/files/', fd,
        { headers: {
          'Content-Type': 'multipart/form-data'
          // "X-CSRFTOKEN": 'csrfCookie',
          // 'Content-Disposition': 'attachment; filename=this.selFile.name'
           }
        })
          .then(res => {
            console.log(res)
            wait(1500) // DEV ONLY: wait for 1.5s
          })
          .then(res => {
            // this.gridOApi.refreshCells()
            this.$store.dispatch('loadFiles')
            console.log('Files loaded')
          })
      } catch (err) {
        console.error(`Error received from axios.post: ${JSON.stringify(err)}`);
      }



    },
    deleteFile () {
      const selectedNodes = this.gridApi.getSelectedNodes();
      // alert(`Selected Files:  ${selectedNodes}`)
      const selectedData = selectedNodes.map( node => node.data );
      const selectedDataStringPresentation = selectedData.map( node => node.file_id).join(', ');
      console.log(selectedDataStringPresentation)
      // axios.delete('api/files/' + result.id)
      // .then(response => {
      //   this.result.splice(id, 1)
      //   console.log(this.result);
      // });
    }

    // deleteNote: function (id) {
    //     swal({
    //         title: "Are you sure?",
    //         text: "You will not be able to recover this note!",
    //         type: "warning",
    //         showCancelButton: true,
    //         confirmButtonColor: "#DD6B55",
    //         confirmButtonText: "Yes, delete it!",
    //         closeOnConfirm: false
    //     },
    //     function(){
    //         axios.delete('/note/' + id)
    //             .then(response => swal("Deleted!", response.data.msg, "success"))
    //             .catch(error => console.log(error.response.data));
    //     });
    // }
  }
}
</script>

<style lang="scss">

$primary-color: #2196F3; // blue-500
$accent-color: green; // amber-A200

@import "~ag-grid-community/dist/styles/ag-grid.css";
@import "~ag-grid-community/dist/styles/ag-theme-balham.css";
@import "~ag-grid-community/dist/styles/ag-theme-bootstrap.css";
@import "~ag-grid-community/dist/styles/ag-theme-material.css";

.ag-theme-material {
  font-size: 16px;
}

.ag-root-wrapper-body.ag-layout-normal {
  border-radius: 4px;
}

// .ag-theme-material .ag-icon-checkbox-checked:empty {
//   // background-image: url(http://i.stack.imgur.com/S4p2R.png) no-repeat 80% 50%;
//   background-color: blue;
// }


/* Style buttons */
.btn {
  margin-top: 20px;
  background-color: DodgerBlue;
  border: none; /* Remove borders */
  color: white; /* White text */
  padding: 12px 16px; /* Some padding */
  font-size: 16px; /* Set a font size */
  cursor: pointer; /* Mouse pointer on hover */
}
/* Darker background on mouse-over */
.btn:hover {
  background-color: Gray;
}
</style>
