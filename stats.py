def count_words(book_text):
    words = book_text.split()

    return len(words)

def count_characters(book_text):
    characters = {}

    for ch in book_text:
        c = ch.lower()
        if c not in characters:
            characters[c] = 0

        characters[c] += 1

    return characters

def sort_on(items):
    return items['num']

def sort_characters(characters):
    ch_arr = []
    for ch, count in characters.items():
        if (ch.isalpha()):
            ch_dict = {
                "char": ch,
                "num": count
            }
            ch_arr.append(ch_dict)

    ch_arr.sort(reverse=True, key=sort_on)
    return ch_arr

