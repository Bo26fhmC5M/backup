#!/bin/bash

# setup-pycharm.sh install
# setup-pycharm.sh uninstall

if [[ "${1,,}" == "install" ]]; then
cd /opt
sudo curl -L https://download.jetbrains.com/python/pycharm-community-2023.3.4.tar.gz | sudo tar -xzv

sudo tee /usr/share/applications/pycharm.desktop << 'EOF' > /dev/null
[Desktop Entry]
Version=2023.3.4
Type=Application
Name=PyCharm
Icon=/opt/pycharm-community-2023.3.4/bin/pycharm.png
Exec=/opt/pycharm-community-2023.3.4/bin/pycharm.sh
Categories=Development;IDE;
Terminal=false
EOF

sudo chmod 644 /usr/share/applications/pycharm.desktop
fi

if [[ "${1,,}" == "uninstall" ]]; then
sudo rm -f /usr/share/applications/pycharm.desktop
sudo rm -rf /opt/pycharm-community-*
fi