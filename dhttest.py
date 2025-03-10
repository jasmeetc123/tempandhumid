import adafruit_dht
import board
import time

dht_device = adafruit_dht.DHT11(board.D17)  # Change D4 if needed

try:
    temperature = dht_device.temperature
    humidity = dht_device.humidity
    print(f"Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%")
except RuntimeError as error:
    print(f"Error reading sensor: {error}")
