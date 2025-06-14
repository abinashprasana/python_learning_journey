"""
Pokemon Info Explorer

Author: Abinash Prasana

A command-line tool that fetches and displays details about Pokemon using the PokeAPI.
It allows users to input a Pokemon's name and returns its ID, height, weight, types, and abilities.
"""

import requests
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url = f"{base_url}pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"⚠ Pokemon '{name}' not found! (Status: {response.status_code})")
        return None

def display_pokemon_info(data):
    print("\n📋 Pokemon Information")
    print("-" * 30)
    print(f"Name   : {data['name'].capitalize()}")
    print(f"ID     : {data['id']}")
    print(f"Height : {data['height']}")
    print(f"Weight : {data['weight']}")
    types = [t['type']['name'].capitalize() for t in data['types']]
    print(f"Types : {', '.join(types)}")
    abilities = [a['ability']['name'].capitalize() for a in data['abilities']]
    print(f"Abilities : {', '.join(abilities)}")
    print("-" * 30)

def main():
    print("Welcome to Pokemon Info Explorer")
    while True:
        name = input("\n🔍Enter Pokemon Name (or types 'exit' to quit): ")
        if name.lower() == "exit":
            print("👋Goodbye, Trainer!")
            break
        info = get_pokemon(name)
        if info:
            display_pokemon_info(info)

if __name__ == "__main__":
    main()