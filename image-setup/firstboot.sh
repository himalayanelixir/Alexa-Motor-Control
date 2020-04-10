#!/bin/bash

# gives a bit of time for the wifi to connect
sleep 20
# enable ssh
sudo systemctl enable ssh
# update and upgrade 
sudo apt-get update -y
sudo apt-get upgrade -y
# install programs
sudo apt-get install expect git zsh python3-pip python3-venv -y
# change default shell for root and pi users
sudo chsh -s /bin/zsh pi
sudo chsh -s /bin/zsh
# install ohmyzsh for root and pi users
sudo -u pi sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
sudo sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended


# install drivers for inkyphat screen
wget https://get.pimoroni.com/inky -P /home/pi
# make downloaded script executable
chmod +x /home/pi/inky
# create script that uses expect to automate adafruit installation prompts
cat <<EOT >/home/pi/script.exp
#!/usr/bin/expect -f
set timeout -1
spawn ./inky
match_max 100000
expect -exact "Do you wish to continue? \[y/N\] "
send -- "y\r"
expect -exact "Do you wish to perform a full install? \[y/N\] "
send -- "y\r"
expect eof
EOT
# make script executable 
chmod +x /home/pi/script.exp
# run automation script which installs the adafruit screen drivers
chown pi /home/pi/script.exp
chown pi /home/pi/inky
su -c '/home/pi/script.exp' - pi
# remove the screen installation script
rm /home/pi/inky
# remove expect automation script
rm /home/pi/script.exp


# tell pi to restart after one minute. This is needed for the ssh changes to work and for the adafruit screen drivers
sudo shutdown -r 1