if(typeof(EventSource) !== '') {
    var source = new EventSource("/humedad");
  
    source.onmessage = function(event) {
      document.getElementById("humedadDIV").innerHTML = event.data;
    };
  
  } else {
    document.getElementById("humedadDIV").innerHTML = "no soportado para tu navegador...";
  }