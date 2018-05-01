import paho.mqtt.client as mqtt

temp = 0.0
humidity = 0.0
discomport = 0.0

person = 0

### publish
def on_connect_publish(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_publish(client, userdata, mid):
    msg_id = mid

mqttc = mqtt.Client()
mqttc.on_connect = on_connect_publish
mqttc.on_publish = on_publish
# pi
# mqttc.connect("192.168.0.24")
# mac
mqttc.connect("172.19.89.83")

### subscribe
def on_connect_subscribe(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    client.subscribe("home/temperature")
    client.subscribe("home/humidity")
    client.subscribe("home/person")

def on_message(client, userdata, msg):

    global temp
    global humidity
    global discomport

    global person

    print("Topic: " + msg.topic + " Message: " + str(msg.payload))
    msg_air = (msg.payload)


    if msg.topic == "home/temperature":
        temp = float(msg.payload)
    elif msg.topic == "home/humidity":
        humidity = float(msg.payload)
    elif msg.topic == "home/person":
        person = float(msg.payload)

    discomport = 1.8*temp-0.55*(1.0-humidity*0.01)*(1.8*temp-26.0)+32.0

    if person == True :
        (result, m_id) = mqttc.publish("home/light", 1)

        if discomport >= 75 :
            (result, m_id) = mqttc.publish("home/air", 1)
        else :
            (result, m_id) = mqttc.publish("home/air", 0)

    else :
        (result, m_id) = mqttc.publish("home/light", 0)
        (result, m_id) = mqttc.publish("home/air", 0)

    print("discomport index : ", discomport )


client = mqtt.Client()
client.on_connect = on_connect_subscribe
client.on_message = on_message
# pi
#client.connect("192.168.0.24", 1883, 60)
# mac
client.connect("172.19.89.83", 1883, 60)



try:
    client.loop_forever()

except KeyboardInterrupt:
    print("Finished!")
    client.unsubscribe(["home/temperature", "home/humidity"])
    client.disconnect()
    mqttc.loop_stop()
    mqttc.disconnect()
