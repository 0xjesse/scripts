### fetches projects compatible with the Arbitrum network (and arent Centralized Exchanges i.e., CEX)
### files is saved as arbitrum-protocols.csv
import csv
import requests

response = requests.get("https://api.llama.fi/protocols")

if response.status_code == 200:
    data = response.json()
    with open('arbitrum-protocols.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Url', 'Description', 'Chains', 'Twitter', 'TVL', 'Chain TVLs', 'Category'])
        for protocol in data:
            name = protocol['name']
            url = protocol['url']
            description = protocol.get('description', "N/A")
            chains = protocol.get('chains', [])
            twitter = protocol.get('twitter', "N/A")
            tvl = protocol.get('tvl', "N/A")
            chainTvls = protocol.get('chainTvls', "N/A")
            category = protocol.get('category', "N/A")

            if "Arbitrum" in chains and category != "CEX":
                writer.writerow([name, url, description, chains, twitter, tvl, chainTvls, category])
else:
    print("Request failed with status code: ", response.status_code)