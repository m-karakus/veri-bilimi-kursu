#!/bin/bash

sudo apt update
sudo sed -i "/#\$nrconf{restart} = 'i';/s/.*/\$nrconf{restart} = 'a';/" /etc/needrestart/needrestart.conf

sudo mount -t nfs 10.3.0.1:/srv/nfs/kubedata /mnt # TODO: Change with NFS SERVER IP
sudo mount | grep kubedata && sudo umount /mnt 
