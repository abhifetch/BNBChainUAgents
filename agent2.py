from uagents import Agent, Context, Model
from web3 import Web3
from web3.middleware import geth_poa_middleware
import os
from dotenv import load_dotenv
import asyncio
import requests

agent_dummy = Agent(
    name = 'Dummy BNB Agent to make transactions',
    port = 8001,
    endpoint = ['http://localhost:8001/submit']
)


# Load environment variables from .env file
load_dotenv()

# Retrieve BscScan API key from environment variables
BSCSCAN_API_KEY = os.getenv("BSCSCAN_API_KEY")
if not BSCSCAN_API_KEY:
    raise ValueError("BSCSCAN_API_KEY not found in environment variables.")


# Connect to BNB Chain Testnet
provider_url = "https://data-seed-prebsc-1-s1.binance.org:8545/"
web3 = Web3(Web3.HTTPProvider(provider_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

class RequestDetails(Model):
    tx_hash : str

class ResponseTransfer(Model):
    response : str

async def get_transaction_status(tx_hash: str) -> dict:
    """
    Uses the BscScan API to get the status of a transaction.
    Returns the JSON response as a dictionary.
    """
    base_url = "https://api.bscscan.com/api"
    params = {
        "module": "transaction",
        "action": "getstatus",
        "txhash": tx_hash,
        "apikey": BSCSCAN_API_KEY  # Replace with your actual API key
    }
    
    response = await asyncio.to_thread(requests.get, base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"HTTP error {response.status_code}"}

@agent_dummy.on_message(model=RequestDetails, replies={ResponseTransfer})
async def startup_handler(ctx: Context, sender: str, msg: RequestDetails):
    ctx.logger.info(f"Received transaction status request for: {msg.tx_hash}")
    tx_status = await get_transaction_status(msg.tx_hash)
    ctx.logger.info(f"Transaction status: {tx_status}")

    # Determine reply based on API response:
    if "error" in tx_status:
        reply = f"API Error: {tx_status['error']}"
    else:
        # Check that the API call was successful
        if tx_status.get("status") == "1" and tx_status.get("message") == "OK":
            if tx_status["result"].get("isError") == "0":
                reply = f"Successful transfer cofirmed by reciever.✅ tx_hash : {msg.tx_hash}"
            else:
                err_desc = tx_status["result"].get("errDescription", "Unknown error")
                reply = f"Transfer rejected: {err_desc}"
        else:
            reply = "Transfer status unknown or API response error."

    ctx.logger.info(f"Reply: {reply}")
    await ctx.send(sender, ResponseTransfer(response=reply))

if __name__ == "__main__":
    agent_dummy.run()
