from set_of_word import set_of_word


class Wordle:
    max_attempt = 6
    word_length = 5
    voided_letter = '*'

    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []

    def attempt_word(self, word: str):
        self.word: str = word.upper()
        self.attempts.append(word)

    def guess_word(self, word: str):
        self.word: str = word.upper()

        result = [set_of_word(x) for x in word]

        secret_word = list(self.secret)

        for i in range(self.word_length):
            letter = result[i]

            if letter.char == secret_word[i]:
                letter.is_in_position = True  # check the letter is correct position
                secret_word[i] = self.voided_letter

            # Loop again and check for YELLOW letters.
            for i in range(self.word_length):
                letter = result[i]

                if letter.is_in_position:
                    continue

                # Skip this letter if it is already in the right place.
                for j in range(self.word_length):
                    if letter.char == secret_word[j]:
                        secret_word[j] = self.voided_letter
                        letter.is_in_word = True
                        break
            return result

    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @property
    def remaining_attempts(self) -> int:
        return self.max_attempt - len(self.attempts)

    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved
