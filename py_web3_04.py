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

web3_connection = Web3(Web3.HTTPProvider(node_provider))

global_gas = 4500000
global_gas_price = web3_connection.toWei(8, 'gwei')


def are_we_connected():
    print(f'Connected: {web3_connection.isConnected()}')


def get_nonce(ETH_address):
    transaction_count = web3_connection.eth.get_transaction_count(ETH_address)
    print(f'Transaction count: {transaction_count}')
    return transaction_count


def deploy_contract(lucky_number, amount_ETH, owner, signature):
    guess_number = web3_connection.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
    transaction_body = {
        'nonce': get_nonce(owner),
        'value': web3_connection.toWei(amount_ETH, 'ether'),
    }
    deployment = guess_number.constructor(lucky_number).buildTransaction(transaction_body)
    signed_transaction = web3_connection.eth.account.sign_transaction(deployment, signature)
    result = web3_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)
    print(f'tx hex: {result.hex()}')
    return result.hex()


if __name__ == '__main__':
    are_we_connected()
    # deploy_contract(lucky_number=7, amount_ETH=2, owner=address_1, signature=private_key_1)
