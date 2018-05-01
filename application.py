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

temp = 0.0
humidity = 0.0
person = False
discomport = 0.0
### subscribe
def on_connect_subscribe(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    client.subscribe("home/temperature")
    client.subscribe("home/humidity")
    client.subscribe("home/person")

def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + " Message: " + str(msg.payload))
    msg_air = "Topic: " + msg.topic + " Message: " + str(msg.payload)


    if msg.topic == "home/temperature":
        temp = msg.payload
    elif msg.topic == "home/humidity":
        humidity = msg.payload
    elif msg.topic == "home/person":
        person = msg.payload

    discomport = 9.0/5.0*temp - 0.55*(1.0-humidity*0.01)(9.0/5.0*temp-26.0)+32.0
    
    (result, m_id) = mqttc.publish("home/air", discomport)


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
