from goblin import Goblin
from hero import Hero


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
    bob = Hero("lora")
    print(f"{bob.name} enters the arena with {bob.health} health.")
    LoraAttack = bob.attack()
    goblin.take_damage(LoraAttack)
    if goblin.is_alive:
        goboattk= goblin.attack()
        bob.take_damage(goboattk)
    else:
        print ("You defeted the Goblin!!")

if __name__ == "__main__":
    main()
