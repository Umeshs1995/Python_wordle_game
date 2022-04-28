from typing import List
from set_of_word import set_of_word
from wordle_game import Wordle
from colorama import Fore
import random


def main():
    word_set = word_file_path (r"C:\Users\admin\PycharmProjects\CodeOpss\demo\data/words.txt")
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)

    while wordle.can_attempt:
        x = input("Type Your Guess:").upper()

        if len(x) != wordle.word_length:
            print(
                Fore.RED
                + f"Word must be {wordle.word_length} characters long!"
                + Fore.RESET
            )
            continue

        if not x in word_set:
            print(
                Fore.RED
                + f"{x} is not a valid word!"
                + Fore.RESET
            )
            continue

        wordle.attempts.append(x)
        display_results(wordle)

    if wordle.is_solved:
        print("You've solved the puzzle.")
    else:
        print("You failed to solve the puzzle!")
        print(f"The secret word was: {wordle.secret}")


def display_results(wordle: Wordle):
    print("\nYour results so far...")
    print(f"You have {wordle.remaining_attempts} attempts remaining.\n")

    lines = []

    for word in wordle.attempts:
        result = wordle.guess_word(word)
        colored_result_str = convert_result(result)
        lines.append(colored_result_str)

    for _ in range(wordle.remaining_attempts):
        lines.append(" ".join(["_"] * wordle.word_length))

    draw_border(lines)


def word_file_path(path:str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set


def convert_result(result: List[set_of_word]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.char + Fore.RESET
        result_with_color.append(colored_letter)
    return " ".join(result_with_color)


def draw_border(lines: List[str], size: int = 9, pad: int = 1):
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    print(top_border)

    for line in lines:
        print("│" + space + line + space + "│")

    print(bottom_border)


if __name__ == "__main__":
    main()
