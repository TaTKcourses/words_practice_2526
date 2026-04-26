def load_words():
    words = []

    with open("top_freq_5000_hu.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",") #több szót tartalamzó sorokat vessző mentén bontja

            for word in parts: #végigmegy a szavakon, fölösleges szóközöket törli, üres elemeket szűri
                word = word.strip()
                if word:
                    words.append(word)

    return words


def sort_by_suffix(words): #szóvég szerinti rendezés
    return sorted(words, key=lambda w: w.lower()[::-1]) #kisbetűvé teszi a szavakat pl USB helyett usb, majd megfordítja a szavakat és aszerint rendez


def main():
    words = load_words() #beolvassa a fájlt - azaz ha változik, akkor is működnie kéne a függvénynek
    return sort_by_suffix(words)


list = main()
print(list)