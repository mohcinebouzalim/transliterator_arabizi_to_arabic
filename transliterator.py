#import libraries
import codecs
import json
import os

#load json file
latin_to_ar = json.loads(open('mapping.manual.json', encoding='utf-8').read())

dict_words = {}
word_counts = codecs.open('arabic.txt', encoding='utf-8').read().split("\n")
for word_count in word_counts:
  if word_count:
    word, n = word_count.split()
    dict_words[word] = int(n)

def sort_key(word):
    if word in dict_words: return dict_words.get(word)
    else: return 1

def sort_by_frequency(words):
    return sorted(words, reverse=True, key=sort_key)

def transliterate_word(latin):
    all_words = set()
    def recursive_search(letters, word, start=False):
        if len(letters) == 0:
            all_words.add(word)
            return
        if start:
            table = latin_to_ar['start']
        else:
            table = latin_to_ar['other']
        max_length = len(max(list(table), key=len))
        for i in range(1, max_length+1):
            l = letters[:i]
            if l in table:
                for ar in table[l]:
                    recursive_search(letters[i:], word+ar)

    recursive_search(latin, '', True)
    return all_words


def transliterate(sentence):
    words = sentence.split()
    new = []
    for word in words:
        all_words = list(transliterate_word(word))
        new.append(sort_by_frequency(all_words)[0])
    return ' '.join(new)
