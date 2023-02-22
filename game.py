import random

player_name = input("Type your name please -> ")

def guess_number():
    print("Let's play a game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Ok, {player_name.capitalize()} try to guess the number in as few attempts as possible.\n")
    
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        
        if guess == number:
            print(f"Congratulations {player_name.capitalize()}! You found the number in {attempts} attempts.")
            break
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")
            
if __name__ == "__main__":
    guess_number()