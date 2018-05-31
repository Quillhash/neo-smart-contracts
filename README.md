#Neo Smart Contracts

#Neo-python

#QuickStart 

#``` Clone the repo and cd ```

# Pull the Docker image
docker pull cityofzion/neo-privatenet

# Start a private network
docker run --rm -d --name neo-privatenet -p 20333-20336:20333-20336/tcp -p 30333-30336:30333-30336/tcp cityofzion/neo-privatenet

# Download the private network wallet or create new wallet (neo-privnet-sample.wallet)
wget https://s3.amazonaws.com/neo-experiments/neo-privnet.wallet

# Create a Python 3.6 virtual environment and activate it
python3.6 -m venv venv 
source venv/bin/activate

# Install neo-python
pip install neo-python

# Remove any old private chain database
rm -rf ~/.neopython/Chains/privnet*

# Start neo-python connected to the private net (-p), showing sc events (-v)
np-prompt -p -v

# AntChain REST Service

## Overview

AntChain REST Service provides a quick and easy way for applications to check for public information about a blockchain including wallet balance. The same information can be found by navigating directly to the website.

The endpoint for this service is located at http://www.antchain.org/api. There is also a Test Net version at http://testnet.antchain.org/api

# API Methods

## antChain.getAddressBalance

antChain.getAddressBalance(addressHexString)

Get the balance of an address at the last known block height
Parameters

String - The address to get the total balance of each asset
Returns

Promise - The resolved promise will be an object that includes the total balances of each asset found at the Address

antChain.getUnspentCoinsByAddress

antChain.getUnspentCoinsByAddress(addressHexString)

Get a list of all coins with a balance for each asset at an address
Parameters

String - The address to get the outstanding balance of each coin
Returns

Promise - The resolved promise will be an object that includes a list of all unspent coins

antChain.getCurrentBlockHeight

antChain.getCurrentBlockHeight()

Get the balance of an address at the latest known block height
Parameters

None
Returns

Promise - The resolved promise will include the height of the last produced block

The rest of the Rest

The remaining methods don't appear to be fully implemented in the back end- they return empty string. They are listed here for completeness

antChain.getBlockByHash(blockHash)
antChain.getBlockByHeight(blockHeight)
antChain.getTransactionByTxid(txId)
antChain.getCurrentBlock()

### For Detailed Info -> /neo-api-js
