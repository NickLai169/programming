# f = open("horse_ebooks.txt", "r")
# text = f.read()
# print(text)

word = 'abcdefg'


def read_file(filename):
    """Returns the text contained in file with given filename."""
    f = open(filename, "r")
    text = f.read()
    return text

def remove_punctuation(word):
    '''takes a word and removes the punctuations from the word'''
    punctuations = [',', '.', '/',"'", '"',';', ':', '[', ']', '(', ')', '?', '!']
    if word == '':
        return ''
    else:
        if word[0] in punctuations:
            return remove_punctuation(word[1:])
        else:
            return word[0] + remove_punctuation(word[1:])

def remove_punctuation_itr(word):
    '''takes a word and removes the punctuations from the word iteratively'''
    punctuations = [',', '.', '/',"'", '"',';', ':', '[', ']', '(', ')', '?', '!']
    new_word = ''
    for i in word:
        if i not in punctuations:
            new_word += i
    return new_word

def count_words(text):
    """Takes a text and returns a dictionary mapping each word to its count, for example:

    count_words(["Fruits and Vegetables and Vegetables on a Budget and Vegetables at a Store and Vegetables to Clean Fruit and Vegetables"])

    would return:
    {'and': 5, 'on': 1, 'Vegetables': 5, 'Budget': 1, 'to': 1, 'Fruit': 1, 'a': 2, 'Clean': 1, 'Fruits': 1, 'Store': 1, 'at': 1}
    """
    new_dict = {}
    for i in text.split():
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    return new_dict
# NOTE: for this one I'm not too sure whether the input should be a list or a string, double check

def pig_latin(word):
    '''returns the pig-latin of a word'''
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_word = ''
    while word != '':
        if word[0] in vowels:
            return word + new_word + 'ay'
        else:
            new_word = new_word + word[0]
            word = word[1:]
    return new_word + 'ay'

def izzle(word):
    '''return the izzle translation of a word'''
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0
    position = 0
    how_many_vowels = 0
    for i in word:
        if i in vowels:
            position = counter
            how_many_vowels += 1
        counter += 1
    if how_many_vowels > 1:
        return word[:position] + 'izzle'
    else:
        return word + 'izzle'

def apply_language_game(text, language_game):
    return ' '.join([language_game(i) for i in text.split()])

def top_n_words(counts, n):
    return sorted(counts, key = counts.get, reverse = True)[:n]

def print_top_n_words(counts, n):
    for i in top_n_words(counts, n):
        print(i, counts[i])

def top_n_words_except(counts, n, boring):
    new_dict = {}
    for i in counts:
        if i not in boring:
            new_dict[i] = counts[i]
    return sorted(new_dict, key = new_dict.get, reverse = True)[:n]

def average_word_length(counts):
    return sum([len(i) for i in counts.split()])/len(counts.split())

def word_diversity(counts):
    return len(set(counts.split()))/len(counts.split())




# text = read_file("gettysburg.txt")
# print(apply_language_game(text, izzle))
