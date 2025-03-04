# BNBChainUAgents

This repository contains BNB transaction agents built using uAgents and Web3.py. The agents facilitate BNB transfers, transaction monitoring, and status verification on the BNB Testnet.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Environment Variables](#installation)
- [Usage](#usage)
- [Wallet Creation](#wallet-creation)
- [Output-Sample](#output-sample)

## Overview

This project provides BNB Chain agents that:

1. Send BNB Transactions using private keys securely stored in environment variables.
2. Verify Transaction Status via the BscScan API.
3. Monitor Wallet Activity.
4. Interact using uAgents framework for decentralized AI agent communication.

## Features

  ✅ Send BNB transactions on Testnet
  ✅ Verify transaction status using [BscScan API](https://docs.bscscan.com/api-endpoints/accounts)
  ✅ Securely store wallet credentials in .env file
  ✅ Asynchronous agent communication
  ✅ Monitor transactions for a given wallet

## Requirements

- **Python 3.11+**
- **pip** (Python package manager)
- **BNB Testnet account** (for sending transactions)
- [**BscScan API Key**](https://docs.bscscan.com/getting-started/viewing-api-usage-statistics) (for checking transaction status)

## Installation

1️⃣ Clone the Repository
```
git clone https://github.com/your-repo/bnb-chain-agents.git
```

2️⃣ Create a Virtual Environment
```
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

4️⃣ Setup Environment Variables
Create a `.env` file in the project directory:
```
touch .env
```

Edit the `.env` file and add your credentials:
```
USER_WALLET=0xYourWalletAddress
USER_KEY=YourPrivateKey
BSCSCAN_API_KEY=YourBscScanApiKey
```

## Usage

### Start Agent 1 (Transaction Sender)
```
python agent1.py
```

### Start Agent 2 (Transaction Validator)
```
python agent2.py
```

### Start Monitoring Agent
```
python monitor_wallet.py
```

### Send a BNB Transfer Request

```
curl -d '{"to_address": "0xReceiverWallet", "amount": 0.01, "agent_to_address": "agent1qv75qva6vhn54zasp6svczkwzxn3qugjrngx6zepq3xqtaquhuayy5s2v4e"}' \
     -H "Content-Type: application/json" -X POST http://localhost:8000/send/bnb
```

note : `agent_to_address` is the agent address for agent2 and it will verify the transaction and send a confirmation.

 ## Wallet Creation

If you need a new wallet, run:

```python
from eth_account import Account

new_account = Account.create()
print(f"New Wallet Address: {new_account.address}")
print(f"Private Key: {new_account.key.hex()}")

```

⚠️ **Save your private key securely! Do not share it or commit it to GitHub.**

## Output Sample

### Agent1.py

```
(venv) abhi@Fetchs-MacBook-Pro BNB Agent % python3 agent1.py
INFO:     [User BNB Agent to make transactions]: Starting agent with address: agent1qgrw5n9ttqtwxvzdwet9jjsgttqx3q4pnt5f9f5d5x2dyv476acrgx6gg79
INFO:     [User BNB Agent to make transactions]: Agent inspector available at https://agentverse.ai/inspect/?uri=http%3A//127.0.0.1%3A8000&address=agent1qgrw5n9ttqtwxvzdwet9jjsgttqx3q4pnt5f9f5d5x2dyv476acrgx6gg79
INFO:     [User BNB Agent to make transactions]: Starting server on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     [uagents.registration]: Registration on Almanac API successful
INFO:     [uagents.registration]: Almanac contract registration is up to date!
INFO:     [User BNB Agent to make transactions]: signed_tx : SignedTransaction(raw_transaction=HexBytes('0xf86c1685174876e80082520894129e995c5f229fb7677b663fb83bc427c1f276cf872386f26fc100008081e5a0219b06312719d73027703a11f692b9e85287efe103f708fe1c2ad6a02d8aa10fa048dca50f4e7b27ee44815a98e7f354a514b6adb78255542cbec1d73e3040a792'), hash=HexBytes('0x1d1ae447fc7230f40b1770c78ad77a0c8de9fdf373c0f911f270912981a5f461'), r=15200228033921717393673596159478329367546092732919419113946863340713400770831, s=32956370653057867147170960199694552170702326940711054580356120796838766880658, v=229)
INFO:     [User BNB Agent to make transactions]: ✅ Transaction Sent! Tx Hash: 0x1d1ae447fc7230f40b1770c78ad77a0c8de9fdf373c0f911f270912981a5f461
INFO:     [User BNB Agent to make transactions]: --------------- message : response='Successful transfer cofirmed by reciever.✅ tx_hash : 0x1d1ae447fc7230f40b1770c78ad77a0c8de9fdf373c0f911f270912981a5f461' ---------------------
INFO:     [User BNB Agent to make transactions]: --------------- status : MsgStatus(status=<DeliveryStatus.DELIVERED: 'delivered'>, detail='Message successfully delivered via HTTP', destination='agent1qv75qva6vhn54zasp6svczkwzxn3qugjrngx6zepq3xqtaquhuayy5s2v4e', endpoint='http://localhost:8001/submit', session=UUID('29521736-ae66-4db2-934a-352b37670dab')) ---------------------
```

### Agent2.py

```
(venv) abhi@Fetchs-MacBook-Pro BNB Agent % python3 agent2.py
INFO:     [Dummy BNB Agent to make transactions]: Starting agent with address: agent1qv75qva6vhn54zasp6svczkwzxn3qugjrngx6zepq3xqtaquhuayy5s2v4e
INFO:     [Dummy BNB Agent to make transactions]: Agent inspector available at https://agentverse.ai/inspect/?uri=http%3A//127.0.0.1%3A8001&address=agent1qv75qva6vhn54zasp6svczkwzxn3qugjrngx6zepq3xqtaquhuayy5s2v4e
INFO:     [Dummy BNB Agent to make transactions]: Starting server on http://0.0.0.0:8001 (Press CTRL+C to quit)
INFO:     [uagents.registration]: Registration on Almanac API successful
INFO:     [uagents.registration]: Almanac contract registration is up to date!
INFO:     [Dummy BNB Agent to make transactions]: Received transaction status request for: 0x1d1ae447fc7230f40b1770c78ad77a0c8de9fdf373c0f911f270912981a5f461
INFO:     [Dummy BNB Agent to make transactions]: Transaction status: {'status': '1', 'message': 'OK', 'result': {'isError': '0', 'errDescription': ''}}
INFO:     [Dummy BNB Agent to make transactions]: Reply: Successful transfer cofirmed by reciever.✅ tx_hash : 0x1d1ae447fc7230f40b1770c78ad77a0c8de9fdf373c0f911f270912981a5f461
```

### wallet_monitor.py

```
(venv) abhi@Fetchs-MacBook-Pro BNB Agent % python3 monitor_agent.py
INFO:     [Monitor BNB Agent to monitor address]: Starting agent with address: agent1q2l4mrp9pnqgyhqk2x6j30qgg4uccdgct2hpkheyyld27qjdqfxf7t6jn6j
INFO:     [Monitor BNB Agent to monitor address]: Agent inspector available at https://agentverse.ai/inspect/?uri=http%3A//127.0.0.1%3A8003&address=agent1q2l4mrp9pnqgyhqk2x6j30qgg4uccdgct2hpkheyyld27qjdqfxf7t6jn6j
INFO:     [Monitor BNB Agent to monitor address]: Starting server on http://0.0.0.0:8003 (Press CTRL+C to quit)
INFO:     [Monitor BNB Agent to monitor address]: No new blocks since last scan.
INFO:     [uagents.registration]: Registration on Almanac API successful
INFO:     [uagents.registration]: Almanac contract registration is up to date!
INFO:     [Monitor BNB Agent to monitor address]: Scanning blocks from 48790417 to 48790420...
INFO:     [Monitor BNB Agent to monitor address]: Recorded transaction: {
  "blockNumber": 48790420,
  "hash": "1d1ae447fc7230f40b1770c78ad77a0c8de9fdf373c0f911f270912981a5f461",
  "from": "0xAfEe66D9404bC93D73ae367cCE4e0ca8280462B6",
  "to": "0x129e995c5F229fB7677B663fb83Bc427C1F276cf",
  "value": "0.01 BNB"
}
INFO:     [Monitor BNB Agent to monitor address]: Scanning blocks from 48790421 to 48790423...
INFO:     [Monitor BNB Agent to monitor address]: Scanning blocks from 48790424 to 48790427...
```

### Curl Request

```
(venv) abhi@Fetchs-MacBook-Pro BNB Agent % curl -d '{"to_address": "0x129e995c5F229fB7677B663fb83Bc427C1F276cf", "amount": 0.01, "agent_to_address": "agent1qv75qva6vhn54zasp6svczkwzxn3qugjrngx6zepq3xqtaquhuayy5s2v4e"}' -H "Content-Type: application/json" -X POST http://localhost:8000/send/bnb
{"response": "Successful transfer cofirmed by reciever.\u2705 tx_hash : 0x1d1ae447fc7230f40b1770c78ad77a0c8de9fdf373c0f911f270912981a5f461"}%                  
```
