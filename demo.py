import random
import time



def main():
    my_num = random.randint(1,4000)

    print("Welcome to the CS Club Number guessing game, I'm thinking of a number between 1 and 4 thousand. What is it?: ")
    num = input("Input your guess here: ")
    if(int(num) == my_num):
        print("Huh... wha ...")
        time.sleep(1)
        print("HOW DID YOU DO THAT?:?!@?!?")
        time.sleep(2)
        print("Reporting Honor Board Violation...")
        time.sleep(0.5)
        print("Report sent")
    else:
        print("NOPE, Later!")


if __name__ == "__main__":
    main()