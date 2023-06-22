import argparse
import requests

def fetch_pokemon_info(pokemon):
    # Clean and format the Pokémon name or Pokédex number
    pokemon = str(pokemon).strip().lower()

    # Construct the API URL
    api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    # Send GET request to the PokéAPI
    response = requests.get(api_url)

    if response.status_code == 200:
        pokemon_info = response.json()
        return pokemon_info
    else:
        print("Failed to fetch Pokémon information. Error code:", response.status_code)
        return None

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Fetch Pokémon information')

# Add command line argument for the Pokémon name
parser.add_argument('pokemon', help='Specify the Pokémon name')

# Parse the command line arguments
args = parser.parse_args()

# Access the value of the Pokémon name argument
pokemon_name = args.pokemon

# Call the function to fetch Pokémon information
pokemon_info = fetch_pokemon_info(pokemon_name)

# Use the fetched Pokémon information
if pokemon_info:
    print("Pokémon information fetched successfully:")
    print("Name:", pokemon_info['name'])
    print("ID:", pokemon_info['id'])
    print("Height:", pokemon_info['height'])
    print("Weight:", pokemon_info['weight'])
    # Additional information can be accessed from the 'pokemon_info' dictionary
else:
    print("Failed to fetch Pokémon information.")