#!/bin/bash
location="$HOME"
chmod +x ~/Mario_Pipe/remove.sh
cd $HOME
if [[ "$(id -u)" == 0 ]]; then
  echo "Mario pipe should not be installed as root!"
  sleep 5
  exit 1
fi
echo "Downloading Open CV"
sudo apt install python3-opencv
echo "Creating application"

mkdir -p ~/.local/share/applications
echo "[Desktop Entry]
Name=Mario Pipe
Comment=Hacked NES simple code
Exec=python3  ${location}/Mario_Pipe/mario_pipe.py
Icon=${location}/Mario_Pipe/mario.png
Terminal=true
Type=Application
Categories=Programming;
StartupNotify=true" > ~/.local/share/applications/Mario_pipe.desktop

echo "#!/bin/bash
python3  ${location}/Mario_Pipe/mario_pipe.py"' "$@"' | sudo tee /usr/local/bin/Mario mkdir -p /usr/local/bin
sudo chmod +x /usr/local/bin/Mario
