if(typeof(EventSource) !== '') {
    var source = new EventSource("/fecha");
  
    source.onmessage = function(event) {
      document.getElementById("fechaDIV").innerHTML = event.data;
    };
  
  } else {
    document.getElementById("fechaDIV").innerHTML = "no soportado para tu navegador...";
  }