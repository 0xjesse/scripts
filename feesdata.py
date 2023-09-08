###fetches data for a list of NFT Marketplaces and converts output into CSV


import csv
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
        return fees_data
    else:
        print(f"Error: Failed to retrieve fees data for {protocol}.")
        return None

# Specify the list of protocol slugs here
protocol_slugs = ["Blur", "Opensea", "Looksrare", "Gem", "X2Y2"]

# Initialize list to store all data
all_data = []

for protocol in protocol_slugs:
    fees_data = get_protocol_fees(protocol)
    if fees_data:
        for day, fee in fees_data.items():
            all_data.append([protocol, day, fee])

# Specify the output file path
csv_file_path = "fees_data.csv"

# Write data to CSV file
with open(csv_file_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Protocol", "Day", "Fee"])  # Write header
    writer.writerows(all_data)  # Write data rows

print(f"Data saved to {csv_file_path}")