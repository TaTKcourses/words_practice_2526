def count_txt_file(file):
    """
        Reads a text file and counts occurrences of valid words.

        A word is considered valid if:
        - it has more than 1 character
        - it contains only alphabetic characters

        The file can contain either:
        - one word per line
        - multiple words separated by commas
    g
        Invalid words are counted separately under '#error_count#'.

        Args:
            file (str): Path to the input text file.

        Returns:
            tuple:
                dict: A dictionary with word counts and an error counter.
                      Example: {"word": 3, "#error_count#": 2}
                set: A set of invalid words encountered in the file.
    """
    error = set()
    res = {"#error_count#": 0}

    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # case 1: single word line
            if "," not in line:
                words = [line]
            else:
                words = line.split(",")

            for word in words:
                word = word.strip()

                if len(word) <= 1:
                    continue

                if not word.isalpha():
                    res["#error_count#"] += 1
                    error.add(word)
                    print(f"{word} contain invalid characters")
                    continue

                res[word] = res.get(word, 0) + 1

    return res, error


def keep_word_tuple_occ(list_word_occ: list):
    """
    Extracts only words from a list of (word, count) tuples.

    Args:
        list_word_occ (list): List of tuples (word, occurrence).

    Returns:
        list: List of words only.
    """
    return [word[0] for word in list_word_occ]


def list_wordreversable(list_word: list, dict_file: dict):
    """
    Filters and returns words whose reversed version
    is also present in a reference dictionary.

    A word is considered reversible if its reversed
    form exists as a key in the given dictionary.

    Args:
        list_word (list): List of words to check.
        dict_file (dict): Dictionary containing words
                          as keys (e.g., word frequency map).

    Returns:
        list: Words whose reversed counterpart is found in dict_file.
    """
    return [word for word in list_word if word[::-1] in dict_file]


def occ_word_file_and_reversable(file, rank=None):
    """
    Combines file word reading and reversible-word filtering.

    Steps:
    1. Read valid words from a pre-selected word list file.
    2. Keep the original word list order.
    3. Optionally limit the number of words considered.
    4. Filter words whose reversed form is also present in the list.

    Args:
        file (str): Path to the input file.
        rank (int | None): Optional number of words to consider from the list.

    Returns:
        tuple:
            list: Words read from the file.
            list: Words whose reversed counterpart is also found in the file.
    """
    counter, error = count_txt_file(file)

    words = [word for word in counter if word != "#error_count#"]

    if rank is not None:
        if rank <= 0 or rank > len(words):
            raise ValueError(f"rank must be > 0 and <= {len(words)}")
        words = words[:rank]

    reversables = list_wordreversable(words, counter)

    return words, reversables
