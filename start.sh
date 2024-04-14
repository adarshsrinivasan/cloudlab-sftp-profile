#!/bin/bash

printf "Startup script - $1 $2 \n"

export SFTP_USER=$1
export SFTP_USER_PWD=$2

sudo apt update

sudo apt install ssh

sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config

sudo tee -a /etc/ssh/sshd_config > /dev/null <<EOT

Match Group $SFTP_USER
ChrootDirectory /var/sftp/$SFTP_USER
X11Forwarding no
AllowTcpForwarding no
ForceCommand internal-sftp
EOT


sudo systemctl restart sshd

sudo groupadd $SFTP_USER

sudo useradd -g $SFTP_USER -d /var/sftp/$SFTP_USER -s /sbin/nologin $SFTP_USER

echo -e "$SFTP_USER_PWD\n$SFTP_USER_PWD" | sudo passwd $SFTP_USER

sudo mkdir -p /var/sftp/$SFTP_USER

sudo chmod 770 /var/sftp/$SFTP_USER

sudo chown $SFTP_USER:$SFTP_USER /var/sftp/$SFTP_USER

