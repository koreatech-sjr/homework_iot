import paho.mqtt.client as mqtt



### publish
def on_connect_publish(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_publish(client, userdata, mid):
    msg_id = mid
    print("message published")

mqttc = mqtt.Client()
mqttc.on_connect = on_connect_publish
mqttc.on_publish = on_publish
mqttc.connect("192.168.0.24")



### subscribe
def on_connect_subscribe(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    client.subscribe("home/temperature")
    client.subscribe("home/humidity")

def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + " Message: " + str(msg.payload))
    msg_air = "Topic: " + msg.topic + " Message: " + str(msg.payload)
    (result, m_id) = mqttc.publish("home/air", msg_air)

client = mqtt.Client()
client.on_connect = on_connect_subscribe
client.on_message = on_message
client.connect("192.168.0.24", 1883, 60)



try:
    client.loop_forever()

except KeyboardInterrupt:
    print("Finished!")
    client.unsubscribe(["home/temperature", "home/humidity"])
    client.disconnect()
    mqttc.loop_stop()
    mqttc.disconnect()
