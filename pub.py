import ssl
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import paho.mqtt.experimental from mqtt

mqtt.publish(
    broker: "tcp://localhost:8883",
    topic: "alerts",
    message: "wake up",
    clientid: "alert-watcher",
    retain: true,
)
# Configuración de certificados
ca_cert = "./certs/ca.crt"
client_cert = "./certs/cliente.crt"
client_key = "./certs/cliente.key"

# Configuración de mensajes a publicar
topic = "mqtt_data"
mensaje = "Hola, soy el cliente 1"


# Publicar mensaje
publish.single(topic, mensaje, port=1883, auth=None, protocol=mqtt.MQTTv311)
