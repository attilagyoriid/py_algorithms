class StringManipulator:

    @staticmethod
    def reverse_string(text: str) -> str:
        lst = list(text)
        result = ""
        for i in range(len(lst) - 1, -1, -1):
            result += lst[i]

        return result

    @staticmethod
    def reverse_word_order(sentence: str) -> str:
        words = []
        length = len(sentence)

        i = 0

        while i < length:

            if sentence[i] != " ":

                word_start = i

                while i < length and sentence[i] != " ":
                    i += 1

                words.append(sentence[word_start:i])

            i += 1

        return " ".join(reversed(words))
