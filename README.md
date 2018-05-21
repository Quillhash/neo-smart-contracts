#Neo Smart Contracts

#Neo-python

#QuickStart 

##``` Clone the repo and cd ```

# Pull the Docker image
docker pull docker pull cityofzion/neo-privatenet

# Start a private network
docker run --rm -d --name neo-privatenet -p 20333-20336:20333-20336/tcp -p 30333-30336:30333-30336/tcp cityofzion/neo-privatenet

# Download the private network wallet
wget https://s3.amazonaws.com/neo-experiments/neo-privnet.wallet

# Create a Python 3.6 virtual environment and activate it
python3.6 -m venv venv
. venv/bin/activate

# Install neo-python
pip install neo-python

# Remove any old private chain database
rm -rf ~/.neopython/Chains/privnet*

# Start neo-python connected to the private net (-p), showing sc events (-v)
np-prompt -p -v


