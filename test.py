import paho.mqtt.client as mqtt
import Adafruit_DHT
import time

# Sensor Configuration
SENSOR = Adafruit_DHT.DHT22  # Change to DHT11 if needed
PIN = 4  # GPIO pin connected to the sensor

# MQTT Configuration
BROKER = "localhost"  # Change this to your Raspberry Pi’s IP if needed
PORT = 1883
TOPIC = "sensor/temperature"

# Initialize MQTT Client
client = mqtt.Client()

try:
    client.connect(BROKER, PORT, 60)
    print(f"Connected to MQTT Broker at {BROKER}:{PORT}")

    while True:
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
        if temperature and humidity:
            payload = f"Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%"
            print(f"Publishing: {payload}")
            client.publish(TOPIC, payload)
        else:
            print("Failed to read from sensor, retrying...")
        
        time.sleep(5)  # Publish data every 5 seconds

except Exception as e:
    print(f"Error: {e}")

finally:
    client.disconnect()
    print("MQTT Disconnected")
