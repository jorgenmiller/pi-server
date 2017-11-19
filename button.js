var socket = io.connect("10.0.0.43:5000")

function connection() {
  socket.emit('refresh', '0')
};

function button() {
  socket.emit('refresh', '1')
};

socket.on('value', function(value) {
  document.getElementById("div1").innerHTML = value
});
