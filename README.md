# XR-CTR
Proyecto final IoT

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
