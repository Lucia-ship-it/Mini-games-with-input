#GUESS MY NUMBER
print("\nHi, I'm Bill\n")

print("Let's play a game: guess my number. Can you figure it out?\n")


import random


while True:
    print("I'm thinking of a number between 1 and 10.\n")
    my_secret_number = random.randint(1, 10)
    your_guess = int(input("What number am I thinking of? "))

    while my_secret_number != your_guess:
        print(f"That's not {your_guess}. Try again!\n")
        your_guess = int(input("What number am I thinking of? "))

    print(f"\nYes, you got it! It really was number {my_secret_number}!\n\n")

    print("Do you want to play again? Type yes or no:")

    while True:
        play_again = input().strip().lower()

        if play_again == "yes":
            print("\n\n\n")
            print("Great, let's do it!")
            print("\n\n\n")
            break
        elif play_again == "no":
            print("\n\n\n")
            print("Thanks for playing! Goodbye!\n")
            exit
        else:
            print("Just type 'yes' or 'no'.")
          
        
# OK    slucka na yes/no
#       pocitadlo neplatnych pokusov s vylepsenymi hlaskami
#       "Soo?: ")  print(f"Hey dude, Come on, it's just 'yes' or 'no'!\n{again}")
# OK    vyber nahodneho cisla pocitacom
#       postupne zobrazovanie textu, s oneskorenim pri hlaske o uhadnuti cisla
#       skóre
#       počet pokusov
#       výber úrovne obtiažnosti
#       Udrží konzolu otvorenú

