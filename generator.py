import random   # véletlen választásokhoz (random szó kiválasztása)
from pathlib import Path  # fájlútvonalak kezeléséhez (platformfüggetlenül)


def load_words(file_path):
    # megnyitjuk a fájlt olvasásra (utf-8 kódolással)
    with open(file_path, "r", encoding="utf-8") as f:
        # minden sort beolvasunk, levágjuk a whitespace-t (\n stb.)
        # és csak a nem üres sorokat tartjuk meg
        return [line.strip() for line in f if line.strip()]


def generate_sentences(n_sentences=3, words_per_sentence=6, n_proper=1):
    # ellenőrzés: nem lehet több tulajdonnév, mint az összes szó
    if n_proper > words_per_sentence:
        raise ValueError("n_proper cannot be bigger than words_per_sentence")

    # a jelenlegi fájl (generator.py) mappájának elérési útja
    base_path = Path(__file__).parent
    word_lists_path = base_path / "word_lists"

    # különböző szólisták betöltése fájlokból
    proper_nouns = load_words(word_lists_path / "proper_nouns_hu.txt")
    stopwords = load_words(word_lists_path / "stopwords_hu.txt")
    freq_words = load_words(word_lists_path / "top_freq_5000_hu.txt")

    # egy közös lista a nem tulajdonneves szavaknak
    pool = stopwords + freq_words
    sentences = []

    # ennyi mondatot generálunk
    for _ in range(n_sentences):
        sentence_words = []

        # kiválasztunk n_proper darab tulajdonnevet
        for _ in range(n_proper):
            sentence_words.append(random.choice(proper_nouns))

        # kiszámoljuk hány szó hiányzik még a mondathoz
        remaining = words_per_sentence - n_proper
        # feltöltjük a mondatot random szavakkal a pool-ból
        for _ in range(remaining):
            sentence_words.append(random.choice(pool))

        # összekeverjük a szavak sorrendjét
        random.shuffle(sentence_words)

        # az első szót nagybetűssé tesszük
        sentence_words[0] = sentence_words[0].capitalize()

        # a szavakat összefűzzük egy mondattá és pontot teszünk a végére
        sentence = " ".join(sentence_words) + "."

        # hozzáadjuk a mondatot a listához
        sentences.append(sentence)

    return sentences