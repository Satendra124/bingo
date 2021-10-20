function _GET_REQUEST(url, response) {
    var xhttp;
    if (window.XMLHttpRequest) {
        xhttp = new XMLHttpRequest();
    } else {
        xhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            response(this.responseText);
        }
    };

    xhttp.open("GET", url, true);
    xhttp.send();
}

function _POST_REQUEST(url, params, response) {
    var xhttp;
    if (window.XMLHttpRequest) {
        xhttp = new XMLHttpRequest();
    } else {
        xhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            response(this.responseText);
        }
    };

    xhttp.open("POST", url, true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send(params);
}


window.addEventListener('beforeunload', function(e) {
    _GET_REQUEST('http://127.0.0.1:8000/search/close', (response) => {
        console.log(response);
    })
});

setInterval(_GET_REQUEST('http://127.0.0.1:8000/live/ask', (response) => {
    console.log(response);
    console.log("called");
}), 10000);