from generator import generate_sentences

result = generate_sentences(n_sentences=4, words_per_sentence=7, n_proper=2)

for sentence in result:
    print(sentence)
