import random

cheatcode = "SGVsbG8sIHdvcmxkIQ=="

easyans = random.randint(1, 10)
mediumans = random.randint(1, 25)
hardans = random.randint(1, 50)

def easy():
    while True:
        try:



            print("Enter your guess")

            guess = int(input("> "))

            if guess > easyans:
                print("Number too high!")
                continue
            elif guess < easyans:
                print("Number too low!")
                continue
            else:
                print("Congratulations! Do you want to play again? (y/n)")

                yn = input("> ")

                if yn == "y" or yn == "Y":
                    main()
                else:
                    exit()

        except ValueError:
            print("Invalid number")
            break
        except KeyboardInterrupt:
            continue

def medium():
    while True:
        try:



            print("Enter your guess")

            guess = int(input("> "))

            if guess > mediumans:
                print("Number too high!")
                continue
            elif guess < mediumans:
                print("Number too low!")
                continue
            else:
                print("Congratulations! Do you want to play again? (y/n)")

                yn = input("> ")

                if yn == "y" or yn == "Y":
                    main()
                else:
                    exit()

        except ValueError:
            print("Invalid number")
            break
        except KeyboardInterrupt:
            continue

def hard():
    while True:
        try:



            print("Enter your guess")

            guess = int(input("> "))

            if guess > hardans:
                print("Number too high!")
                continue
            elif guess < hardans:
                print("Number too low!")
                continue
            else:
                print("Congratulations! Do you want to play again? (y/n)")

                yn = input("> ")

                if yn == "y" or yn == "Y":
                    main()
                else:
                    exit()

        except ValueError:
            print("Not a number!")
            break
        except KeyboardInterrupt:
            continue

def main():
    print("Welcome! Please Enter Mode")
    
    print("""
[1] - Easy
[2] - Medium
[3] - Hard
""")
    mode = input("> ")

    if mode == "1":
        easy()
    elif mode == "2":
        medium()
    elif mode == "3":
        hard()

main()