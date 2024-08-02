from web3 import Web3



def main():
  
  #connetct to ganache server (usually hosted in 127.0.0.1:7545
  w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

  #try to connect 
  if not w3.isConnected():
      print("Not connected to Ganache, try to re-launch the service")
      main()
  abi_input = input('Input the ABI of the smart contract you are trying to reach')
  print(f'ABI {abi_input} set for the contract')
  address_input = input('Input the address of the contract you are trying to reach')
  print(f'Address {address_input} set for the contract')
  
  abi = abi_input  #Connect to the smart contract ABI
  contract_address = address_input #Connect to the smart contract address

  # Create the istance for the contract
  contract = w3.eth.contract(address=contract_address, abi=abi)

  account = w3.eth.accounts[0]
  tx_hash = contract.functions.set(123).transact({'from': account})
  w3.eth.wait_for_transaction_receipt(tx_hash)

  ### From there the code must suite tehc ode of your contract.
  ### We are here working with th example from the tutorial
  # This lines in particulare are going to read the value of the smart contract we have created.
  stored_data = contract.functions.storedData().call()
  print(f"Stored data for the smart contract was: {stored_data}")


main()
