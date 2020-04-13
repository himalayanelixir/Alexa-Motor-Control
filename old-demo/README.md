Links that are useful or might become useful: 

https://scribles.net/controlling-leds-on-raspberry-pi-using-voice-with-amazon-echo/
https://www.pubnub.com/blog/alexa-voice-controlled-raspberry-pi-using-lambda-and-pubnub/
https://gist.github.com/kbeflo/154d531ae5f5cb2766be3d8a15626342
https://www.everythingcli.org/ssh-tunnelling-for-fun-and-profit-autossh/

sudo apt-get update -y && sudo apt-get upgrade -y

sudo apt-get install rpi.gpio -y

sudo apt-get install python3-pip -y

# sudo apt-get install autossh 

pip3 install flask

pip3 install flask_ask

pip3 install 'cryptography<2.2'

wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip

unzip /path/to/ngrok.zip

./ngrok authtoken <YOUR_AUTH_TOKEN>

./ngrok http 80 (other port)




sudo nano /etc/systemd/system/autossh.service

sudo systemctl daemon-reload

sudo systemctl start autossh.service

sudo systemctl enable autossh.service

sudo systemctl list-unit-files | grep enabled

sudo nano /etc/systemd/system/alexamotor.service