###fetches top 5 dexes of each chain
### creates file titled top_dexes.csv
### note a dex (decentralized exchange) can be the top dex across multiple networks/blockchains so there may be duplicates
import requests
import csv

MAX_DEXES_PER_CHAIN = 5

response = requests.get("https://api.llama.fi/protocols")
if response.status_code == 200:
     data = response.json()
     with open('top_dexes.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Url', 'Description', 'Chain', 'Twitter', 'TVL', 'Category'])
        for chain in ['BSC', 'Gnosis', 'OKXChain']:
            dexes = [protocol for protocol in data if 'category' in protocol and protocol['category'] == 'Dexes' and chain in protocol['chains']]
            dexes_sorted = sorted(dexes, key=lambda x: x['tvl'], reverse=True)[:MAX_DEXES_PER_CHAIN]
            for protocol in dexes_sorted:
                name = protocol['name']
                url = protocol['url']
                description = protocol.get('description', 'N/A')
                twitter = protocol.get('twitter', 'N/A')
                tvl = protocol.get('tvl', 'N/A')
                writer.writerow([name, url, description, chain, twitter, tvl, 'Dexes'])
                print("Name: ", name)
                print("Url: ", url)
                print("Description: ", description)
                print("Chain: ", chain)
                print("Twitter: ", twitter)
                print("TVL: ", tvl)
                print("Category: Dexes")
else:
    print("Request failed with status code: ", response.status_code)