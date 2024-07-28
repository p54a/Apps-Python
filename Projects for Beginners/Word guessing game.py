import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

trys = 12
guesses = ""

while trys > 0:
    trys -= 1
    
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end="")
    
    
    guess = input("\nEnter a char: ")
    guesses += guess

print(f"\nThe word is {word}")