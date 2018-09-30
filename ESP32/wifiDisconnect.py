from network import WLAN

station = WLAN(0)

station.active(True)

print("Disconnecting ...")
station.disconnect()
