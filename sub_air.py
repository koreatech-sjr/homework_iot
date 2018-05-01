import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    client.subscribe("home/air")
    ## client.subscribe("")

def on_message(client, userdata, msg):
    if int(msg.payload) == 1 :
        print("Topic: " + msg.topic + " AirConditioner : " + "ON")
    else :
        print("Topic: " + msg.topic + " AirConditioner : " + "OFF")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# YOU NEED TO CHANGE THE IP ADDRESS OR HOST NAME
# pi
# client.connect("192.168.0.24", 1883, 60)
# mac
client.connect("172.19.89.83", 1883, 60)
#client.connect("localhost")

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Finished!")
    client.unsubscribe(["home/air"])
    client.disconnect()
