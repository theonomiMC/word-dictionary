import json
import difflib

data = json.load(open('eng_dict/data.json'))


def translate(w):
    if w in data:
        return  "\n".join(data[w])

    elif difflib.get_close_matches(w, data.keys(), cutoff=0.7):
        matched_w = difflib.get_close_matches(w, data.keys(), cutoff=0.7)[0]
        ask = input(f"Did you mean {matched_w}? 'Y' or 'N': ").lower()
        if ask == 'y':
            return "\n".join(data[matched_w])
    return 'No such word on dictionary!'


def app():
    word = input('Enter word to translate: ').lower()

    return translate(word)


print(app())


# print(formated_list(['a', 'b', 'c']))
