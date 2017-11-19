var socket = io.connect("127.0.0.1:5000")
var number = undefined

io.on('value get', value, get_values()){
  number = value
}


function check(){

}

function get_values(){
  socket.emit('get values')
}

function set_values(){
  socket.emit('set values')
}
