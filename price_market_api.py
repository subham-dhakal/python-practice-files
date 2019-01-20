import json
from urllib.request import urlopen

#with urlopen("https://api.coinmarketcap.com/v1/ticker/?limit=10") as response:

source=urlopen("https://api.coinmarketcap.com/v1/ticker/?limit=10")
source_refined = source.read().decode('utf-8') #since, api responds with byte instead of char, we need to decode it
    
source_data = json.loads(source_refined)

for coin in source_data:
	USD=float(coin.get("price_usd"))
	print("The name of currency is  ",coin.get("name"))
	print("The rank is ",coin.get("rank"))
	print("The price in usd is ",coin.get("price_usd"))
	print("The price in NRP is ",USD*101.96)
	print()
	

	#We can also use string formatter like below:
	#print(f"{coin.get('name')}:{coin.get('price_usd')}")