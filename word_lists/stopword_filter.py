
stopszavak = set(open("stopwords_hu.txt", encoding="utf-8").read().splitlines())

for szo in open("top_freq_5000_hu.txt", encoding="utf-8").read().splitlines():
    if szo in stopszavak:
        print(szo)






