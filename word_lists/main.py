from code_function import occ_word_file_and_reversable


def main():
    rank = 10  # set a value if you want; be careful about length

    counter_occ, is_reversable = occ_word_file_and_reversable(
        "top_freq_5000_hu.txt",
        rank
    )
    print('-'*50)

    # print('top 10 of all words into to_freq_5000_hu.txt:')
    # print(counter_occ[:10]) # words with the most
    # occurrences among the 5000 words
    # print('-'*50)
    print(f'top {rank} of all words with a reverse into to_freq_5000_hu.txt:')
    print(is_reversable)  # prints the most frequent words among
    # the 5000 that also have their reverse in the list
    print('-'*50)


if __name__ == "__main__":
    main()
