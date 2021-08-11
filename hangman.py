# Write your code here
import random

print("H A N G M A N")

base = ["kotlin", "python", "java", "javascript"]
comp_choice = random.choice(base)

show = list("-" * len(comp_choice))
lives = 8
answers = []
alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "v",
            "x", "y", "z", "q"}


def legit_check(guess, tries):
    if len(guess) != 1:
        print("You should input a single letter")
        return False
    elif guess not in alphabet:
        print("Please enter a lowercase English letter")
        return False
    elif guess in show or guess in tries:
        print("You've already guessed this letter")
        return False
    else:
        return True


while True:
    choice = input('Type "play" to play the game, "exit" to quit:')
    if choice != "play":
        break
    while lives > 0:
        print()
        print("".join(show))
        my_hit = input("Input a letter:")
        if legit_check(my_hit, answers):
            if my_hit not in comp_choice:
                print("That letter doesn't appear in the word")
                answers.append(my_hit)
                lives -= 1
            else:
                k = 0
                for char in comp_choice:
                    if char == my_hit:
                        show[k] = char
                        answers.append(my_hit)
                    k += 1

        if "".join(show) == comp_choice:
            break

    if "".join(show) != comp_choice:
        print("You lost!")
    else:
        print(f"You guessed the {comp_choice}!")
        print("You survived!")
