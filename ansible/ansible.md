# Ansible Run Steps

1. Do the [keys](./kube_setup/keys/key_setup.md) step if it is not done yet. 
1. Install Ansible  
   ```bash
   pip install --user ansible
   ```
1. Update below files/folders with your credentials...  
   1. [`inventory`](./inventory.yaml)  file
   2. [`host_vars`](./host_vars/) folder
   3. [`kube_setup`](./kube_setup/) folser

1. Test the connection. On terminal come to [`ansible`](./) folder and run the code... 
   ```bash
   ansible-playbook ping.yaml
   ```
1. You can see the server informations via this command
   ```bash
   ansible all -m gather_facts

   IP="161.35.64.182"
   ansible all -m gather_facts --limit $IP 
   ```  
5. Kubernetes & VPN Installation
   - There are different Kubernetes type. If you are testing it, If you have low resources, ıf your machine has less then 2GB Ram then use `K3S`...  
   - If you have enough resources, If you will use Kubernetes on production then use [`K8S`](#k8s-installation)...  

## K8S Installation...  
1. Run below command... 
   ```bash
   ansible-playbook k8s-full-kubernetes-install.yaml
   ```
