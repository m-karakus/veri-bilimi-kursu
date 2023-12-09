#!/bin/bash

sudo apt update
sudo sed -i "/#\$nrconf{restart} = 'i';/s/.*/\$nrconf{restart} = 'a';/" /etc/needrestart/needrestart.conf
sudo apt install nfs-kernel-server
sudo mkdir /srv/nfs/kubedata -p
sudo chown -R nobody:nogroup /srv/nfs/kubedata
sudo chmod 777 /srv/nfs/kubedata
echo "/srv/nfs/kubedata *(rw,sync,no_subtree_check,no_root_squash,no_all_squash,insecure)" | sudo tee /etc/exports
sudo exportfs -rav 
sudo systemctl restart nfs-kernel-server
sudo showmount -e localhost