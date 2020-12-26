import random

print("------------------ Rock Paper Scissor Game ------------------")


def ask_name():
    name = input(">>> Enter your name:")
    if name == "":
        ask_name()
    else:
        return name


name = ask_name()
print(f"[+] Nice to meet you {name}!")


def game():
    try:
        global rounds
        rounds = int(input(">>> Number of Rounds:"))
        print("*******************************************")
    except ValueError:
        game()

    user_score, comp_score, roun, draw = 0, 0, 0, 0
    while roun != rounds:
        print("--------------------------------------")

        user = input(">>> Enter Here:").lower()

        choice = {"rock": "scissor", "paper": "rock", "scissor": "paper"}
        comp = random.choice(tuple(choice))

        print("[+] Computer:", comp)
        if user == "quit":
            break
        elif user not in choice:
            print("[-] Enter valid input!")
            continue
        elif user == choice[comp]:
            print("[+] You lost!")
            comp_score += 1
        elif user == comp:
            print("[+] Draw!")
            draw += 1
        else:
            print("[+] You Won!")
            user_score += 1
        print(f"{name.title()}: {user_score}  Computer: {comp_score} Draw: {draw}")
        roun += 1


game()
print("*******************************************")
print(f"{max(user_score, comp_score)}")
ask = input("Do you want to play again?")
if ask in ("y", "yes"):
    game()
else:
    exit()
