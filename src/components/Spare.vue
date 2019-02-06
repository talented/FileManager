<template>
  <b-container>

    <br  />
    <b-card bg-variant="light">
      <b-form-file v-model="selFile" ref="form" placeholder="Upload a file..."></b-form-file>

      <b-button @click="submitFile">Submit</b-button>
    </b-card>

    <hr />

    <!-- <b-button><i class="fa fa-folder"></i> Upload -->

    <!-- <label class="sr-only" for="inlineFormInputName2">File Upload</label>
    <b-form-file v-model="selFile" :state="Boolean(selFile)" placeholder="Choose a file..." enctype="multipart/form-data"></b-form-file>
      <div class="mt-3">Selected file: {{file && file.name}}</div>
      <input type="file" ref="form" v-on:change="fileUpload()"/>
      <b-button v-on:click="submitFile()">Enter</b-button> -->



  </b-container>

</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      message: 'Welcome to Your Vue.js App!',
      selFile: null
    }
  },
  methods: {
    fileUpload () {
      this.selFile = this.$refs.form.files[0]
    },
    submitFile () {
      console.log(this.selFile)
      var vm = this
      const fd = new FormData()

      fd.append('file', vm.selFile)

      try {
        axios.post('fileupload/', fd,
        { headers: {
          'Content-Type': 'multipart/form-data'
          // "X-CSRFTOKEN": 'csrfCookie',
          // 'Content-Disposition': 'attachment; filename=this.selFile.name'
           }
        })
          .then(res => {
            console.log(res)
          })
      } catch (err) {
        console.error(`Error received from axios.post: ${JSON.stringify(err)}`);
      }
    }
  }
}
</script>

<style lang="css">

/* Style buttons */
.btn {
  margin-top: 20px;
  /* background-color: DodgerBlue; /* Blue background */ */
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
