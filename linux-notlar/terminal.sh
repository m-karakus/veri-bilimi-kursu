#!/bin/bash
# Read Password
# echo -n Password: 
# read -s password
# echo

sudo apt install vim git curl zsh -y
# echo $password
sudo chsh -s $(which zsh) $(whoami)
# echo $password

curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | bash && \
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions && \
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting && \
echo "changing the plugins" && sed -i 's/\(^plugins=([^)]*\)/\1 zsh-autosuggestions zsh-syntax-highlighting/' .zshrc| bash && \
cd ~ && source .zshrc && \
echo "Done"