import random

# Computer randomly chooses -1, 0, or 1
computer = random.choice([-1, 1, 0])

# Taking user input
YouChoose = input("Enter Your Choice (s for Snake, w for Water, g for Gun): ").lower()

# Dictionaries for mapping user input to values and vice versa
YouDict = {"s": 1, "w": -1, "g": 0}
ReverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Check if the user input is valid
if YouChoose not in YouDict:
    print("Invalid choice! Please choose 's', 'w', or 'g'.")
else:
    # Map the user input to the corresponding value
    You = YouDict[YouChoose]
    
    # Print user and computer choices
    print(f"You Choose: {ReverseDict[You]}")
    print(f"Computer Choose: {ReverseDict[computer]}")
    
    # Game logic
    if computer == You:
        print("It's a Draw!")
    else:
        if (computer == -1 and You == 1) or (computer == 1 and You == 0) or (computer == 0 and You == -1):
            print("You Win!")
        else:
            print("You Lose!")
