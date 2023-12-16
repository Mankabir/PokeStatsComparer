import unittest
from pokemon import Pokemon 

class TestPokemon(unittest.TestCase):

    def test_init_and_stat_fetching(self):
        # Test with a real Pokemon
        pikachu = Pokemon('pikachu')
        self.assertEqual(pikachu.name, 'pikachu')
        self.assertTrue(isinstance(pikachu.stats, dict))
        self.assertTrue('speed' in pikachu.stats)

    def test_init_with_invalid_pokemon(self):
        # Test with an invalid Pokemon name
        fake_pokemon = Pokemon('notapokemon')
        self.assertEqual(fake_pokemon.name, 'notapokemon')
        self.assertEqual(fake_pokemon.stats, {})

    def test_compare_stats(self):
        # Test comparing stats of two real Pokemon
        pikachu = Pokemon('pikachu')
        bulbasaur = Pokemon('bulbasaur')
        self.assertTrue(isinstance(pikachu.compare_stats(bulbasaur), str) or pikachu.compare_stats(bulbasaur) is None)

if __name__ == '__main__':
    unittest.main()
