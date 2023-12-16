# PokeStatsComparer

PokeStatsComparer is a Python project that leverages the PokeAPI to fetch and compare Pokémon statistics. It allows users to retrieve detailed stats like speed, attack, and defense for different Pokémon and provides functionality for stat comparison.

## Code Explanation

### Part 1: Interacting with PokeAPI
- **Libraries**: The script primarily uses the `requests` library for API interaction.
- **Pokemon Class**: Represents a Pokémon and contains methods for API interaction and stats comparison.
- **`get_pokemon_stats()`**: Fetches stats for a specific Pokémon from the PokeAPI.
- **Stats Dictionary**: Stores the fetched stats in a dictionary for easy access and comparison.

### Part 2: Comparing Pokémon Stats
- **`compare_stats(other_pokemon)`**: Compares the stats of two Pokémon instances.
- **Stat Comparison Logic**: The method iterates through each stat, comparing the corresponding values from two Pokémon.
- **Printed Output**: Displays a comparison result for each stat in a user-friendly format.

### Part 3: Unit Tests
- **Testing Framework**: Uses Python’s `unittest` framework for testing.
- **Test Cases**: Includes tests for API data fetching, error handling, and stats comparison functionality.

### Part 4: Main Script
- **`main()`**: The main method where instances of the `Pokemon` class are created and compared.
- **Script Execution**: Running `main.py` initiates the fetching and comparing of Pokémon stats.

## Installation

To use this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Mankabir/PokeStatsComparer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd PokeStatsComparer
   ```
3. Install the required dependencies (ensure you have Python installed):
   ```bash
   pip install requests
   ```

## Usage

To run the project:

1. Navigate to the project directory.
2. Run the main script:
   ```bash
   python main.py
   ```

## Running the Tests

The project includes unit tests to validate the functionality. To run the tests, use the following command:

```bash
python -m unittest
```

## Acknowledgments

- PokeAPI for providing the Pokémon data.