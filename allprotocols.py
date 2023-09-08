# retrieves all protocols from Defillama with a tvl < 250000
import requests
import csv

response = requests.get("https://api.llama.fi/protocols")

if response.status_code == 200:
    data = response.json()
    with open('allprotocol_0908_Final.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Url', 'Description', 'Chains', 'Twitter', 'TVL', 'Chain TVLs', 'Category'])
        for protocol in data:
            name = protocol['name']
            url = protocol['url']
            description = protocol.get('description', "N/A")
            chains = protocol.get('chains', [])
            twitter = protocol.get('twitter', "N/A")
            tvl = protocol.get('tvl', "N/A")
            category = protocol.get('category', "N/A")

            if tvl is None or tvl < 250000:
                continue     # ignores protocols with TVL < 250,000

            writer.writerow([name, url, description, chains, twitter, tvl, category])

else:
    print("Request failed with status code: ", response.status_code)