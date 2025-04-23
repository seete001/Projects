import requests

url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
response = requests.get(url, timeout=10)  # Add timeout to avoid hanging indefinitely

if response.status_code == 200:
    data = response.json()
    print(f"Current Bitcoin price: ${data['bitcoin']['usd']}")
else:
    print(f"Failed to retrieve data: {response.status_code}")
