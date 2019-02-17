import Vue from 'vue'

export default Vue.extend({
  template: `
          <span style="margin-left: 5px;">

              <font-awesome-icon :icon="imgIcon" size="2x" />

          </span>
          `,
  data: function () {
    return {
      imgIcon: null,
      value: ''
    }
  },
  beforeMount() {
    // let array = ['file-pdf', 'file-image', 'file-word', 'file-powerpoint', 'file-excel', 'file-video', 'file-archive', 'file']
    switch (this.params.value) {
      case 'pdf': {
        this.imgIcon = 'file-pdf'
        break
      }
      case 'jpg' || 'jpeg' || 'png' || 'gif': {
        this.imgIcon = 'file-image'
        break
      }
      case 'doc' || 'docx': {
        this.imgIcon = 'file-word'
        break
      }
      case 'ppt' || 'pptx': {
        this.imgIcon = 'file-powerpoint'
        break
      }
      case 'xls' || 'xlsx': {
        this.imgIcon = 'file-excel'
        break
      }
      case 'mp4' || 'mkv' || 'avi' || 'mov' || 'wmv' || 'mpeg' || 'mpg' || 'm4v' || 'flv': {
        this.imgIcon = 'file-video'
        break
      }
      case 'zip' || 'rar': {
        this.imgIcon = 'file-archive'
        break
      }
      default: {
        this.imgIcon = 'file'
      break;
   }
    }
    this.value = this.params.value
  },
})
