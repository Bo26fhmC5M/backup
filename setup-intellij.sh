#!/bin/bash

# setup-intellij.sh install
# setup-intellij.sh uninstall

if [[ "${1,,}" == "install" ]]; then
cd /opt
sudo curl -L https://download.jetbrains.com/idea/ideaIC-2023.3.4.tar.gz | sudo tar -xzv

sudo tee /usr/share/applications/intellij.desktop << 'EOF' > /dev/null
[Desktop Entry]
Version=2023.3.4
Type=Application
Name=IntelliJ
Icon=opt/idea-IC-233.14475.28/bin/idea.png
Exec=opt/idea-IC-233.14475.28/bin/idea.sh
Categories=Development;IDE;
Terminal=false
EOF

sudo chmod 644 /usr/share/applications/intellij.desktop
fi

if [[ "${1,,}" == "uninstall" ]]; then
sudo rm -f /usr/share/applications/intellij.desktop
sudo rm -rf /opt/idea-IC-*
fi