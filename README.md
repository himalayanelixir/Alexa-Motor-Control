# Alexa Pi Furniture Control
<!-- vscode-markdown-toc -->
* [Summary](#Summary)
* [Setup](#Setup)
	* [Alexa](#Alexa)
	* [ngrok](#ngrok)
	* [Raspberry Pi](#RaspberryPi)
	* [Motor Driver](#MotorDriver)
* [Example](#Example)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='Summary'></a>Summary

This demo moves convertible furniture up and down using Alexa, a Raspberry Pi, and a motor driver. With a few small modifications you could control anything using GPIO on the Raspberry Pi.

![Diagram](https://raw.githubusercontent.com/himalayanelixir/alexa-pi-furniture-control/master/docs/alexa-pi-furniture-control.png)
<p align="center"><i>Entire system</i></p>

## <a name='Setup'></a>Setup

### <a name='Alexa'></a>Alexa

Use skills JSON in ```alexa/``` to create skills for your use case. Endpoints should be the ones from ngrok.

### <a name='ngrok'></a>ngrok

Use ngrok to serve as a message passer between the Alexa service and the Raspberry Pi. We need it because the Raspberry Pi doesn't have a static address we can use to find it.

You will need to subscribe to get reserved endpoint addresses. Follow the instructions on the website to setup the endpoints, and to connect it to the Raspberry Pi.

### <a name='RaspberryPi'></a>Raspberry Pi
This is an extremely manual process because I was in a rush when I initially wrote this up. It can be put into a simple bash script to run on firstboot. Sorry.

```bash
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install rpi.gpio -y
sudo apt-get install python3-pip -y
wget -q https://raw.githubusercontent.com/himalayanelixir/alexa-pi-furniture-control/master/raspberry-pi/requirements.txt /home/pi/
pip3 install -r /home/pi/requirements.txt
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
unzip /path/to/ngrok.zip
./ngrok authtoken <YOUR_AUTH_TOKEN>
# change port depending on what you setup flask-ask with
./ngrok http 80 (other port)
# create services (copied and pasted from raspberry-pi/services/)
sudo nano /etc/systemd/system/alexamotor.service
sudo nano /etc/systemd/system/ngrok.service
sudo systemctl start alexamotor.service
sudo systemctl enable alexamotor.service
sudo systemctl start ngrok.service
sudo systemctl enable ngrok.service
sudo systemctl daemon-reload
# make sure services are enabled
sudo systemctl list-unit-files | grep enabled
wget -q https://raw.githubusercontent.com/himalayanelixir/alexa-pi-furniture-control/master/raspberry-pi/motor_control.py /home/pi/
sudo chmod +x /home/pi/motor-control.py
```

### <a name='MotorDriver'></a>Motor Driver

To control the furniture you will just need a driver to communicate with from the Raspberry Pi to the motor. I used a simple Pololu G2 High-Power Motor
Driver 24v13. Just modify the GPIO pins that are turned on and off in ```raspberry-pi/motor-control.py``` to use a different one.

## <a name='Example'></a>Example

Got this code working with a convertible bed. The full video can be found here: <https://youtu.be/vljLdq9bu4k>.

<p align="center">
  <img src="https://raw.githubusercontent.com/himalayanelixir/alexa-pi-furniture-control/master/docs/alexa-pi-furniture-control.gif">
</p>
