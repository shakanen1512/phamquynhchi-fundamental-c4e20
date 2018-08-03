your_sentence = input().lower()
letter_counts = {}
for letter in your_sentence:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1
letter_items = list(letter_counts.keys())
letter_items.sort()
for i in letter_items:
    for key, value in letter_counts.items():
        if i == key:
            print(key, " ", value)