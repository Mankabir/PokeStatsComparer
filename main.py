import requests
from pokemon import Pokemon 

def main():
    # Create Pokemon instances
    poke_1 = Pokemon(input('Choose your pokemon: '))
    poke_2 = Pokemon(input('Choose your pokemon: '))

    # Compare their stats
    poke_1.compare_stats(poke_2)


if __name__ == "__main__":
    main()
