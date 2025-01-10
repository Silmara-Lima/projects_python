import requests

option = input("n/Choose what user StarWars data you'd like?")
option = option.strip()
option = str.lower(option)

def fetch_data(option):
  url = (f"https://swapi.mimo.dev/api/{option}/")
  data = []
    
  try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    print(f"Successfully fetched {len(data)} entities")
  except requests.HTTPError as e:
    print(f"Error fetching data: {e}")
    return None

  return data

data = fetch_data(option)

if data:
    for entity in data:
      print(entity["name"])
else:
  print("Unable to download data")