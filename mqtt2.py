#humid/temperature
#led light

#pip3 install adafruit-circuitpython-dht
#sudo apt-get install libgpiod2
#pip3 install adafruit-blinka

import time
import adafruit_dht
import board
import paho.mqtt.client as mqtt
import json

dht_device = adafruit_dht.DHT11(board.D4)

class MQTTClient:
    def __init__(self, server, port):
        self.mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_message = self.on_message
        self.mqttc.connect(server, port, 60)

    def on_connect(self, client, userdata, flags, reason_code, properties):
        print(f"Connected with result code {reason_code}")
        # Subscribe to a topic 
        # self.mqttc.subscribe("onrelay")

    def on_message(self, client, userdata, msg):
        try:
            # Attempt to parse the message payload as JSON
            message = json.loads(msg.payload.decode())
            print(msg.topic, message)
            # Handle relay topic(rpi 1, water pump for webdashboard side when they turn on)
            if msg.topic == 'onrelay':
                # Control the relay based on the message
                self.control_relay(message)
            else:
                print(f"Received message on unhandled topic: {msg.topic}")
        except json.JSONDecodeError:
            print(f"Could not parse message payload as JSON: {msg.payload}")

    def start(self):
        self.mqttc.loop_start()

    def stop(self):
        self.mqttc.loop_stop()
        # Clean up
        # GPIO.cleanup()

    # Method to publish json with topic to broker
    def publish(self, topic, message):
        self.mqttc.publish(topic, json.dumps(message))

    # Read temperature and humidity from sensor and publishes the data
    def readTempAndHumid(self, topic):
        try:
            temperature_c = dht_device.temperature
            temperature_f = temperature_c * (9 / 5) + 32

            humidity = dht_device.humidity

            print("Temp:{:.1f} C / {:.1f} F    Humidity: {}%".format(temperature_c, temperature_f, humidity))
            # Publish the moisture level
            self.publish(topic, {'temp': "{:.2f}".format(temperature_c), 'humid':"{}%".format(humidity)})

            # FOR TESTING (HARD CODED DATA, for work WITHOUT sensors)
            # print("Temp:{:.1f} C / {:.1f} F    Humidity: {}%".format(30.50, 86.9, 55.55))
            # self.publish(topic, {'temp': "{:.2f}".format(30.50), 'humid':"{}%".format(55.55)})

        except RuntimeError as err:
            print(err.args[0])


if __name__ == "__main__":
    # Main method
    # Replace "test.mosquitto.org" with the Broker IP such as "192.xxx.xxx.xxx" or wtv is the ip
    client = MQTTClient("test.mosquitto.org", 1883)

    client.start()
    try:
        while True:
            # Topic used is "home/temp", able to change depending on topic needed
            client.readTempAndHumid("home/temp")
            time.sleep(1)  # Delay for 1 second before reading again
    except KeyboardInterrupt:
        client.stop()
