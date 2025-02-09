import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    
    while True:
        # Choose difficulty level
        print("\nChoose a difficulty level:")
        print("1. Easy (1-10, Unlimited attempts)")
        print("2. Medium (1-50, 7 attempts)")
        print("3. Hard (1-100, 5 attempts)")
        print("4. Quit")
        
        choice = input("Enter your choice (1, 2, 3, or 4): ")
        
        if choice == '4':
            print("Thanks for playing! Goodbye!")
            break
        
        if choice == '1':
            number = random.randint(1, 10)
            attempts = float('inf')  # Unlimited attempts
        elif choice == '2':
            number = random.randint(1, 50)
            attempts = 7
        elif choice == '3':
            number = random.randint(1, 100)
            attempts = 5
        else:
            print("Invalid choice! Please select a valid option.")
            continue

        print(f"\nI have selected a number. You have {attempts} attempts to guess it correctly.")
        attempt_count = 0
        
        while attempt_count < attempts:
            try:
                guess = int(input("Enter your guess: "))
                attempt_count += 1

                if guess < number:
                    print("Too low! Try again.")
                elif guess > number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed the number in {attempt_count} attempts.")
                    break
            except ValueError:
                print("Please enter a valid number.")
            
            if attempt_count >= attempts:
                print(f"Sorry, you've run out of attempts. The number was {number}.")
    
# Run the game
guess_the_number()
