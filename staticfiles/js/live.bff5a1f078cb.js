let socket = new WebSocket("ws://localhost:8000/ws/live/" + game_id)
socket.onopen = function(e) {
    console.log("socket connected")
}
let win = false;
socket.onmessage = function(e) {
    console.log("socket message", e['data'])
    if (e['data'] == 'Win') {
        if (win) {
            swal("You Won!")
                .then((value) => {
                    game_over()
                });
        } else {
            swal("Opponent Won!")
                .then((value) => {
                    game_over()
                });
        }

    }
    $("." + key_to_board[e['data']]).css('background-color', 'coral');
    let i = parseInt(key_to_board[e['data']][1]) - 1
    let j = parseInt(key_to_board[e['data']][3]) - 1
    console.log(i)
    live_board[i][j] = 0
    move = !move
    checkifWin()
}
socket.onclose = function(e) {
    console.log("socket close")
}
var board = JSON.parse(board_str)
var key_to_board = {}
var live_board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
var move
if (is_my_move == "True") move = true
else move = false
for (let i = 1; i < 6; i++) {
    for (let j = 1; j < 6; j++) {
        let cur = "r" + (i).toString() + "c" + (j).toString()
        $("." + cur).text(board[cur])
        key_to_board[board[cur]] = cur
        live_board[i - 1][j - 1] = board[cur]
    }
}
console.log(game_id)
$(".num").click(function(e) {
    //$(this).css("background", "coral");
    if (move) socket.send($(this).text())
});



function checkifWin() {
    let k = 0
    for (let i = 0; i < 5; i++) {
        let ans = true;
        for (let j = 0; j < 5; j++) {
            ans = ans && (live_board[i][j] == 0)
        }
        if (ans) k++;
        ans = true;
        for (let j = 0; j < 5; j++) {
            ans = ans && (live_board[j][i] == 0)
        }
        if (ans) k++;
    }
    if (k >= 5) {
        claimWin()
    }
}

function claimWin() {
    win = true;
    socket.send("Win")
}

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

function game_over() {
    _GET_REQUEST('http://127.0.0.1:8000/live/finish/', () => {
        window.location = '/'
    })
}