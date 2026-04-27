with open("word_lists/proper_nouns_hu.txt", "r", encoding = "utf-8") as f:
    nouns = [line.strip() for line in f]

with open("word_lists/top_freq_5000_hu.txt", "r", encoding = "utf-8") as f:
    topfreq = [line.strip() for line in f]

# kód logikája: minden tulajdonnévre minden gyakori szót ellenőrzünk beágyazott ciklusokkal
# lehetne unordered seteket is alkalmazni, de jóval lassabb mert folyton feltöltünk és kiürítünk seteket

# kis- és nagybetűket nem különböztetünk meg (.lower() method mindkét szóra)
# feltesszük, hogy a gyakori szóban egy ugyanolyan betű többször is használható
# (legalábbis azért, mert ez a módszer csak akkor műkszik)

dictionary = dict()    
for noun in nouns:
    n = noun.lower()
    for freq_word in topfreq:
        fw = freq_word.lower()

        # itt: minden betűre az adott tulajdonnévben megnézünk minden betűt az adott
        # gyakori szóban (fordítva nem működne), és a "found" boolean változót
        # állítgatjuk betűnként
        # a "valid" változó pedig az egyes gyakori szavakat kontrollálja
        valid = True
        for n_letter in n:
            found = False
            for fw_letter in fw:
                if n_letter == fw_letter:
                    found = True
                    break
                else:
                    continue
            if not found: # elég egy betű a tulajdonnévből, ami nincs benne, az azonnal megszegi a feltételünket
                valid = False
                break
            else:
                continue
        if valid:
            if noun not in dictionary:
                dictionary[noun] = list()

            dictionary[noun].append((freq_word))

print(dictionary.keys()) # összes bekerült tulajdonnév

print(dictionary["Réka"]) # példa