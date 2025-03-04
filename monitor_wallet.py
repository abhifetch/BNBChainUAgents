from uagents import Agent, Context
from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get wallet address and key from environment variables
user_wallet = os.getenv("USER_WALLET")

monitor_agent = Agent(
    name='Monitor BNB Agent to monitor address',
    port=8003,
    endpoint=['http://localhost:8003/submit']
)

# Connect to BNB Chain Testnet
provider_url = "https://data-seed-prebsc-1-s1.binance.org:8545/"
web3 = Web3(Web3.HTTPProvider(provider_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Address to monitor
monitored_address = web3.to_checksum_address(user_wallet)

# Keep track of the last block we scanned
last_scanned_block = web3.eth.block_number

@monitor_agent.on_interval(period=10)
async def monitor_handler(ctx: Context):
    global last_scanned_block

    try:
        current_block = web3.eth.block_number
        if current_block <= last_scanned_block:
            ctx.logger.info("No new blocks since last scan.")
            return

        ctx.logger.info(f"Scanning blocks from {last_scanned_block+1} to {current_block}...")

        for block_num in range(last_scanned_block + 1, current_block + 1):
            block = web3.eth.get_block(block_num, full_transactions=True)
            for tx in block['transactions']:
                tx_from = tx['from']
                tx_to = tx['to']
                # Check if monitored address is involved
                if (tx_from and tx_from.lower() == monitored_address.lower()) or \
                   (tx_to and tx_to.lower() == monitored_address.lower()):
                    details = {
                        "blockNumber": block_num,
                        "hash": tx['hash'].hex(),
                        "from": tx_from,
                        "to": tx_to if tx_to else "Contract Creation",
                        "value": str(web3.from_wei(tx['value'], 'ether')) + " BNB"
                    }
                    ctx.logger.info(f"Recorded transaction: {json.dumps(details, indent=2)}")

        # Update last scanned block
        last_scanned_block = current_block

    except Exception as e:
        ctx.logger.error(f"Error during monitoring: {e}")

if __name__ == "__main__":
    monitor_agent.run()
