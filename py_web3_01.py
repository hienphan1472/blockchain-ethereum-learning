from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

# declare this into .env file with your node provider url from infura
node_provider = os.environ['NODE_PROVIDER']

web3_connection = Web3(Web3.HTTPProvider(node_provider))


def are_we_connected():
    print(f'Connected: {web3_connection.isConnected()}')


def latest_block():
    print(f'Latest block: {web3_connection.eth.block_number}')


def balance_of(address):
    balance_wei = web3_connection.eth.get_balance(address)
    balance_ETH = web3_connection.fromWei(balance_wei, 'ether')
    print(f'Balance: {balance_ETH} ether')


if __name__ == '__main__':
    are_we_connected()
    latest_block()
    balance_of('0x3EcEf08D0e2DaD803847E052249bb4F8bFf2D5bB')

