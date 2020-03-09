import random

def get_kgram(text, ptr, k):
    """Returns the kgram starting at position ptr in a text. For example:
    get_kgram("hello", 0, 3) would return "hel"
    get_kgram("hello", 1, 3) would return "ell"
    get_kgram("hello", 1, 4) would return "ello"
    get_kgram("hello", 3, 4) would crash since 3 + 4 is longer than the string."""
    if len(text) < ptr + k:
        print(ptr, '+', k, 'is longer than the string')
    else:
        return text[ptr: ptr + k]
# print(get_kgram('bo ba bee', 0, 4))

def build_markov_model(text, k):
    dict = {}
    for i in range(len(text) - k):
        # print(dict)
        current_kgram = get_kgram(text, i,k)
        # print(current_kgram)
        if current_kgram not in dict:
            # dict[current_kgram] = {text[i + k + 1]:1}
            dict[current_kgram] = {text[i + k]: 1}
        else:
            if text[i + k] in dict[current_kgram]:
                dict[current_kgram][text[i + k]] += 1
            else:
                dict[current_kgram][text[i + k]] = 1
    return dict
# print(build_markov_model('the ether', 3))

def next_character_frequency(m, kgram, c):
    """ Returns the number of times c follows kgram
    m is the model (a dictionary)
    kgram is a kgram in in m
    c is a character that follows the given kgram"""
    if kgram in m:
        return m[kgram][c]
    else:
        return 0

# text = "the theremin in the basement is the theologian's theft detection device."
text = "Look, no one ever said Jotaro Kujo was a nice guy. I beat the crap outta people, more than I have to. Some are even still in the hospital. I've had idiot teachers who like to talk big, so I taught them a lesson, and they never came back to class. If I go to a restaurant and the food is bad, I make it a policy to stiff 'em with the bill. But, even a bastard like me... can spot true evil when he sees it! True evil, are those who use the weak for their own gain, then crush them underfoot when they're through! Especially an innocent woman! And that is exactly what you've done, isn't it? And your Stand gets to hide from the victim, the law, and the consequences. That's why... I will judge you myself!"
m = build_markov_model(text, 4)
# print(m)

def random_character(m, kgram):
    """returns a random character obeying markov model
    m is the model (a dictionary)
    kgram is a kgram in in m"""
    lst = []
    for i in m[kgram]:
        for i2 in range(m[kgram][i]):
            lst.append(i)
    # print(lst)
    return random.choice(lst)

def generate_random_text(m, N):
    """Returns A randomly generated text of length N
    that obeys the probability distribution specified in m.

    m is a Markov Model
    N is the desired output length"""
    curr_text = random.choice(list((m.keys())))
    k_length = len(curr_text)
    N -= len(curr_text)
    for i in range(N):
        # print(curr_text)
        # print(curr_text[::-1][:k_length][::-1])
        if curr_text[::-1][:k_length][::-1] in m:
            temp = random_character(m, curr_text[::-1][:k_length][::-1])
            # print('path 1', temp)
            curr_text += temp
        else:
            temp = random.choice(list(m.keys()))
            # print('path 2', temp)
            curr_text = curr_text[:len(curr_text) - 2]
            curr_text +=  temp
    return curr_text

# print(generate_random_text(m, 400))
# dict = {'a': 1, 'b': 2, 'c': 3}
# print(dict.keys())
