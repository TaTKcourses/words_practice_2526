from collections import Counter
import json
import re


PROPER_NOUNS_FILE = "word_lists/proper_nouns_hu.txt"
FREQ_WORDS_FILE = "word_lists/top_freq_5000_hu.txt"
STOPWORDS_FILE = "word_lists/stopwords_hu.txt"

OUTPUT_JSON = "result.json"
OUTPUT_TXT = "result.txt"


def normalize_text(text: str) -> str:
    """
    Kisbetűsít, és csak a betűket tartja meg.
    A magyar ékezetes betűket is megtartja.
    """
    text = text.lower()
    return "".join(ch for ch in text if ch.isalpha())


def read_token_file(filename: str) -> list[str]:
    """
    Olyan fájlt olvas be, ahol a szavak lehetnek:
    - soronként egyesével
    - vagy vesszővel elválasztva
    - vagy ezek keverékeként
    """
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    raw_tokens = re.split(r"[,\n;]+", content)

    tokens = []
    for token in raw_tokens:
        cleaned = token.strip()
        if cleaned:
            tokens.append(cleaned)

    return tokens


def read_proper_nouns(filename: str) -> list[str]:
    """
    Tulajdonnevek beolvasása.
    Feltételezzük, hogy ezek külön elemekként szerepelnek a fájlban.
    """
    names = read_token_file(filename)

    unique_names = []
    seen = set()
    for name in names:
        if name not in seen:
            seen.add(name)
            unique_names.append(name)

    return unique_names


def read_frequent_words(filename: str, stopwords_filename: str | None = None) -> list[str]:
    """
    Gyakori szavak beolvasása, opcionálisan stopword-szűréssel.
    """
    words = read_token_file(filename)

    stopwords = set()
    if stopwords_filename is not None:
        stopwords_raw = read_token_file(stopwords_filename)
        stopwords = {normalize_text(w) for w in stopwords_raw if normalize_text(w)}

    result = []
    seen = set()

    for word in words:
        norm = normalize_text(word)
        if not norm:
            continue
        if norm in stopwords:
            continue
        if norm not in seen:
            seen.add(norm)
            result.append(norm)

    return result


def can_build_name_from_word(name: str, word: str) -> bool:
    """
    Eldönti, hogy a 'word' betűiből kirakható-e a 'name'.
    A betűk darabszámát is figyeli.
    """
    name_norm = normalize_text(name)
    word_norm = normalize_text(word)

    name_counter = Counter(name_norm)
    word_counter = Counter(word_norm)

    for letter, needed_count in name_counter.items():
        if word_counter[letter] < needed_count:
            return False

    return True


def find_matches(proper_nouns: list[str], frequent_words: list[str]) -> dict[str, list[str]]:
    """
    Minden tulajdonnévhez megkeresi azokat a gyakori szavakat,
    amelyekből a tulajdonnév kirakható.
    """
    result = {}

    for name in proper_nouns:
        matches = []
        for word in frequent_words:
            if can_build_name_from_word(name, word):
                matches.append(word)

        if matches:
            result[name] = matches

    return result


def save_to_json(data: dict[str, list[str]], filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def save_to_txt(data: dict[str, list[str]], filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        for name, words in data.items():
            f.write(f"{name}: {', '.join(words)}\n")


def main():
    proper_nouns = read_proper_nouns(PROPER_NOUNS_FILE)
    frequent_words = read_frequent_words(FREQ_WORDS_FILE, STOPWORDS_FILE)

    result = find_matches(proper_nouns, frequent_words)

    save_to_json(result, OUTPUT_JSON)
    save_to_txt(result, OUTPUT_TXT)

    print(f"Tulajdonnevek száma: {len(proper_nouns)}")
    print(f"Szűrt gyakori szavak száma: {len(frequent_words)}")
    print(f"Találatot adó tulajdonnevek száma: {len(result)}")
    print(f"Eredmény elmentve: {OUTPUT_JSON}, {OUTPUT_TXT}")


if __name__ == "__main__":
    main()
