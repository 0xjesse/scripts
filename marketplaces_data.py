###fetches fees data for a list of NFT Marketplaces

import requests

def get_protocol_fees(protocol):
    base_url = "https://api.llama.fi/summary/fees/"
    data_type = "dailyFees"
    url = f"{base_url}{protocol}?dataType={data_type}"

    response = requests.get(url)
    if response.status_code == 200:
        fees_data = response.json()
        print(f"Fees for {protocol}:")
        for day, fee in fees_data.items():
            print(f"{day}: {fee}")
    else:
        print(f"Error: Failed to retrieve fees data for {protocol}.")

# Specify the list of protocol slugs here
protocol_slugs = ["Blur", "Opensea", "Looksrare", "X2Y2"]

for protocol in protocol_slugs:
    get_protocol_fees(protocol)
    print()  # Add an empty line between each protocol's fees