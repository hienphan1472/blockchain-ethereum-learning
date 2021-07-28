from web3 import Web3
from dotenv import load_dotenv
import os


load_dotenv()
node_provider = os.environ['NODE_PROVIDER_LOCAL']
address_1 = os.environ['ADDRESS_1']
address_2 = os.environ['ADDRESS_2']
private_key_1 = os.environ['PRIVATE_KEY_1']
web3_connection = Web3(Web3.HTTPProvider(node_provider))

global_gas = 4500000
global_gas_price = web3_connection.toWei(8, 'gwei')


def are_we_connected():
    print(f'Connected: {web3_connection.isConnected()}')


def get_nonce(ETH_address):
    return web3_connection.eth.get_transaction_count(ETH_address)


def transfer_ETH(sender, receiver, signature, amount_ETH):
    transaction_body = {
        'nonce': get_nonce(sender),
        'to': receiver,
        'value': web3_connection.toWei(amount_ETH, 'ether'),
        'gas': global_gas,
        'gasPrice': global_gas_price
    }
    signed_signature = web3_connection.eth.account.sign_transaction(transaction_body, signature)
    result = web3_connection.eth.send_raw_transaction(signed_signature.rawTransaction)
    print(f'tx hash: {result.hex()}')
    return result


if __name__ == '__main__':
    are_we_connected()
    transfer_ETH(address_1, address_2, private_key_1, 2)
