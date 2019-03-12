import Vue from 'vue'

export default Vue.extend({
  template: `
          <span style="margin-left: 10px;">

              <font-awesome-icon :icon="imgIcon" size="2x" style="color: #9A2530;" />

          </span>
          `,
  data () {
    return {
      imgIcon: null,
      value: ''
    }
  },
  beforeMount() {
    switch (this.params.value) {
      case 'pdf':
        this.imgIcon = 'file-pdf'
        break

      case 'jpg':; case 'jpeg':; case 'png':; case 'gif':
        this.imgIcon = 'file-image'
        break

      case 'doc':; case 'docx':
        this.imgIcon = 'file-word'
        break

      case 'ppt':; case 'pptx':
        this.imgIcon = 'file-powerpoint'
        break

      case 'xls':; case 'xlsx':
        this.imgIcon = 'file-excel'
        break

      case 'mp4':; case 'mkv':; case 'avi':; case 'mov':; case 'wmv':;
      case 'mpeg':; case 'mpg':; case 'm4v':; case 'flv':
        this.imgIcon = 'file-video'
        break

      case 'zip':; case 'rar':
        this.imgIcon = 'file-archive'
        break

      default:
        this.imgIcon = 'file-alt'
      break;

    }
    this.value = this.params.value
  },
})
