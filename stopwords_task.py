# stopwords betöltése (egy szó soronként)
def load_stopwords(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


# top freq lista betöltése (vesszős sorok kezelése miatt tisztítjuk)
def load_top_freq(filepath):
    words = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            for word in parts:
                cleaned = word.strip()
                if cleaned:
                    words.append(cleaned)
    return words


# stopwords közül azok, amik nincsenek a top freq listában
def find_missing_stopwords(stopwords, top_words):
    return list(set(stopwords) - set(top_words))


# futtatás
if __name__ == "__main__":
    stopwords = load_stopwords("word_lists/stopwords_hu.txt")
    top_words = load_top_freq("word_lists/top_freq_5000_hu.txt")

    missing = find_missing_stopwords(stopwords, top_words)

    print(missing)
