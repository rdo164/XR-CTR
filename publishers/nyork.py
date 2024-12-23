import ssl
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import pandas as pd
import numpy as np
from datetime import datetime

# Configuración de certificados
ca_cert = "../certs/ca.crt"
client_cert = "../certs/NewYork.crt"
client_key = "../certs/NewYork.key"

# Crear datos sintéticos
def create_synthetic_data(num_rows):
    data_list = []
    
    for _ in range(num_rows):
        new_row = {
            'Temperatura': 30 + np.random.normal(0, 10),
            'Tiempo': 'scattered clouds',
            'Direccion_viento': np.random.uniform(0, 360),
            'Velocidad_viento': np.random.uniform(0, 10)
        }
        data_list.append(new_row)
    
    synthetic_data = pd.DataFrame(data_list)
    return synthetic_data

# Generar datos sintéticos
synthetic_data = create_synthetic_data(30)

# Publicar los datos mediante MQTT
for index, row in synthetic_data.iterrows():
    temperatura, tiempo, direccion_viento, velocidad_viento = row
    topic = 'home/NewYork/viento'
    message = f'Temperatura: {temperatura}, Tiempo: {tiempo}, Direccion_viento: {direccion_viento}, Velocidad_viento: {velocidad_viento}'
    publish.single(
        topic, 
        message, 
        hostname="0.0.0.0",
        qos=2, 
        port=8883, 
        tls={'ca_certs': ca_cert, 'certfile': client_cert, 'keyfile': client_key}, 
        protocol=mqtt.MQTTv311
    )
