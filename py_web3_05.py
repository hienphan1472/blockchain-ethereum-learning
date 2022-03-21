from web3 import Web3
from dotenv import load_dotenv
import os
import json


load_dotenv()
node_provider = os.environ['NODE_PROVIDER_LOCAL']
address_1 = os.environ['ADDRESS_1']
address_2 = os.environ['ADDRESS_2']
private_key_1 = os.environ['PRIVATE_KEY_1']
private_key_2 = os.environ['PRIVATE_KEY_2']
contract_abi = json.loads(os.environ['CONTRACT_ABI'])
contract_bytecode = os.environ['CONTRACT_BYTECODE']
contract_address = os.environ['CONTRACT_ADDRESS']

web3_connection = Web3(Web3.HTTPProvider(node_provider))

global_gas = 4500000
global_gas_price = web3_connection.toWei(8, 'gwei')


def are_we_connected():
    print(f'Connected: {web3_connection.isConnected()}')


def get_balance():
    contract = web3_connection.eth.contract(address=contract_address, abi=contract_abi)
    balance_contract = web3_connection.fromWei(contract.functions.getBalance().call(), 'ether')
    print(f'Current contract balance: {balance_contract}')
    return balance_contract


def play(player, guess_number, amount_ETH, signature):
    contract = web3_connection.eth.contract(address=contract_address, abi=contract_abi)
    player = Web3.toChecksumAddress(player)


if __name__ == '__main__':
    are_we_connected()
    get_balance()
