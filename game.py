from goblin import Goblin


ARENA_NAME = "Gibbles Grand Guesthouse"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gibble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    newgoblin = Goblin("Sibble")

    print(f"{newgoblin.name} enters the arena with {newgoblin.health} health.")

    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
