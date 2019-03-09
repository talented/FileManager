// utils.js
import moment from 'moment'

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
    var date = new Date(timestamp)
    var formattedTime = moment(date).fromNow()
    return formattedTime
}

export { wait, sizeFormatter, dateFormatter }
