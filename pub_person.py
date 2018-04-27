import paho.mqtt.client as mqtt
import random
import time

### person sensor

def getMsg():
    msg = str(random.randrange(0, 1))
    return msg

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_publish(client, userdata, mid):
    msg_id = mid
    print("message published")

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

# YOU NEED TO CHANGE THE IP ADDRESS OR HOST NAME
mqttc.connect("192.168.0.24")
#mqttc.connect("localhost")
mqttc.loop_start()

try:
    while True:
        t = getMsg()
        (result, m_id) = mqttc.publish("home/person", t)
        time.sleep(2)

except KeyboardInterrupt:
    print("Finished!")
    mqttc.loop_stop()
    mqttc.disconnect()
