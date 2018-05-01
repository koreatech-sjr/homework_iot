import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    client.subscribe("home/air")
    ## client.subscribe("")

def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + " Message: " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# YOU NEED TO CHANGE THE IP ADDRESS OR HOST NAME
client.connect("192.168.0.24", 1883, 60)
#client.connect("localhost")

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Finished!")
    client.unsubscribe(["home/air"])
    client.disconnect()
