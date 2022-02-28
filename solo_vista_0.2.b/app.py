from flask import Flask, render_template, Response, json
import requests, time
from datetime import datetime
from decimal import *


app = Flask(__name__)

url = ('https://climatologia.meteochile.gob.cl/application/productos/emaResumenDiario/330020')

url2 = requests.get('https://climatologia.meteochile.gob.cl/application/productos/boletinClimatologicoDiario')


@app.route("/")
def vista():
    
    while True:
        response = requests.get(url)
        weatherdata = response.json()
        estacion = weatherdata['datosEstacion']['nombreEstacion']
        codigo_nacional = weatherdata['datosEstacion']['codigoNacional']
        precialafecha = weatherdata['datos']['valoresMasRecientes']['aguaCaida24Horas']
        
        text = url2.text
        data=json.loads(text)
        momento1 = data[9]['metaDatos']['fechaDatos']
        intensidadV = data[9]['datos']['viento']['intensidad']
        direccionV = data[9]['datos']['viento']['direccion']
        tiempo_presente = data[9]['datos']['tiempoPresente']
        
        
          
        return render_template ("vista.html", est = estacion, cn = codigo_nacional,precialafecha=precialafecha, 
                                intensidadV=intensidadV, direccionV=direccionV, fechadatos=momento1, 
                                tiempo_presente=tiempo_presente)
        
@app.route('/agua24')
def agua24():
    
    def agua_24():
        
        while True:
            
            text = url2.text
            data1=json.loads(text)
            agua2 = data1[9]['datos']['precipitacion24Horas']

            yield f"data:{agua2}\n\n"
                
            time.sleep(300)
            
    return Response(agua_24(), mimetype= 'text/event-stream')

@app.route('/rocio')
def rocio():
    
    def punto_rocio():
        
        while True:
            response = requests.get(url)
            weatherdata = response.json()
            rocio = weatherdata['datos']['valoresMasRecientes']['puntoDeRocio']
            rocio1 = Decimal(rocio)
            rocio = round(rocio1,1)
            yield f"data:{rocio} º\n\n"
            time.sleep(300)
            
            
    return Response(punto_rocio(), mimetype= 'text/event-stream')

@app.route('/humedad')
def humedad():
    
    def humedad_relativa():
        
        while True:
            response = requests.get(url)
            weatherdata = response.json()
            humedad = weatherdata['datos']['valoresMasRecientes']['humedadRelativa']
            humedad1 = Decimal(humedad)
            humedad = round(humedad1,1)
            yield f"data:{humedad} H\n\n"
            time.sleep(300)
            
            
    return Response(humedad_relativa(), mimetype= 'text/event-stream')

@app.route('/data')
def data():
    
    def temperatura_actual():
        
        while True:
            response = requests.get(url)
            weatherdata = response.json()
            high = weatherdata['datos']['valoresMasRecientes']['temperatura']
            a_number = Decimal(high)
            high = round(a_number,1)
            yield f"data:{high} ºC\n\n"
            time.sleep(300)
            
    return Response(temperatura_actual(), mimetype= 'text/event-stream')

@app.route('/viento')
def viento():
    
    def viento_actual():
        
        while True:
            response = requests.get(url)
            weatherdata = response.json()
            viento = weatherdata['datos']['valoresMasRecientes']['fuerzaDelViento']
            a_number = Decimal(viento)
            viento = round(a_number,1)

            yield f"data:{viento} m/s\n\n"
            time.sleep(300)
            
    return Response(viento_actual(), mimetype= 'text/event-stream')

@app.route('/agua')
def agua():
    
    def agua_actual():
        
        while True:
            response = requests.get(url)
            weatherdata = response.json()
            agua = weatherdata['datos']['valoresMasRecientes']['aguaCaidaDelMinuto']
            a_number = Decimal(agua)
            agua = round(a_number,1)
            
            if agua == 0.0:
                yield f"data: S/P\n\n"
            elif agua > 0.0:    
                yield f"data:{agua} ml\n\n"
                
            time.sleep(300)
            
    return Response(agua_actual(), mimetype= 'text/event-stream')

@app.route('/fecha')
def fecha():
    
    def fecha_dato():
        
        while True:
            response = requests.get(url)
            weatherdata = response.json()
            fecha = weatherdata['fechaCreacion']
            yield f"data:{fecha} UTC\n\n"
            time.sleep(300)
            
    return Response(fecha_dato(), mimetype= 'text/event-stream')


@app.route('/tempmax')
def tempmax():
    
    def temp_max():
        
        while True:
            
            text = url2.text
            data=json.loads(text)
            tempmax = data[9]['datos']['temperaturaMaxima']
            yield f"data:{tempmax} ºC\n\n"
            time.sleep(86400)
            
    return Response(temp_max(), mimetype= 'text/event-stream')


@app.route('/tempmin')
def tempmin():
    
    def temp_min():
        
        while True:
            
            text = url2.text
            data=json.loads(text)
            tempmin = data[9]['datos']['temperaturaMinima']
            yield f"data:{tempmin} ºC\n\n"
            time.sleep(300)
            
    return Response(temp_min(), mimetype= 'text/event-stream')


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port= 8080, debug=True)