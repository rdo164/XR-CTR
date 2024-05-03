import re
from typing import NamedTuple
import paho.mqtt.client as mqtt
import requests
import os
import ssl

# Los datos son insertados mediante el uso de InfluxDB API
INFLUXDB_URL = "https://us-east-1-1.aws.cloud2.influxdata.com/api/v2/write?org=57b4981ce8369016&bucket=tiempo&precision=ns"

INFLUXDB_TOKEN = "l2lPe6vkpnQLEH32CZOPpJwCtOcZ87KEFMlseOaWMRxkzg7JmxHHOO5Dn2hyxtKhIDOWHviklPciuC9oOZslTQ=="
HEADERS = {
    'Authorization': f'Token {INFLUXDB_TOKEN}',
    'Content-type': 'text/plain'
}

# Configuración de MQTT
MQTT_ADDRESS = '192.168.208.2'

#MQTT_USER = 'iotuser'
#MQTT_PASSWORD = 'iotpassword'
MQTT_TOPIC = 'home/+/+'  # [room]/[temperature|humidity|light|status]
MQTT_REGEX = 'home/([^/]+)/([^/]+)'
MQTT_CLIENT_ID = 'MQTTInfluxDBBridge'


class SensorData(NamedTuple):
    location: str
    measurement: str
    value: float

# publicador
def on_connect(client, userdata, flags, rc, properties=None):

    print('Connected with result code ' + str(rc))

    # s
    client.subscribe(MQTT_TOPIC)
    # Publicar 10 mensajes MQTT
    for i in range(10):

        topic = f'home/room{i}/temperature'
        
        message = f'{20 + i * 0.5}'  # temperatura incremental

        client.publish(topic, message)


# suscriptor
def on_message(client, userdata, msg):

    print(msg.topic + ' ' + str(msg.payload))
    sensor_data = _parse_mqtt_message(msg.topic, msg.payload.decode('utf-8'))

    if sensor_data is not None:
        _send_sensor_data_to_influxdb(sensor_data)

# conversión de datos
def _parse_mqtt_message(topic, payload):

   
    match = re.match(MQTT_REGEX, topic)
    
    if match:
    
        location = match.group(1)
    
        measurement = match.group(2)

        if measurement == 'status':
            return None
        return SensorData(location, measurement, float(payload))
    
    else:
        return None

# envío de datos
def _send_sensor_data_to_influxdb(sensor_data):
    
    data = f'{sensor_data.measurement},location={sensor_data.location} value={sensor_data.value}'
    
    response = requests.post(INFLUXDB_URL, headers=HEADERS, data=data)
    
    print(response.text)


def main():

    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    # mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.tls_set(ca_certs="./certs/ca.crt", certfile="./certs/cliente.crt", keyfile="./certs/cliente.key", tls_version=ssl.PROTOCOL_TLS)
    mqtt_client.connect(MQTT_ADDRESS, 8883)
    mqtt_client.loop_forever()


if __name__ == '__main__':
    print('MQTT to InfluxDB puente')
    main()
