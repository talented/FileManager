// utils.js
import moment from 'moment'

function sizeFormatter(params) {
  let size = params.value
  // #2**10 = 1024
  const power = 2**10
  let n = 0
  let powerN = {0 : 'B', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
  while (size > power) {
      size /=  power
      n += 1
  }
  size = Math.round(size * 10) / 10

  return size.toString() + ' ' + powerN[n]
}

function dateFormatter(params) {
  let timestamp = params.value
  let date = new Date(timestamp)
  let formattedTime = moment(date).fromNow()
  return formattedTime
}

export { sizeFormatter, dateFormatter }

// utils to delay promise
// wait(ms) {
//   return (x) {
//     console.log("will be waiting")
//     return new Promise(resolve => setTimeout(() => resolve(x), ms));
//   };
// }

// function secondsToHMS(secs) {
//   function z(n){ return (n<10?'0':'') + n }
//   let sign = secs < 0? '-':''
//   secs = Math.abs(secs)
//   return sign + z(secs/3600 |0) + ':' + z((secs%3600) / 60 |0) + ':' + z(secs%60)
// }
