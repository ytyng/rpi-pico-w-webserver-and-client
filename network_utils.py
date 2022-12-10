import rp2
import network
import uasyncio
import secrets


async def prepare_wifi():
    """
    Prepare Wi-Fi connection.

    https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf  # noqa
    """
    # Set country code
    rp2.country(secrets.COUNTRY)

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)

    for i in range(10):
        status = wlan.status()
        if wlan.status() < 0 or wlan.status() >= network.STAT_GOT_IP:
            break
        print(f'Waiting for connection... status={status}')
        uasyncio.sleep(1)
    else:
        raise RuntimeError('Wifi connection timed out.')

    # CYW43_LINK_DOWN (0)
    # CYW43_LINK_JOIN (1)
    # CYW43_LINK_NOIP (2)
    # CYW43_LINK_UP (3)
    # CYW43_LINK_FAIL (-1)
    # CYW43_LINK_NONET (-2)
    # CYW43_LINK_BADAUTH (-3)

    wlan_status = wlan.status()

    if wlan_status != network.STAT_GOT_IP:
        raise RuntimeError(
            'Wi-Fi connection failed. status={}'.format(wlan_status))

    print('Wi-fi ready. ifconfig:', wlan.ifconfig())
    return wlan
