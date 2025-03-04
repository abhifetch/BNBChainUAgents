from eth_account import Account

new_account_user = Account.create()
print(f"New Wallet Address: {new_account_user.address}")
print(f"Private Key: {new_account_user.key.hex()}")


new_account_dummy = Account.create()
print(f"New Wallet Address: {new_account_dummy.address}")
print(f"Private Key: {new_account_dummy.key.hex()}")
