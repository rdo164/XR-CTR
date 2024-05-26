import ssl
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import pandas as pd
import time

# Configuración de certificados
ca_cert = "./certs/ca.crt"
client_cert = "./certs/LasVegas.crt"
client_key = "./certs/LasVegas.key"

data = pd.read_csv("LVegas.csv")
for index, row in data.iterrows():
    datetime,Temperatura,Tiempo,Direccion_viento,Velocidad_viento= row
    Temperatura = Temperatura -273
    topic = f'home/LasVegas/viento'
    message = f'Temperatura: {Temperatura}, Tiempo: {Tiempo}, Direccion_viento: {Direccion_viento}, Velocidad_viento: {Velocidad_viento}'
    publish.single(topic, message, hostname="0.0.0.0", qos=2, port=8883, tls={'ca_certs': ca_cert, 'certfile': client_cert, 'keyfile': client_key}, protocol=mqtt.MQTTv311)
    time.sleep(10)