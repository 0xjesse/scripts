'''retrieves all protocols from Defillama'''
import requests

response = requests.get("https://api.llama.fi/protocols")

if response.status_code == 200:
    data = response.json()
    for protocol in data:
        name = protocol['name']
        url = protocol['url']
        description = protocol.get('description',"N/A")
        chains = protocol.get('chains',[])
        twitter = protocol.get('twitter',"N/A")
        tvl = protocol.get('tvl',"N/A")
        chainTvls = protocol.get('chainTvls',"N/A")

        if "Arbitrum" in chains:
            print("Name: ", name)
            print("Url: ", url)
            print("Description: ", description)
            print("Chains: ", chains)
            print("Twitter: ", twitter)
            print("TVL: ", tvl)
            print("Chain TVLs: ", chainTvls)
else:
    print("Request failed with status code: ", response.status_code)