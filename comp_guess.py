import random
def computer_guess(x):
    low=1
    high=x
    feedback= ''
    while feedback != 'c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'Is {guess} too high(h/H), too low(l/L) or correct(c/C)??:').lower
        if feedback=='h':
            high=guess - 1
        elif feedback=='l':
            low=guess + 1
    print(f"yay, the computer has guessed {guess} which is correct.")

computer_guess(10)    