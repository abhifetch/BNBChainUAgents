# BNBChainUAgents

This repository contains BNB transaction agents built using uAgents and Web3.py. The agents facilitate BNB transfers, transaction monitoring, and status verification on the BNB Testnet.

## Table of Contents

- Overview
- Features
- Requirements
- Installation
- Environment Variables
- Usage
- Agents
  - Agent 1 - Transaction Sender
  - Agent 2 - Transaction Validator
- Monitor Agent (Future Work)
- Wallet Creation
- Future Enhancements

## Overview

This project provides BNB Chain agents that:

1. Send BNB Transactions using private keys securely stored in environment variables.
2. Verify Transaction Status via the BscScan API.
3. Monitor Wallet Activity (planned feature).
4. Interact using uAgents framework for decentralized AI agent communication.

## Features

  ✅ Send BNB transactions on Testnet
  ✅ Verify transaction status using [BscScan API](https://docs.bscscan.com/api-endpoints/accounts)
  ✅ Securely store wallet credentials in .env file
  ✅ Asynchronous agent communication
  🔜 Monitor transactions for a given wallet (Future Work)

## Requirements

- **Python 3.11+**
- **pip** (Python package manager)
- **BNB Testnet account** (for sending transactions)
- [**BscScan API Key**](https://docs.bscscan.com/getting-started/viewing-api-usage-statistics) (for checking transaction status)
