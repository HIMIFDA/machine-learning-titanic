echo "Install all depedencies with pip"
pip3 install -r requirements.txt
echo "All depedencies has been installed"

echo "Train our model"
sudo mkdir model
python3 titanic.py
echo "Done"
echo "Model saved on /model"

echo "We are ready!"