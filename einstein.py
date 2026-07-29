import sys
import requests

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument" )
try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

api_key = "b164c1238fbabab9731f732bd4150b13a8355b87daf342efea904a8740766c80"
url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

try:

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    bitcoin_price = float(data["data"]["priceUsd"])

except requests.RequestException:
    sys.exit("API Request failed")
except (KeyError, ValueError):
    sys.exit("Failed to parse API response")

total_cost = bitcoins * bitcoin_price

print(f"${total_cost:,.4f}")



