from collections import Counter

def letter_frequency(text):
    text = text.lower()
    letters = [c for c in text if c.isalpha()]

    total = len(letters)

    if total == 0:
        return {}

    counts = Counter(letters)
    return {letter: count / total for letter, count in counts.items()}

def compare_frequencies(input_file, reference_file="word_lists/top_freq_5000_hu.txt"):

    with open(input_file, "r", encoding="utf-8") as f:
        input_text = f.read()

    with open(reference_file, "r", encoding="utf-8") as f:
        ref_text = f.read()

    input_freq = letter_frequency(input_text)
    ref_freq = letter_frequency(ref_text)

    result = {}

    for letter, ref_val in ref_freq.items():
        inp_val = input_freq.get(letter, 0)


        lower = ref_val * 0.9
        upper = ref_val * 1.1

        if inp_val < lower or inp_val > upper:
            result[letter] = {
                "reference": ref_val,
                "input": inp_val
            }

    return result

if __name__ == "__main__":
    files = [
        "word_lists/stopwords_hu.txt",
        "word_lists/proper_nouns_hu.txt"
    ]

    for f in files:
        print(f"\n--- {f} ---")
        result = compare_frequencies(f)
        print(result)