import paho.mqtt.client as mqtt
def on_connect(client, userdata, flags, rc):
    i=0

def on_message(client, userdata, msg):
	i=0

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("127.0.0.1", 1883, 60)
client.loop_start()


def printToAWSconsole(args):
    client.publish("response", args, 0)


