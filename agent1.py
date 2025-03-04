from uagents import Agent, Context, Model
from web3 import Web3
from web3.middleware import geth_poa_middleware
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

agent_user = Agent(
    name = 'User BNB Agent to make transactions',
    port = 8000,
    endpoint = ['http://localhost:8000/submit']
)

class RequestTransfer(Model):
    to_address : str
    amount : float
    agent_to_address : str

class RequestDetails(Model):
    tx_hash : str

class ResponseTransfer(Model):
    response : str

# Agent to which we send confirmation message
second_agent_address = 'agent1qv75qva6vhn54zasp6svczkwzxn3qugjrngx6zepq3xqtaquhuayy5s2v4e'

# Get wallet address and key from environment variables
user_wallet = os.getenv("USER_WALLET")
user_key = os.getenv("USER_KEY")

# Connect to BNB Chain Testnet
provider_url = "https://data-seed-prebsc-1-s1.binance.org:8545/"
web3 = Web3(Web3.HTTPProvider(provider_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

@agent_user.on_rest_post("/send/bnb", RequestTransfer, ResponseTransfer)
async def handle_post(ctx: Context, req: RequestTransfer) -> ResponseTransfer:
    try:
        # Convert addresses to checksum format
        to_address = web3.to_checksum_address(req.to_address)
        
        # Get the nonce (transaction count)
        nonce = web3.eth.get_transaction_count(user_wallet)

        # Set transaction parameters
        tx = {
            'to': to_address,
            'value': web3.to_wei(req.amount, 'ether'),
            'gas': 21000,  # Standard for simple BNB transfer
            'gasPrice': web3.eth.gas_price,
            'nonce': nonce,
            'chainId': 97  # BNB Testnet Chain ID
        }

        # Sign the transaction
        signed_tx = web3.eth.account.sign_transaction(tx, user_key)
        ctx.logger.info(f"signed_tx : {signed_tx}")

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        ctx.logger.info(f"✅ Transaction Sent! Tx Hash: {web3.to_hex(tx_hash)}")

        # Send a message to the second agent with the transaction hash
        message, status = await ctx.send_and_receive(
            req.agent_to_address,
            RequestDetails(tx_hash=web3.to_hex(tx_hash)),
            response_type=ResponseTransfer
        )
        ctx.logger.info(f'--------------- message : {message} ---------------------')
        ctx.logger.info(f'--------------- status : {status} ---------------------')
        return ResponseTransfer(
        response = message.response
    )
    
    except Exception as e:
        print(f"❌ Transaction Failed: {e}")

if __name__ == "__main__":
    agent_user.run()
