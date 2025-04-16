from zeroconf import Zeroconf, ServiceBrowser, ServiceListener
import socket

class NanoleafListener(ServiceListener):
    def add_service(self, zeroconf, service_type, name):
        info = zeroconf.get_service_info(service_type, name)
        if info and "nanoleaf" in name.lower():
            ip = socket.inet_ntoa(info.addresses[0])
            print(f"✅ Found Nanoleaf: {name} at IP {ip}")
        else:
            print(f"ℹ️ Service found: {name}, but not Nanoleaf")

    def update_service(self, zeroconf, service_type, name):
        pass

    def remove_service(self, zeroconf, service_type, name):
        pass

if __name__ == "__main__":
    zeroconf = Zeroconf()
    listener = NanoleafListener()
    browser = ServiceBrowser(zeroconf, "_nanoleaf._tcp.local.", listener)

    try:
        print("🔎 Scanning for Nanoleaf devices... Press Ctrl+C to stop.")
        import time
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopping discovery.")
    finally:
        zeroconf.close()
