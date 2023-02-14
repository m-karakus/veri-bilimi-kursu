# Terminal Güncelleme

```bash
sudo apt install vim git curl zsh && \
chsh -s /bin/zsh && \
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" && \
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions && \
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting && \ 
sed 's/\(^plugins=([^)]*\)/\1 zsh-autosuggestions zsh-syntax-highlighting/' .zshrc 
```


