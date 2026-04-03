import random
while True:
    secret = random.randint(1,100)
    print("GUESSING GAME \n guess a number between 1 to 100")
    count = 0
    while True:
        guess = int(input("enter you num: "))
        count += 1
        if guess == secret:
            print(f"Congratulation!! you are correct.\n Gussed in {count} attempts")
            break
        elif guess < secret:
            print("too Low!! Guess Again")
        elif guess > secret:
            print("too High!! Guess Again")
    
    again = input("\n Play Again? (YES/NO): ")
    if again.lower()!= "yes":
        print("thanks and come again!")
        break



