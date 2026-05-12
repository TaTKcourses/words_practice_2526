def find_words_containing(search_string, wordlist_file="word_lists/top_freq_5000_hu.txt"):
    """
    Visszaadja azokat a szavakat, amelyek tartalmazzák a search_string-et.
    Kis- és nagybetűk között nem tesz különbséget.
    """

    matches = []

    with open(wordlist_file, "r", encoding="utf-8") as file:
        for line in file:
            words = line.split()

            for word in words:
                word = word.strip(",.;:")
                if search_string.lower() in word.lower():
                    matches.append(word)

    return matches


# Tesztelés
if __name__ == "__main__":
    result = find_words_containing("pont")
    print(result)