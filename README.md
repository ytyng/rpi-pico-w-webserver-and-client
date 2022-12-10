# rpi-pico-w-webserver-and-client

Raspberry Pi Pico W webserver and client sample code

## Raspberry PI Pico W

https://www.raspberrypi.com/products/raspberry-pi-pico/

It is a small microcomputer board equipped with Wi-fi.
It is very convenient for developing IoT gadgets because
it can perform network communication by itself.

Unlike Raspberry Pi Zero, etc., it is not possible to run an OS such as Linux,
You can run code written in MicroPython.

Wifi を搭載した小さなマイコンボードです。
単体でネットワーク通信ができることにより、IoT ガジェットの開発に非常に便利です。

Raspberry Pi Zero 等と違い、 Linux 等のOS が実行できるわけではありませんが、
MicroPython で書いたコードを実行できます。


## uf2 Framework

Download uf2 firmware from here
https://micropython.org/download/rp2-pico-w/

Latest build link:
https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2

Install uf2 firmware to Raspberry Pi Pico W using Raspberry Pi Pico's USB port.

## Libraries

Install libraries using Thonny IDE.

Thonny > tools > Manage packages

- urequest
- microdot
- microdot_asyncio

## Hardware Setup

Connect switch to GPIO 14 and GND.

## Configure

Copy secrets.template.py to secrets.py and edit it.

## Deployment

Copy main.py, network_utils.py, secrets.py to Raspberry Pi Pico W using Thonny IDE.

## Run

Run main.py using Thonny IDE.

Request Raspberry PI Pico W's IP address from your browser.

http://xxx.xxx.xxx.xxx/

http://xxx.xxx.xxx.xxx/led/on Then LED will be turned on.

http://xxx.xxx.xxx.xxx/led/on Then LED will be turned off.

Press GPIO 14 switch to request http to https://example.com/ .
