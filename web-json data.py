import json
from urllib.request import urlopen

# here girisagar46 is a username. Try with your username.
with urlopen("https://api.github.com/users/girisagar46") as response:
    source = response.read().decode('utf-8') #since, api responds with byte instead of char, we need to decode it
    
source_data = json.loads(source)
print(source_data)