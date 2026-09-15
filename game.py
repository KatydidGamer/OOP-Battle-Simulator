from goblin import Goblin
from hero import Hero


ARENA_NAME = "Gibbles Grand Guesthouse"
def battle(hero: Hero,enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_dam= hero.attack()
        enemy.take_damage(hero_dam)
        if enemy.is_alive():
            enemy_dm= enemy.attack()
            hero.take_damage(enemy_dm)
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gibble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    newgoblin = Goblin("Sibble")

    print(f"{newgoblin.name} enters the arena with {newgoblin.health} health.")

    bob = Hero("lora")
    print(f"{bob.name} enters the arena with {bob.health} health.")
    battle(bob,goblin)
if __name__ == "__main__":
    main()
