import paho.mqtt.client as mqtt
import adafruit_dht
import board
import time

# Initialize DHT22 Sensor
dht_device = adafruit_dht.DHT22(board.D4)  # DHT22 sensor on GPIO4

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
        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity
            
            if temperature is not None and humidity is not None:
                payload = f"Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%"
                print(f"Publishing: {payload}")
                client.publish(TOPIC, payload)
            else:
                print("Failed to read from sensor, retrying...")

        except RuntimeError as error:
            print(f"Sensor reading error: {error}")  # Common for DHT sensors, just retry
            time.sleep(2)
            continue

        time.sleep(5)  # Publish data every 5 seconds

except Exception as e:
    print(f"Error: {e}")

finally:
    client.disconnect()
    print("MQTT Disconnected")
