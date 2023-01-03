# Virtual Box Linux Lite Kurulumu Notlar

## Snap Shot Almayı unutmayın

Video Link: <https://youtu.be/gQtZbUX2zHQ>

## Dosya Paylaşımı (Güncellendi 2023-01-03)

1. Bilgisayarı Başlat
2. Devices -> Shared Folders (Paylaşılan Klasorler) alanına git
3. Yeni bir dosya ekle
4. Dosya adına `codes` yaz
5. `Permanent` vs `Auto-mount` alanı seçili olsun, diğerini kaldır.
6. Devices -> Insert Guest Additions CD image menüsüne tıkla ve CD yi bilgisayara takmış ol.
7. Kullanıcıya yetki verelim.

    ```bash
    sudo adduser $USER vboxsf
    ```

8. Terminalden aşağıdaki komutları çalıştır.

    ```bash
    sudo mount /dev/cdrom /media/cdrom
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install build-essential linux-headers-`uname -r`
    sudo /media/cdrom/./autorun.sh
    sudo reboot
    ```

9. Bilgisayar yeniden başlatılacak. Sonrasında aşağıdaki kodlara devam edelim. 

    ```bash
    ln -s /media/sf_codes ~/codes
    cd ~/codes
    touch test.txt
    ```

10. Bilgisayarı yeniden başlaralım.

    ```bash
    sudo reboot
    ```
