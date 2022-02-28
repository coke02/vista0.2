if(typeof(EventSource) !== "") {
    var source = new EventSource("/tempmin");
  
    source.onmessage = function(event) {
      document.getElementById("tempminDIV").innerHTML = event.data ;
    };
  
  } else {
    document.getElementById("tempminDIV").innerHTML = "no soportado para tu navegador...";
  }