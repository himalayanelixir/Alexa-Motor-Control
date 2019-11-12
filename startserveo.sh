https://gist.github.com/kbeflo/154d531ae5f5cb2766be3d8a15626342
https://www.everythingcli.org/ssh-tunnelling-for-fun-and-profit-autossh/


sudo nano /etc/systemd/system/autossh.service

sudo systemctl daemon-reload

sudo systemctl start autossh.service

sudo systemctl enable autossh.service

sudo systemctl list-unit-files | grep enabled

sudo nano /etc/systemd/system/alexamotor.service




requirements to run 

sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install rpi.gpio
sudo apt-get install python3-pip
sudo apt-get install autossh
pip3 install flask
pip3 install flask_ask
pip3 install 'cryptography<2.2'

