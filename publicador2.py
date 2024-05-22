import ssl
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import pandas as pd

# Configuración de certificados
ca_cert = "./certs/ca.crt"
client_cert = "./certs/cliente2.crt"
client_key = "./certs/cliente2.key"

data = pd.read_csv("LVegas.csv")
for index, row in data.head(30).iterrows():
    datetime,Temperatura,Tiempo,Direccion_viento,Velocidad_viento= row
    topic = f'home/LasVegas/viento'
    message = f'Temperatura: {Temperatura}, Tiempo: {Tiempo}, Direccion_viento: {Direccion_viento}, Velocidad_viento: {Velocidad_viento}'
    publish.single(topic, message, hostname="192.168.208.2", port=8883, tls={'ca_certs': ca_cert, 'certfile': client_cert, 'keyfile': client_key}, protocol=mqtt.MQTTv311)