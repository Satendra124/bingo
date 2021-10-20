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

function close_request() {
    _GET_REQUEST('http://127.0.0.1:8000/search/close', (response) => {
        console.log(response);
    })
}

window.addEventListener('beforeunload', close_request);

function ask_if_match() {
    _GET_REQUEST('/live/ask', (response) => {
        var jsres = JSON.parse(response)
        if (jsres['status'] == 'active') window.location = '/live/board/'
        console.log(response)
    });
}

setInterval(ask_if_match, 10000);