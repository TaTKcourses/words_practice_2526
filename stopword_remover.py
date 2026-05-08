import os


def load_words(filename):
    import os
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)

    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")  # split by comma
            words.extend([p.strip() for p in parts if p.strip()])

    return words


def remove_stopwords(
    freq_file="word_lists/top_freq_5000_hu.txt",
    stopwords_file="word_lists/stopwords_hu.txt"
):
    """
    Removes stopwords from the list of frequent words.

    Args:
        freq_file (str): path to frequent words file
        stopwords_file (str): path to stopwords file

    Returns:
        list: filtered list without stopwords
    """
    freq_words = load_words(freq_file)
    stopwords = set(load_words(stopwords_file))

    filtered = [word for word in freq_words if word not in stopwords]

    return filtered


if __name__ == "__main__":
    result = remove_stopwords()
    print(result[:20])  # first 20 words
    print(f"Remaining words: {len(result)}")
    