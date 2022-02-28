if(typeof(EventSource) !== "") {
    var source = new EventSource("/agua24");
  
    source.onmessage = function(event) {
      document.getElementById("agua24DIV").innerHTML = event.data;
    };
  
  } else {
    document.getElementById("agua24DIV").innerHTML = "no soportado para tu navegador...";
  }