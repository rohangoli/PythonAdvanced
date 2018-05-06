##https://www.tensorflow.org/install/install_linux#NVIDIARequirements

## Install pip and Virtualenv
sudo apt-get install python-pip python-dev python-virtualenv

## Create a Virtualenv environment
virtualenv --system-site-packages ~/TensorFlow

## Activate the Virtualenv environment
source ~/TensorFlow/bin/activate

## Ensure pip>=8.1 is installed
easy_install -U pip

## Install TensorFlow

pip install --upgrade tensorflow      # for Python 2.7
## pip3 install --upgrade tensorflow     # for Python 3.n
## pip install --upgrade tensorflow-gpu  # for Python 2.7 and GPU
## pip3 install --upgrade tensorflow-gpu # for Python 3.n and GPU

pip install tensorboard

