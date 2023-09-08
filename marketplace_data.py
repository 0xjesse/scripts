###fetches data from 1 NFT marketplaces

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
        print("Error: Failed to retrieve fees data.")

# Specify the protocol slug here
protocol_slug = "LooksRare"
get_protocol_fees(protocol_slug)