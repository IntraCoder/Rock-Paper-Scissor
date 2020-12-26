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
    global score
    rounds = int(input(">>> Number of Rounds:"))
    print("*******************************************")

    score = {name: 0, "Computer": 0, "Draw": 0}
    roun = 1

    while roun != rounds + 1:
        print("--------------------------------------")
        print(f"Round-{roun}")
        user = input(">>> Enter (rock/paper/scissor):").lower()
        choe = {"rock": "scissor", "scissor": "paper", "paper": "scissor"}
        comp = random.choice(tuple(choe))
        print("[+] Computer:", comp)
        if user == "quit":
            break

        elif user not in choe:
            print("[-] Enter valid input!")
            continue

        elif user == choe[comp]:
            print("[+] You lost!")
            score["Computer"] += 1

        elif user == comp:
            print("[+] Draw!")
            score["Draw"] += 1

        else:
            print("[+] You Won!")
            score[name] += 1

        print(f"{name.title()}: {score[name]}  Computer: {score['Computer']} Draw: {score['Draw']}")
        roun += 1


game()

global score
print("*******************************************")
if score[name] == score["Computer"]:
    print("Draw !")
elif score[name] > score["Computer"]:
    print(name, "Won!")
else:
    print("Computer Won!")
