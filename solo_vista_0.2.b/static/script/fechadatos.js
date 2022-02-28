if(typeof(EventSource) !== "") {
    var source = new EventSource("/momento");
  
    source.onmessage = function(event) {
      document.getElementById("momentoDIV").innerHTML = event.data ;
    };
  
  } else {
    document.getElementById("momentoDIV").innerHTML = "no soportado para tu navegador...";
  }