# Key Setup for The New Servers

1. First of all, create servers/instances. Choose Ubuntu or Debian distro (Current: Ubuntu 22.04) 
2. __Ideally open all ports and disable firewall we will handle it by kubernetes.__ But if not acceptable these are needs to be open: ports TCP/UDP
   1. 80 --> HTTP
   2. 443 --> HTTPS
   3. 6443 --> Kubernetes Default
   4. 51820 --> Wireguard VPN
   4. 51821 --> Wireguard VPN UI
3. No need for Digital Ocean but for AWS you can do the LoadBalancing for 6443 master TCP
4. Get the SSH PEM keys from Server Provider `provider.pem`  and download it in this folder.
5. Add `ansible` key to the each server by using below steps. 

## Keys
1. Go the this inse of this folder from terminal  
   ```sh
   cd kube_setup/keys/

   # copy ansible keys to your local .ssh folder
   # these keys created wit this command: 
   # ssh-keygen -t ed25519 -C "ansible"
   cp ansible.pub  ~/.ssh/ansible.pub 
   cp ansible  ~/.ssh/ansible
   ```
1. Create `ansible` user... Run below command on remote server    
   ```bash
   # to connect servers, update the user and ip 
   username=root
   ip="16.171.113.56"
   ssh -i id_ed25519 $username@$ip 
   ```  
   ```bash
   username=ansible
   sudo adduser --disabled-password $username
   sudo passwd -d $username
   sudo usermod -aG sudo $username
   su - $username
   ```
1. Check user... run below command to check if everythins is ok  
   ```bash
   sudo -v && echo "All good" || echo "User is not in sudo group."
   ```
1. After the creation of user you can close the session or open a new terminal. 
   ```bash
   # one for ansible user
   exit
   # one for closıng the connection
   exit
   ```
1. Copy `ansible` key to the servers... run below command __on your local machine__  
   ```bash
   cat ~/.ssh/ansible.pub | \
      ssh -i provider.pem $username@$ip \
      "sudo mkdir -p  /home/ansible/.ssh; \
      sudo chmod 700 /home/ansible/.ssh; \
      sudo tee -a /home/ansible/.ssh/authorized_keys; \
      sudo chmod 600 /home/ansible/.ssh/authorized_keys; \
      sudo chown -R ansible:ansible /home/ansible/.ssh"
   ```  
1. Repeat steps for the all serves. [2 to 5]
2. Add/Update [argo](../../roles/ssh-keys/files/argo) ssh keys to the GIT/GITHUB/GITLAB repo as __deploy keys__. So ArgoCD can read yamls from there.  

