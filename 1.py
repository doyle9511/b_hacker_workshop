import requests

block_height = 2817669
url = f"https://api.blockcypher.com/v1/btc/test3/blocks/{block_height}"

try:
    response = requests.get(url)
    response.raise_for_status()

    block_data = response.json()
    block_hash = block_data['hash']

    print(f"Block Hash for block {block_height} on Bitcoin Testnet3: {block_hash}")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred: {err}")