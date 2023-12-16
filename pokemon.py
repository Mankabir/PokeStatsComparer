import requests

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.stats = self.get_pokemon_stats()

    def get_pokemon_stats(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.name}"
        try:
            data = requests.get(url)
            data.raise_for_status()  # Raise an exception for non-successful status codes
            json_data = data.json()
            stats = json_data["stats"]

            stats_dict = {}
            for stat in stats:
                stat_name = stat["stat"]["name"]
                base_stat = stat["base_stat"]
                stats_dict[stat_name] = base_stat
            return stats_dict
        except requests.exceptions.RequestException as errormsg:
            print(f"An error occurred while fetching data for {self.name}: {str(errormsg)}")
            return {}

    def compare_stats(self, other_pokemon):
        if not self.stats:
            print(f"Stats not available for {self.name}. Comparison cannot be performed.")
            return
        if not other_pokemon.stats:
            print(f"Stats not available for {other_pokemon.name}. Comparison cannot be performed.")
            return

        print(f"Comparing stats between {self.name.capitalize()} and {other_pokemon.name.capitalize()}:")
        for stat in self.stats:
            if stat in other_pokemon.stats:
                self_value = self.stats[stat]
                other_value = other_pokemon.stats[stat]
                if self_value > other_value:
                    print(f"{self.name.capitalize()} has higher {stat}: {self_value} > {other_value}")
                elif self_value < other_value:
                    print(f"{other_pokemon.name.capitalize()} has higher {stat}: {other_value} > {self_value}")
                else:
                    print(f"{self.name.capitalize()} and {other_pokemon.name.capitalize()} have the same {stat}: {self_value}")
            else:
                print(f"Stat '{stat}' not found for both Pokémon.")