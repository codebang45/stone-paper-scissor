

while True:


    import random
    item_list = ["stone","paper","scissor"]

    user_choice = input("enter your choice = stone,paper,scissor: ")
    compu_choice = random.choice(item_list)

    print(f"user choice = {user_choice}, computer choice = {compu_choice}")

    if user_choice == compu_choice:
        print("both chooses same: = match tie")

    elif user_choice == "stone":
        if compu_choice == "paper":
            print("paper covers stone = computer win")

        else:
            print("stone smashes scissor = you win") 

    elif user_choice == "paper":
        if compu_choice == "scissor":
            print("scissor cut paper = computer win")

        else:
            print("paper covers stone = you win")

    elif user_choice == "scissor":
        if compu_choice == "paper":
            print("scissor cuts paper = you win")

        else:
            print("stone smashes scissor = computer win")





