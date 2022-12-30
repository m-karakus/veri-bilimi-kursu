# Virtual Box Linux Lite Kurulumu Notlar

## Snap Shot Almayı unutmayın

## Dosya Paylaşımı

1. Bilgisayarı Başlat
2. Devices -> Shared Folders (Paylaşılan Klasorler) alanına git
3. Yeni bir dosya ekle
4. Dosya adına `codes` yaz
5. `Permanent` alanı seçili olsun, diğerlerini kaldır.
6. Bilgisayarı başlat
7. Devices -> Insert Guest Additions CD image menüsüne tıkla ve CD yi bilgisayara takmış ol.
8. Terminalden aşağıdaki komutları çalıştır.

    ```bash
    sudo mount /dev/cdrom /media/cdrom
    sudo apt-get update
    sudo apt-get install build-essential linux-headers-`uname -r`
    sudo /media/cdrom/./VBoxLinuxAdditions.run
    sudo reboot
    ```

9. Bilgisayar yeniden başlatılacak. Sonrasında aşağıdaki kodlara devam edelim. 

    ```bash
    mkdir ~/codes
    sudo mount -t vboxsf codes ~/codes
    cd ~/codes
    ```

10. Dosya yolunu kalıcı kale getirelim. 

    ```bash
    whoami
    sudo nano /etc/fstab
    ```

11. Açılan Pencerede aşağıdaki satırları ekleyelim ve Ctrl+O ile kaydedelim vd Ctrl+x ile kapatalım

    ```bash
    codes	/home/<username>/codes	vboxsf	defaults	0	0
    ```

12. Modülleri düzeltmek için aşağıdaki kodu terminalde çalıştıralım. 

    ```bash
    sudo nano /etc/modules
    ```

13. `/etc/modules` dosyası açılacaktır, yeni bir satıra aşağıdaki yazıyı ekleyelim ve kaydedelim.

    ```bash
    vboxsf
    ```

14. Bilgisayarı yeniden başlaralım. 

    ```bash
    sudo reboot
    ```
