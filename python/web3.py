# Here's a Python code snippet using the `web3.py` library for interacting with Ethereum:


from web3 import Web3

# Connect to an Ethereum node
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Check connection status
if web3.isConnected():
    print("Connected to Ethereum node")
else:
    print("Failed to connect to Ethereum node")

# Get the latest block number
block_number = web3.eth.block_number
print("Latest block number:", block_number)

# Get the balance of an Ethereum address
address = '0x1234567890abcdef...'
balance = web3.eth.get_balance(address)
print("Balance:", web3.fromWei(balance, 'ether'), "ETH")


# In this code snippet, we're using the `web3.py` library to connect to an Ethereum node and perform basic operations.

# To use `web3.py`, you'll need to install it first by running `pip install web3` in your Python environment.

# Here's a breakdown of the code:

# 1. We create a `Web3` object and connect to an Ethereum node using `Web3.HTTPProvider`.
# Replace `'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'` with your own Infura project ID or the URL of your Ethereum node.

# 2. We check if the connection to the Ethereum node is successful using `web3.isConnected()`.

# 3. We retrieve the latest block number using `web3.eth.block_number` and print it.

# 4. We get the balance of an Ethereum address using `web3.eth.get_balance`. Replace `'0x1234567890abcdef...'` with the actual Ethereum address you want to check.

# 5. Finally, we print the balance in Ether by converting it from Wei to Ether using `web3.fromWei`.

# You can modify and extend this code snippet to interact with smart contracts, send transactions, or perform more advanced operations using the `web3.py` library.
# Refer to the `web3.py` documentation (https://web3py.readthedocs.io) for more information and examples.