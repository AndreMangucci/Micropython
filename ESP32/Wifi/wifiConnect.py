from network import WLAN
from time import sleep

ssid = "HERMANN 2.4GHz"
password = "nino021712"
station = WLAN(0)

station.active(True)
station.connect(ssid, password)

sleep(2)

print(station.isconnected())
print('teste')

