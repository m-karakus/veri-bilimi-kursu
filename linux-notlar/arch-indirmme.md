# Arch indirmek için kullandığımız komutlar

## Arch base indirme

1. Klavye düzenini ayarayalım  
`loadkeys trq`

2. Font Büyütelim  
`setfont ter-132b`

3. Wifi Bağlantısı Yapalım  
    `iwctl`  
    `device list`  
    `station w0 scan`  
    `station w0 get-networks`  
    `station w0 connect wifi-name`  
    `exit`

4. Disk bölümlerini ayarlayalım  
    `fdisk -l`  
    `fdisk /dev/sda`  
    `g`  
    `n` --> `+500M` -> EFI  
    `n` --> diskin tamamı -> Linux  
    `mkfs.fat -F32 /dev/sda1`  
    `mkfs.ext4 /dev/sda2`  
    
5. Saat ve tarihi ayarla  
    `timedatectl set-ntp true`

6. root bölümünü /mnt ye bağlıyoruz  
    `mount /dev/sda2 /mnt`  
    `mkdir /mnt/boot`  
    `mount /dev/sda1 /mnt/boot/`  
    `lsblk`  

7. Yeni bölümlari bağlayalım ve fstab güncelleyelim  
    `pacstrap /mnt base linux linux-firmware vim nano`  
    `genfstab -U  /mnt >> /mnt/etc/fstab`  
    `cat /mnt/etc/fstab`  

8. indirme işlemi  
    `arch-chroot /mnt`  
    `ln -sf /usr/share/zoneinfo/Europe/Istanbul /etc/localtime`  
    `hwclock --systohc`  
    `vim /etc/locale.gen`  
    `locale-gen`  
    `vim /etc/locale.conf`  
        bu dosyaya  
    
        ``` 
        LANG=en_US.UTF-8  
        LC_CTYPE=en_US.UTF-8  
        LC_ALL=en_US.UTF-8  
        ```  
9. Hostname ayarlama  
    `vim /etc/hostname`  
    `arch`  
    `vim /etc/hosts`  
    ```
    127.0.0.1   localhost  
    ::1         localhost
    127.0.1.1   arch.localdomain    arch
    ```   
10. swap  
    `fallocate -l 4GB /swapfile`  
    `chmod 600 /swapfile`  
    `mkswap /swapfile`  
    `swapon /swapfile`  
    `vim /etc/fstab`  
    ```
    /swapfile none swap defaults 0 0
    ```   

11. Kullanıcı ve parola oluşturma  
    `passwd`  
    `pacman -S grub efibootmgr networkmanager network-manager-applet wireless_tools wpa_supplicant dialog os-prober mtools dosfstools base-devel linux-headers`  
      
    `grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB`  
      
    `grub-mkconfig -o /boot/grub/grub.cfg`  
    `exit`

12. Çıkış  
    `umount -a`  
    `reboot`  

13. Internet Bağlantısı  
    `systemctl start NetworkManager`  
    `systemctl enable NetworkManager`  
    `nmtui`  

14. User ekleme  
    `useradd -m -G wheel mk`  
    `passwd mk`  
    `EDITOR=vim visudo`  
    ```
    %wheel ALL=(ALL) ALL   
    ```   
    `pacman -Syyu`  

---

## Arch DTOS indirme işlemi devamı

`sudo pacman -S git`  
`git clone https://gitlab.com/dwt1/dtos`  
`cd dtos`  
`./dtos`  

REF1: <https://www.youtube.com/watch?v=nyEmX6Gibf4&t=452s>  
REF2: <https://www.youtube.com/watch?v=nyEmX6Gibf4&t=452s>  

---

## Arch Xfce4 Indirme  
bilgisayarına göre aşağıdakilerden birini uygula  
```
pacman -S xf86-video-intel  
pacman -S xf86-video-amdgpu  
pacman -S nvidia nvidia-utils  
```  

`sudo pacman -S xorg`  
`sudo pacman -S lxdm`  
`sudo systemctl enable lxdm.service`  
`sudo pacman -S xfce4 xfce4-goodies pulseaudio pavucontrol xdg-user-dirs`  

`sudo pacman -S base-devel --needed`  
`git clone https://aur.archlinux.org/paru.git`  
`cd paru`  
`makepkg -si`  

