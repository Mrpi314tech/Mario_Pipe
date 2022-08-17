#!/bin/bash
location="$HOME"
cd $HOME
if [[ "$(id -u)" == 0 ]]; then
  echo "Mario pipe should not be installed as root!"
  sleep 5
  exit 1
fi
echo "Downloading Open CV"
pip install opencv-python
echo "Creating application"

mkdir -p ~/.local/share/applications
echo "[Desktop Entry]
Name=UC37
Comment=UC37 the AI
Exec=python3  ${location}/Mario_Pipe/mario_pipe.py
Icon=${location}/Mario_Pipe/mario.png
Terminal=true
Type=Application
Categories=Programming;
StartupNotify=true" > ~/.local/share/applications/UC37.desktop

echo "#!/bin/bash
python3  ${location}/Mario_Pipe/mario_pipe.py"' "$@"' | sudo tee /usr/local/bin/Mario mkdir -p /usr/local/bin
sudo chmod +x /usr/local/bin/Mario
