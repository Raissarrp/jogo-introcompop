# Constantes para cálculos de batalha
BASE_DEFENSE = 50
DEFENSE_MULTIPLIER = 2
# Define defense multiplier based on character level
def get_defense_multiplier(level):
    return 2 + level * 0.1