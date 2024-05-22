import re
from typing import NamedTuple
import paho.mqtt.client as mqtt
import requests
import os
import csv
import ssl
import pandas as pd
import json
from datetime import datetime

INFLUXDB_URL = "https://us-east-1-1.aws.cloud2.influxdata.com/api/v2/write?org=57b4981ce8369016&bucket=tiempo&precision=ns"
INFLUXDB_TOKEN = "l2lPe6vkpnQLEH32CZOPpJwCtOcZ87KEFMlseOaWMRxkzg7JmxHHOO5Dn2hyxtKhIDOWHviklPciuC9oOZslTQ=="
HEADERS = {
    'Authorization': f'Token {INFLUXDB_TOKEN}',
    'Content-type': 'text/plain'
}

MQTT_ADDRESS = '192.168.208.2'
MQTT_TOPIC = 'home/#'  
MQTT_REGEX = 'home/([^/]+)/([^/]+)'

class Data(NamedTuple):
    location: str
    measurement: str
    Temperatura: float
    Tiempo: str
    Direccion_viento: float
    Velocidad_viento: float

def on_connect(client, userdata, flags, rc, d):
    if rc == 0:
        print("Conexión establecida con éxito al broker MQTT")
        # Suscribirse al tema después de la conexión
        client.subscribe(MQTT_TOPIC)
    else:
        print("Error de conexión al broker MQTT. Código de resultado:", rc)


def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))
    sensor_data = _parse_mqtt_message(msg.topic, msg.payload.decode('utf-8'))
    
    if sensor_data is not None:
        data = f'{sensor_data.measurement},location={sensor_data.location} Temperatura={sensor_data.Temperatura},Tiempo={sensor_data.Tiempo},Direccion_viento={sensor_data.Direccion_viento},Velocidad_viento={sensor_data.Velocidad_viento}'
        response = requests.post(INFLUXDB_URL, headers=HEADERS, data=data) #Enviamos datos a influxDB
        print(f"Response status code: {response.status_code}, Response text: {response.text}")

def _parse_mqtt_message(topic, payload):
    match = re.match(MQTT_REGEX, topic)
    if match:
        location = match.group(1)
        measurement = match.group(2)
        if measurement == 'status':
            return None
        values = payload.split(",")
        try:
            Temperatura = float(values[0].split(":")[-1].strip())
            Tiempo = '"' + values[1].split(":")[-1].strip() + '"'
            Direccion_viento = float(values[2].split(":")[-1].strip())
            Velocidad_viento = float(values[3].split(":")[-1].strip())
            return Data(location, measurement, Temperatura, Tiempo, Direccion_viento, Velocidad_viento)
        except ValueError as e:
            print(f"Error parsing values: {e}")
            return None
    else:
        print(f"No match for topic: {topic}")
        return None

import re
from typing import NamedTuple
import paho.mqtt.client as mqtt
import requests
import os
import csv
import ssl
import pandas as pd
import json
from datetime import datetime

INFLUXDB_URL = "https://us-east-1-1.aws.cloud2.influxdata.com/api/v2/write?org=57b4981ce8369016&bucket=tiempo&precision=ns"
INFLUXDB_TOKEN = "l2lPe6vkpnQLEH32CZOPpJwCtOcZ87KEFMlseOaWMRxkzg7JmxHHOO5Dn2hyxtKhIDOWHviklPciuC9oOZslTQ=="
HEADERS = {
  'Authorization': f'Token {INFLUXDB_TOKEN}',
  'Content-type': 'text/plain'
}

MQTT_ADDRESS = '192.168.208.2'
MQTT_TOPIC = 'home/#'  
MQTT_REGEX = 'home/([^/]+)/([^/]+)'

class Data(NamedTuple):
    location: str
    measurement: str
    Temperatura: float
    Tiempo: str
    Direccion_viento: float
    Velocidad_viento: float

def on_connect(client, userdata, flags, rc, d):
 if rc == 0:
    print("Conexión establecida con éxito al broker MQTT")
    # Suscribirse al tema después de la conexión
    client.subscribe(MQTT_TOPIC)
 else:
    print("Error de conexión al broker MQTT. Código de resultado:", rc)


def on_message(client, userdata, msg):
 print(msg.topic + ' ' + str(msg.payload))
 sensor_data = _parse_mqtt_message(msg.topic, msg.payload.decode('utf-8'))
 
  # Procesamiento de datos (agregado)
 if sensor_data is not None:
    # Comprobación de "status" (ya existente)
    if sensor_data.measurement == 'status':
        return None
    
    # Comprobaciones adicionales (ejemplo)
    if sensor_data.Temperatura < -20 or sensor_data.Temperatura > 40:
        print(f"Temperatura fuera de rango: {sensor_data.Temperatura}")
        # Manejar error (opcional: descartar o registrar)
        return None
    
    # ... (agregar más comprobaciones según necesidad)

    # Preparación de datos para InfluxDB
    data = f'{sensor_data.measurement},location={sensor_data.location} Temperatura={sensor_data.Temperatura},Tiempo={sensor_data.Tiempo},Direccion_viento={sensor_data.Direccion_viento},Velocidad_viento={sensor_data.Velocidad_viento}'
    response = requests.post(INFLUXDB_URL, headers=HEADERS, data=data) #Enviamos datos a influxDB
    print(f"Response status code: {response.status_code}, Response text: {response.text}")

def _parse_mqtt_message(topic, payload):
  # ... (código existente para obtener location y measurement)
  
  values = payload.split(",")
  try:
      Temperatura = float(values[0].split(":")[-1].strip())
      Tiempo = '"' + values[1].split(":")[-1].strip() + '"'
      Direccion_viento = float(values[2].split(":")[-1].strip())
      Velocidad_viento = float(values[3].split(":")[-1].strip())
      return Data(location, measurement, Temperatura, Tiempo, Direccion_viento, Velocidad_viento)
  except ValueError as e:
      print(f"Error parsing values: {e}")
      return None
  
def main():

    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.tls_set(ca_certs="./certs/ca.crt", certfile="./certs/cliente.crt", keyfile="./certs/cliente.key", tls_version=ssl.PROTOCOL_TLS)
    mqtt_client.connect(MQTT_ADDRESS, 8883)
    mqtt_client.loop_forever()


if __name__ == '__main__':
    print('MQTT to InfluxDB puente')
    main()