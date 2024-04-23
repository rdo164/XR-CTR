import paho.mqtt.client as mqtt
import ssl

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Conexao con MQTT {reason_code} por {client} {userdata}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("tumamsota/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    temperature = float(msg.payload.decode('utf-8'))

    print(f"Temperatura recibida: {temperature} °C por el {client}")

mqtt_cliente = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_cliente.on_connect = on_connect
mqtt_cliente.on_message = on_message
#

# configuración TLS
mqtt_cliente.tls_set(
    ca_certs="/mnt/c/D_IoT/D_IoT_Reto2/Certificado/mosquitto.org.crt",
                     certfile="/mnt/c/D_IoT/D_IoT_Reto2/Certificado/client.crt",
                     keyfile="/mnt/c/D_IoT/D_IoT_Reto2/Certificado/client.key",
                     tls_version=ssl.PROTOCOL_TLSv1_2)

mqtt_cliente.connect("test.mosquitto.org", 8884, 20) 

#            conexión a utilizar | puerto | cada cuanto tiempos
mqtt_cliente.loop_forever()
