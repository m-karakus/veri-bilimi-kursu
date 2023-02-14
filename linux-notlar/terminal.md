# Terminal Güncelleme

```bash
sudo apt install vim git curl zsh -y && \
chsh -s /bin/zsh && \
curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | bash && \
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions && \
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting && \
echo "changing the plugins" && sed -i 's/\(^plugins=([^)]*\)/\1 zsh-autosuggestions zsh-syntax-highlighting/' .zshrc| bash && \
echo "Done"
```


sudo apt install curl zsh -y && curl -fsSL https://raw.githubusercontent.com/m-karakus/veri-bilimi-kursu/main/linux-notlar/terminal.sh | bash