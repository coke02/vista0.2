if(typeof(EventSource) !== '') {
    var source = new EventSource("/rocio");
  
    source.onmessage = function(event) {
      document.getElementById("rocioDIV").innerHTML = event.data;
    };
  
  } else {
    document.getElementById("rocioDIV").innerHTML = "no soportado para tu navegador...";
  }