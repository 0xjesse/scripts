import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Define the API endpoint
url = "https://api.llama.fi/protocol/uniswap"

# Get the current date
end_date = datetime.now()

# Get the date 3 months ago
start_date = end_date - timedelta(days=90)

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON
    data = response.json()

    # Extract the dates and TVL values
    dates = [datetime.fromtimestamp(item["date"]) for item in data["tvl"] if start_date <= datetime.fromtimestamp(item["date"]) <= end_date]
    tvl_values = [item["totalLiquidityUSD"] for item in data["tvl"] if start_date <= datetime.fromtimestamp(item["date"]) <= end_date]

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(dates, tvl_values)
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xlabel('Date')
    plt.ylabel('TVL (USD)')
    plt.title('Uniswap TVL Over the Last 3 Months')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

else:
    print(f"Failed to get data: {response.content}")