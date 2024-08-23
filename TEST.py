from web3 import Web3
import json

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Ensure connection is successful
assert web3.isConnected(), "Failed to connect to Ganache"

# Set default account for transactions
web3.eth.default_account = web3.eth.accounts[0]

# Load ABI and bytecode from compiled contract JSON file
contract_path = "./build/contracts/Counter.json"  # Update with correct path
with open(contract_path, 'r') as file:
    contract_json = json.load(file)
    contract_abi = contract_json['abi']
    contract_bytecode = contract_json['bytecode']

# Deploy the contract
Counter = web3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
tx_hash = Counter.constructor().transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
contract_address = tx_receipt.contractAddress

# Create contract instance
counter_contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Test: Increment the counter
def test_increment():
    # Call increment function
    tx_hash = counter_contract.functions.increment().transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    
    # Get updated counter value
    count = counter_contract.functions.viewCount().call()
    
    # Check if counter was incremented to 1
    assert count == 1, f"Test failed: expected 1, got {count}"
    print("Test passed: Counter incremented to 1.")

# Test: Decrement the counter
def test_decrement():
    # Call decrement function
    tx_hash = counter_contract.functions.decrement().transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    
    # Get updated counter value
    count = counter_contract.functions.viewCount().call()
    
    # Check if counter was decremented to 0
    assert count == 0, f"Test failed: expected 0, got {count}"
    print("Test passed: Counter decremented to 0.")

# Test: Reset the counter
def test_reset():
    # Call reset function
    tx_hash = counter_contract.functions.reset().transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    
    # Get updated counter value
    count = counter_contract.functions.viewCount().call()
    
    # Check if counter was reset to 0
    assert count == 0, f"Test failed: expected 0, got {count}"
    print("Test passed: Counter reset to 0.")

choose = input('''Choose your action:
[1] Test Number Increment
[2] Test Number Decremnt
[3] Test Number Reset''')

if choose == '1':
  test_increment()
elif choose == '2':
  test_decrement()
elif choose == '3':
  test_reset()
