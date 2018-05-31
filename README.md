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
Example

var antChain = neo.antChain('http://www.antchain.org/api/v1/');
antChain.getAddressBalance('AQVh2pG732YvtNaxEGkQUei3YA4cvo7d2i').then(function (result) {
    console.log(JSON.stringify(result, null, 2));
});

Output Log:

{
  "asset": [
    {
      "assetid": "c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b",
      "name": "AntShare",
      "value": "50000000"
    },
    {
      "assetid": "602c79718b16e442de58778e148d0b1084e3b2dffd5de6b7b16cee7969282de7",
      "name": "AntCoin",
      "value": "10000.00000001"
    }
  ],
  "address": "AQVh2pG732YvtNaxEGkQUei3YA4cvo7d2i"
}

antChain.getUnspentCoinsByAddress

antChain.getUnspentCoinsByAddress(addressHexString)

Get a list of all coins with a balance for each asset at an address
Parameters

String - The address to get the outstanding balance of each coin
Returns

Promise - The resolved promise will be an object that includes a list of all unspent coins
Example

var antChain = neo.antChain('http://www.antchain.org/api/v1/');
antChain.getUnspentCoinsByAddress('AQVh2pG732YvtNaxEGkQUei3YA4cvo7d2i').then(function (result) {
    console.log(JSON.stringify(result, null, 2));
});

Output Log:

[
  {
    "assetid": "c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b",
    "balance": "50000000",
    "list": [
      {
        "state": 1,
        "n": 0,
        "value": "50000000",
        "txid": "01a6e985c1c1da04996b3472f04dfcacc4384d8b5b2f21f17367ea92f6a9cb26"
      }
    ],
    "name": "小蚁股"
  },
  {
    "assetid": "602c79718b16e442de58778e148d0b1084e3b2dffd5de6b7b16cee7969282de7",
    "balance": "10000.00000001",
    "list": [
      {
        "state": 1,
        "n": 0,
        "value": "10000",
        "txid": "94cdb1088db24091a97da9d443258d992edb8a0c9fbf821393fa82597d382299"
      },
      {
        "state": 1,
        "n": 0,
        "value": "0.00000001",
        "txid": "240a8493228a5df1982e3c72618eecde208425c1d55f323fa728e42e8c93303c"
      }
    ],
    "name": "小蚁币"
  }
]

antChain.getCurrentBlockHeight

antChain.getCurrentBlockHeight()

Get the balance of an address at the latest known block height
Parameters

None
Returns

Promise - The resolved promise will include the height of the last produced block
Example

var antChain = neo.antChain('http://www.antchain.org/api/v1/');
antChain.getCurrentBlockHeight().then(function (result) {
    console.log(JSON.stringify(result, null, 2));
});

Output Log:

{
  "height": 1147253
}

The rest of the Rest

The remaining methods don't appear to be fully implemented in the back end- they return empty string. They are listed here for completeness

antChain.getBlockByHash(blockHash)
antChain.getBlockByHeight(blockHeight)
antChain.getTransactionByTxid(txId)
antChain.getCurrentBlock()

Example

var antChain = neo.antChain('http://www.antchain.org/api/v1/');
antChain.getBlockByHash('d42561e3d30e15be6400b6df2f328e02d2bf6354c41dce433bc57687c82144bf').then(function (result) {
    console.log(JSON.stringify(result, null, 2));
});

Output Log:

""
