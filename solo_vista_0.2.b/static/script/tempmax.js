if(typeof(EventSource) !== "") {
    var source = new EventSource("/tempmax");
  
    source.onmessage = function(event) {
      document.getElementById("tempmaxDIV").innerHTML = event.data ;
    };
  
  } else {
    document.getElementById("tempmaxDIV").innerHTML = "no soportado para tu navegador...";
  }