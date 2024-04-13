#!/bin/bash

printf "Startup script - $1 $2 \n"

export SFTP_USER=$1
export SFTP_USER_PWD=$2

sudo apt install ssh

sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config

sudo tee -a /etc/ssh/sshd_config > /dev/null <<EOT

Match Group $SFTP_USER
ChrootDirectory %h
X11Forwarding no
AllowTcpForwarding no
ForceCommand internal-sftp
EOT


sudo systemctl restart sshd

sudo groupadd $SFTP_USER

sudo useradd -G $SFTP_USER -d /srv/$SFTP_USER -s /sbin/nologin $SFTP_USER

sudo passwd $SFTP_USER_PWD

sudo mkdir -p /srv/$SFTP_USER

sudo chmod g+rx /srv/$SFTP_USER

sudo mkdir -p /srv/$SFTP_USER/data

sudo chown $SFTP_USER:$SFTP_USER /srv/$SFTP_USER/data

