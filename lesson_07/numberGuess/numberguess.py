import random

answer = random.randint(1, 101)
print("guess the number")
guess = int(input())

total_guesses = 0

while guess != answer:
    total_guesses += 1
    if guess < answer:
        print("too low")
    elif guess > answer:
        print("too high")
    guess = int(input("try again: "))

if total_guesses == 1:
    print("You got it in 1 try")
else:
    print(f"{answer} was the answer")
    print(f"It took you {total_guesses} tries")
