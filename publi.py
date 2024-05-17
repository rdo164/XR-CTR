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
MQTT_TOPIC = 'home/Portland/viento'  
MQTT_REGEX = 'home/([^/]+)/([^/]+)'

class Data(NamedTuple):
    location: str
    measurement: str
    time: datetime
    Temperatura: float
    Tiempo: str
    Direccion_viento: float
    Velocidad_viento: float
    

def on_connect(client, userdata, flags, rc, properties=None):
    print('Connected with result code ' + str(rc))
    client.subscribe(MQTT_TOPIC)
    data = pd.read_csv("new_temperature.csv")
    for index, row in data.head(10).iterrows():
        datetime,Temperatura,Tiempo,Direccion_viento,Velocidad_viento= row
        topic = f'home/Portland/viento'
        message = f'Temperatura: {Temperatura}, Tiempo: {Tiempo}, Direccion_viento: {Direccion_viento}, Velocidad_viento: {Velocidad_viento}'
        client.publish(topic, message)

def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))
    sensor_data = _parse_mqtt_message(msg.topic, msg.payload.decode('utf-8'))
    
    if sensor_data is not None:
        _send_sensor_data_to_influxdb(sensor_data)

def _parse_mqtt_message(topic, payload):
    match = re.match(MQTT_REGEX, topic)
    if match:
        location = match.group(1)
        measurement = match.group(2)
        if measurement == 'status':
            return None
        values = payload.split(",")
        try:
            time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
            Temperatura = float(values[0].split(":")[-1].strip())
            Tiempo = '"' + values[1].split(":")[-1].strip() + '"'
            Direccion_viento = float(values[2].split(":")[-1].strip())
            Velocidad_viento = float(values[3].split(":")[-1].strip())
            return Data(location, measurement, time, Temperatura, Tiempo, Direccion_viento, Velocidad_viento)
        except ValueError as e:
            print(f"Error parsing values: {e}")
            return None
    else:
        print(f"No match for topic: {topic}")
        return None

def _send_sensor_data_to_influxdb(sensor_data):
    time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    # Format the data including timestamp
    data = f'{sensor_data.measurement},location={sensor_data.location} {time},Temperatura={sensor_data.Temperatura},Tiempo={sensor_data.Tiempo},Direccion_viento={sensor_data.Direccion_viento},Velocidad_viento={sensor_data.Velocidad_viento}'
    # Print the data being sent
    print(f"Sending data to InfluxDB: {data}")

    # Send data to InfluxDB
    response = requests.post(INFLUXDB_URL, headers=HEADERS, data=data)
    
    # Print response status code and text
    print(f"Response status code: {response.status_code}, Response text: {response.text}")



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