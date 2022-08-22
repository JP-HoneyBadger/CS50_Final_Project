# Teach you Spanish numbers, zero to ten.
# Input number and output the Spanish word with sound pronunciation.


import pyttsx3
import re
import sys

# Using a class for global variable


class Number:
    def __init__(self, num):
        self.num = num

    @classmethod
    def get(cls):
        num = input(
            "Learn Spanish numbers by typing in a number 0-10: ").strip()
        return num


class Answer:
    def __init__(self, answer):
        self.answer = answer

    @classmethod
    def get(cls):
        answer = input("Do you want to continue Y/N: ").upper().strip()
        return answer


def main():
    # Getter (Getting the variable num)
    num = Number.get()
    # Calling check_num
    check_num(num)
    # Calling coverted_num
    converted_num(num)
    # Calling play_again
    answer = Answer.get()
    play_again(answer)


# Check for number 0-10


def check_num(num):
    n = re.search(r"^(\d[0]*)$", num)
    if n is None:
        print("Please enter a number 0-10")
        main()
    else:
        return (num)


# Convert number to Spanish word


def converted_num(num):
    print(num)
    sn = num_spanish[num]
    print(sn)
    speak_num_spanish(sn)

# Asking if player wants to play again


def play_again(answer):
    while True:
        if answer == 'Y':
            main()
        elif answer == 'N':
            sys.exit("Thanks for playing!")
        else:
            while answer not in 'YN':
                print("Invalid input, please try again.")
                answer = input("Do you want to continue Y/N: ").upper()


# Speak spanish number


def speak_num_spanish(sn):
    engine = pyttsx3.init()
    engine.say(sn)
    engine.runAndWait()


# 0-10 in Spanish
num_spanish = {
    "0": "cero",
    "1": "uno",
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "cinco",
    "6": "seis",
    "7": "siete",
    "8": "ocho",
    "9": "nueve",
    "10": "diez"
}


if __name__ == "__main__":
    main()
