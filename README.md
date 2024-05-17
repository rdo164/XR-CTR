# XR-CTR
Proyecto final IoT
Envio de datos mediante MQTT con certificados TLS/SSL

Para asegurar que los IPs coincidan para el envío mediante certificados, es necesario verificar los siguientes puntos:
- Creación de certificados en el apartado de SAN: Al generar los certificados, es necesario incluir las direcciones IP necesarias en el campo de Subject Alternative Name (SAN) para que coincidan con las direcciones IP utilizadas en tu configuración.

Configuración en mosquitto.conf: En el archivo de configuración mosquitto.conf, especifica la dirección IP correcta en el apartado bind_address para que el servidor MQTT se enlace a la dirección IP deseada.

Configuración en docker-compose: En docker-compose para desplegar Mosquitto, es necesario configurar correctamente las secciones de subnet(subred) y gateway(direccion IP concreta) para que coincidan con tu red y dirección IP.

Configuración en el archivo .py: En el script Python publi.py donde publicamos los datos a través de MQTT, es necesario asegurarse de que la dirección IP utilizada en la variable MQTT_ADDRESS coincida con las direcciones IP configuradas en los pasos anteriores.



Bibliografía

- Send Data via mqtt https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-mqtt.html

```
version: '3'

services:
  mqtt-broker:
    image: eclipse-mosquitto
    container_name: mqtt-broker
    ports:
      - "1883:1883"
    volumes:
      - ./mosquitto.conf:/mosquitto/config/mosquitto.conf:ro  # Ajusta la ruta del archivo de configuración si es necesario

  influxdb:
    image: influxdb:latest
    volumes:
      - influxdb-storage:/var/lib/influxdb  # Ruta donde se almacenarán los datos de InfluxDB
    environment:
      - INFLUXDB_DB=db0
      - INFLUXDB_ADMIN_USER=xabitelle
      - INFLUXDB_ADMIN_PASSWORD=MFONWOOCLCNRO  # Ajusta la contraseña del administrador de InfluxDB

  telegraf:
    image: telegraf
    volumes:
      - ./telegraf.conf:/etc/telegraf/telegraf.conf:ro  # Ajusta la ruta del archivo de configuración de Telegraf
    depends_on:
      - mqtt-broker
      - influxdb

volumes:
  influxdb-storage:
  
```

```
home/room0/temperature b'20.0'    
<html>
<head><title>405 Not Allowed</title></head>
<body>
<center><h1>405 Not Allowed</h1></center>  
<hr><center>nginx/1.24.0</center>
</body>
</html>

home/room1/temperature b'20.5'
<html>
<head><title>405 Not Allowed</title></head>
<body>
<center><h1>405 Not Allowed</h1></center>  
<hr><center>nginx/1.24.0</center>
</body>
</html>

home/room2/temperature b'21.0'
<html>
<head><title>405 Not Allowed</title></head>
<body>
<center><h1>405 Not Allowed</h1></center>
<hr><center>nginx/1.24.0</center>
</body>
</html>

home/room3/temperature b'21.5'
<html>
<head><title>405 Not Allowed</title></head>
<body>
<center><h1>405 Not Allowed</h1></center>
<hr><center>nginx/1.24.0</center>
</body>
</html>

home/room4/temperature b'22.0'
<html>
<head><title>405 Not Allowed</title></head>
<body>
<center><h1>405 Not Allowed</h1></center>
<hr><center>nginx/1.24.0</center>
</body>
</html>

home/room5/temperature b'22.5'
<html>
<head><title>405 Not Allowed</title></head>
<body>
<center><h1>405 Not Allowed</h1></center>
<hr><center>nginx/1.24.0</center>
</body>
</html>

home/room6/temperature b'23.0'
<html>
<head><title>405 Not Allowed</title></head>
<body>
<center><h1>405 Not Allowed</h1></center>
<hr><center>nginx/1.24.0</center>
</body>
</html>
```
Problemas
