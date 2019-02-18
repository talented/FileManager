<template>
  <b-container>

    <br  />
    <b-card bg-variant="light">
      <b-form-file v-model="selFile" ref="form" placeholder="Upload a file..."></b-form-file>

      <b-button variant="primary" @click="submitFile">Submit</b-button>
    </b-card>

    <br />

    <b-card bg-variant="light">

    <b-button variant="danger" @click="deleteFile()">Delete Selected File(s)</b-button>
    <b-button variant="warning" @click="getSelectedRows()">Show Details</b-button>

    <hr />

    <ag-grid-vue style="width: 100%; height: 500px; border: 1px solid #e7e9ea; border-radius: 4px;"
                 class="ag-theme-material"
                 :row-height=60
                 :columnDefs="columnDefs"
                 :gridOptions="gridOptions"


                 :autoGroupColumnDef="autoGroupColumnDef"
                 :frameworkComponents="frameworkComponents"
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
                 @rowClicked = "onRowClicked"
                 :paginationAutoPageSize="true"
                 :pagination="true"

                 @gridReady="onGridReady"
                 :rowData="rowData">
    </ag-grid-vue>

  </b-card>


  <!-- Modal Component -->
  <b-modal v-if="mShow" v-model="modal" @ok="handleOk" @cancel="$emit('close')">
      Selected file(s) will be deleted?
  </b-modal>

  </b-container>

</template>

<script>
import axios from 'axios'
import {AgGridVue} from "ag-grid-vue"
import filetypeCellRenderer from "../filetypeCellRenderer.js"

import { mapState } from 'vuex'
import { wait, sizeFormatter, dateFormatter } from '../utils'


// import ConfirmationModal from './ConfirmationModal'

export default {
  data () {
    return {
      message: 'Welcome to Your Vue.js App!',
      data: {dirname: '.', root: '.'},
      selFile: null,
      columnDefs: null,
      autoGroupColumnDef: null,
      frameworkComponents: null,
      rowSelection: null,
      gridOptions: {},
      modal: false,
      mShow: false,
      result_id: null
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
          width: 305,
          // checkboxSelection: true,
          filterParams: { newRowsAction: "keep" },
          checkboxSelection: params => {
            return params.columnApi.getRowGroupColumns().length === 0;
          },
          headerCheckboxSelection: function(params) {
            return params.columnApi.getRowGroupColumns().length === 0;
          },
        },
        {
          headerName: 'Filetype',
          field: 'filetype',
          width: 55,
          cellRenderer: 'filetypeCellRenderer',
          filterParams: { newRowsAction: "keep" },
        },
        {
          headerName: 'Size',
          field: 'size',
          valueFormatter: sizeFormatter,
          width: 60,
          filterParams: { newRowsAction: "keep" }
        },
        {
          headerName: 'Added',
          field: 'since_added',
          width: 80,
          sort: 'desc',
          valueFormatter: dateFormatter
          // comparator: dateComparator
        }
        // {headerName: 'Added', field: 'since_added', width: 100, sort: "asc", filterParams: { newRowsAction: "keep" } }
    ]

    this.frameworkComponents = {
      filetypeCellRenderer: filetypeCellRenderer
    }

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
      params.api.setRowData();
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

      var config = {
        onUploadProgress (e) {
          var percentCompleted = Math.round( (e.loaded * 5000) / e.total );
          // console.log("waiting")
        }
      };

      try {
        axios.post('api/files/', fd, config,
        { headers: {
          'Content-Type': 'multipart/form-data'
          // "X-CSRFTOKEN": 'csrfCookie',
          // 'Content-Disposition': 'attachment; filename=this.selFile.name'
           }
        })
          .then(res => {
            // console.log(res)
            this.$store.dispatch('loadFiles')
            // wait(5000) // DEV ONLY: wait for 1.5s
          })
          .then( () => {
            // this.gridOApi.refreshCells()
            // console.log('Files loaded')
            // this.gridApi.setRowData();
          })
      } catch (err) {
        console.error(`Error received from axios.post: ${JSON.stringify(err)}`);
      }



    },
    // select_file (selectedNodes) {
    //   // const selectedNodes =
    //   // alert(`Selected Files:  ${selectedNodes}`)
    //   const selectedData = selectedNodes.map( node => node.data );
    //   // const result_id = selectedData.map( node => node.file_id).join(', ');
    //   return selectedData.map( node => node.file_id)
    //   // return result_id
    // },

    deleteFile () {
      const selectedNodes = this.gridApi.getSelectedNodes()
      if (selectedNodes.length > 0) {
        const selectedData = selectedNodes.map( node => node.data );
        // const result_id = selectedData.map( node => node.file_id).join(', ');
        const result_id = selectedData.map( node => node.file_id)
        console.log(result_id)
        this.result_id = result_id
        this.mShow = true
        this.modal = true
      }
      // if (confirm (`You are deleting id: ${result_id}\nare you sure?`))
    },
    handleOk () {
        axios.delete('api/files/' + this.result_id)
          .then(response => {
            console.log(response)
            // this.result.splice(id, 1)
            // alert(`This will be deleted? ${result_id}`)
            this.$store.dispatch('loadFiles')
            // console.log(this.result);
        })
        .catch(error => {
          console.log(error)
        })
        // this.modalShow = false
        this.mShow = false
    },
    onRowClicked(event) {
      let file_id = event.node.data.file_id
      let filename = event.node.data.name
      console.log(file_id)
      axios({
        url: `media/${filename}`,
        method: 'GET',
        responseType: 'blob',
      })
      .then ((res) => {
        const url = window.URL.createObjectURL(new Blob([res.data]))
        const link = document.createElement('a')
        link.href = url
        link.setAttribute('download', filename)
        document.body.appendChild(link)
        link.click()
      })

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

// function sizeFormatter(params) {
//   return Math.floor(params.value).toString() + ' TB'
// }

function sizeComparator(d1, d2) {
  console.log(params)
  return params
}

function dateComparator(date1, date2) {
  console.log(date1, date2)
  var date1Number = monthToComparableNumber(date1);
  var date2Number = monthToComparableNumber(date2);
  if (date1Number === null && date2Number === null) {
    return 0;
  }
  if (date1Number === null) {
    return -1;
  }
  if (date2Number === null) {
    return 1;
  }
  return date1Number - date2Number;
}

function monthToComparableNumber(date) {
  if (date === undefined || date === null || date.length !== 10) {
    return null;
  }
  var yearNumber = date.substring(6, 10);
  var monthNumber = date.substring(3, 5);
  var dayNumber = date.substring(0, 2);
  var result = yearNumber * 10000 + monthNumber * 100 + dayNumber;
  return result;
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
  font-family: Questrial, Roboto;
}

.ag-theme-material .ag-row, .ag-theme-material .ag-row:not(.ag-row-first) {
  padding-top: 7px;
}

.ag-theme-material .ag-icon-checkbox-checked:empty {
  background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAC2ElEQVR42tWaPWhTURTHgzZ+QkWk0KWLZKiERPJNaCtBqYODQyRFbP3oaEdxfGPH0klwEXGwg+AQ3Sy4iC5VwclJBzEFKa04tKSV1vj/Q+t9fb70vCZe33mBQ5J3zr33/7s59917c1+s1Wr9ZZlMppzL5ZxsNvsM74uwVki2uK3BoSY/rbu+IPBEPp9/yMIajdqo0RcAziE4GwxUbg1q3QVAqjbiNxD8Fu/1MIxtU4MfBDX/AfBJm1XYVCKROEx/mEYN1EJN3nSif2fAesUP0qnJqMkLQe10OB6AKRbQaNTm0erEeJty57yQNgrSyYwJao+57/McNCH2bhztX4Vl9oqjRvc8EfP8JPUwxFcqlSNo+51Lx1wqlTrZBrTu1qwBgGk86zcLwy5qB6D4EbS71WbSasIG1QKk0+njaPOzsHy4ohWAbd8Xlg0rxWLxlEoA9OyoIJ52Td8YMGuvr3uJx9h4ylitAI+Enl/CMqFPIwBT57Ignr1fZaw6AA5ItPFNAHjMWI0AbOuJtIXkDKwSAGkxFmDLeImx6gAKhUI/6l4WAB4wViUAeva5IP5LqVTqtQpQLpePIg0mYdVarXZwH3l/UxD/C7fMC4y1BsCBBd9790YimUweCpA6A4j/IeT9PcZaA+Cs6dlEyBCm7LzQ+59gx6wCQOgb4w8OAf9tQfwWbJix1gCQm+eMLzAEU+c0fKtC2RnG2gbow7X1/UDgdQDXXgllPnIbaRfApNA4rm8GhcDnO0LsZgEv1m0fwEBM7Gz7BHsJawqg06zTKoAE0YV9gMWtAggz6vUuIH5iTJ1lPdYBBIgbHUI4LB8SgAwh5P0C7jo9SgDMGicgRBMAZ1hGD4AZ2LcCQNxlrC6A4BCvObHpBTAQkz4Qa7ieoN8mwD/7e51retTxYruu7xB/vnvB8t/rnR1wyHuA+P864Ij8EVPkD/mifcwa/YPu6D9qEP2HPSL/uM1vzeJjU/DsstoAAAAASUVORK5CYII=');
  // background-color: #dc3545;
}

// .ag-theme-material .ag-icon-checkbox-checked {
//   background: none;
// }

.ag-cell-focus,.ag-cell-no-focus{
  border:none !important;
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
  // background-color: DodgerBlue;
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
