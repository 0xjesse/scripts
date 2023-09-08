###fetches launchpad protocols
### prints out the results & creates a saved file titled launchpad_protocol.csv
import requests
import csv

response = requests.get("https://api.llama.fi/protocols")

if response.status_code == 200:
     data = response.json()
     with open('launchpad_protocol.csv', mode='w', newline='') as file:
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

            if category != "Dexes":
                continue     # ignores protocols not categorized as "Launchpad"

            writer.writerow([name, url, description, chains, twitter, tvl, protocol.get('chainTvls', "N/A"), category])
            print("Name: ", name)
            print("Url: ", url)
            print("Description: ", description)
            print("Chains: ", chains)
            print("Twitter: ", twitter)
            print("TVL: ", tvl)
            print("Category: ", category)

else:
    print("Request failed with status code: ", response.status_code)