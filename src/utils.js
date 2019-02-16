// utils.js

// utils to delay promise
function wait(ms) {
    return (x) => {
        console.log("will be waiting")
        return new Promise(resolve => setTimeout(() => resolve(x), ms));
    };
}

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

function secondsToHMS(secs) {
  function z(n){return (n<10?'0':'') + n;}
  var sign = secs < 0? '-':'';
  secs = Math.abs(secs);
  return sign + z(secs/3600 |0) + ':' + z((secs%3600) / 60 |0) + ':' + z(secs%60);
}

function dateFormatter(params) {

    var timestamp = params.value
    var now = new Date()
    var date = new Date(timestamp)

    var time_difference_in_seconds = (now.getTime() - date.getTime()) / 1000
    // return secondsToHMS(time_difference_in_seconds)
    const t = 60
    const times = ['seconds', 'minutes', 'hours', 'days', 'month', 'year']
    var formattedTime = null
    switch (true) {
      case (time_difference_in_seconds < t):
        formattedTime = (Math.trunc(time_difference_in_seconds)).toString() + " " + times[0]
        break
      case (time_difference_in_seconds < 60 * t) :
        formattedTime = (Math.trunc(time_difference_in_seconds/60)).toString() + " " + times[1]
        break
      case (time_difference_in_seconds < 3600 * t):
        formattedTime = (Math.trunc(time_difference_in_seconds/3600)).toString() + " " + times[2]
        break
      case (time_difference_in_seconds < 3600 * 24 * t):
        formattedTime = (Math.trunc(time_difference_in_seconds/3600 * 24)).toString() + " " + times[3]
        break
      case (time_difference_in_seconds < 3600 * 24 * 30 * t):
        formattedTime = (Math.trunc(time_difference_in_seconds/3600 * 24 * 30)).toString() + " " + times[4]
        break
    }
    return formattedTime + ' ago'
    // if (time_difference_in_seconds < 60) {
    //   formattedTime = times[0]
    // }
    // else if (60 < time_difference_in_seconds < 3600) {
    //   formattedTime = times[1]
    // }
    // else if (3600 < time_difference_in_seconds < 216000) {
    //   formattedTime = times[2]
    // }
    // else if (216000 < time_difference_in_seconds < 12960000) {
    //   formattedTime = times[3]
    // }
    // else if (time_difference_in_seconds > 12960000) {
    //   formattedTime = times[4]
    // }
    //
    // return formattedTime + ' ago'
    // // multiplied by 1000 so that the argument is in milliseconds, not seconds.
    // // var date = new Date(timestamp*1000);
    // var year = date.getFullYear()
    // var month = date.getMonth()
    // var day = date.getDate();
    // console.log("days: ", days)
    // // Hours part from the timestamp
    // var hours = date.getHours();
    // console.log("hours: ", hours)
    // // Minutes part from the timestamp
    // var minutes = "0" + date.getMinutes();
    // // Seconds part from the timestamp
    // var seconds = "0" + date.getSeconds();
    //
    // // Will display time in 10:30:23 format
    // // var formattedTime = hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
    //
    // return date
}

export { wait, sizeFormatter, dateFormatter }
