def main():
    input_file_path = r"C:\Users\admin\PycharmProjects\CodeOpss\demo\data/words.txt"
    output_file_path = r"C:\Users\admin\PycharmProjects\CodeOpss\demo\data/words.txt"
    letter_words = []

    with open(input_file_path, 'r') as f:
        for line in f.readlines():
            word = line.strip()
            if len(word) == 5:
                letter_words.append(word)

    with open(output_file_path, 'w') as f:
        for word in letter_words:
            f.write(word + '\n')

    print(f"Found {len(letter_words)} five-letter words.")


if __name__ == "__main__":
    main()
