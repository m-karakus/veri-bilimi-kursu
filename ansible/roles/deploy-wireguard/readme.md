# Enable VPN on the machines

1. Create VPN server  
2. Create client conf and save in `ansible/roles/enable-wireguard/files/wireguard/wg0.conf`  
3. Update [vpn-deamon-for-workers.yaml](./../../vpn-deamon-for-workers.yaml)  
4. Run 
    ```bash
    ansible-playbook vpn-deamon-for-workers.yaml
    ```
__NOTE__: change `wg0.conf` for each machine, It has to be unique. Othervise we can not reach the server via VPN IP