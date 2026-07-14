health = 100
while True:
    print(f"\n Your current health is :{health}")
    action = input("Do you want to 'fight', 'heal', or 'exit'? ").lower()
    if action == "exit":
        print("Saving game... Thanks for playing! 🎮")
        break
    elif action == "fight":
        print("You fought a monster! You lost 40 health.")
        health -= 40
    elif action == "heal":
        print("You drank a potion! You gained 20 health.")
        health += 20
    else:
        print("Invalid action! The monsters are watching...")
    if health <= 0:
        print("Game Over! You ran out of health. 💀")
        break
