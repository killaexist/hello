from brain_games.games.template import is_greeting, gcd_desc, wrong_answer
import prompt
from random import randint



def is_gcd():
    name = is_greeting()
    gcd_desc()
    count_correct = 0
    while count_correct < 3:
        r_num = randint(0, 99)
        r_num2 = randint(0, 99)
        print(f"Question: {r_num} {r_num2}")
        ans = prompt.string("Your answer: ")
        
        












from colorama import Fore


def main():
    print(f'{Fore.RED}Hello!') 


if __name__ == '__main__':
    main()
