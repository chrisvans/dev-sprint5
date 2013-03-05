def make_word_dict(l):
    scrabble_dict = {}
    for letter in l:
        if letter in scrabble_dict:
            scrabble_dict[letter] = scrabble_dict[letter] + 1
        else:
            scrabble_dict[letter] = 1
    return scrabble_dict

def signature(s):
    t = list(s)
    scrabble_dict = make_word_dict(t)
    print scrabble_dict
    return scrabble_dict


def all_possibilities(filename, scrabble_letters, min_num_letters, total_word_length):
    """
    Takes in a filename, the letters you have in your tray, the minimum number of 
    letters in your tray that you need to include in your word, and the maximum length
    of word you want.
    """
    d = []
    for line in open(filename):
        word = line.strip().lower()
        list_word = list(word)
        word_dict = make_word_dict(list_word)
        for i in scrabble_letters.keys():
            if i in word_dict:
                if word_dict[i] > 1:
                    word_dict[i] = word_dict[i]-1
                else:
                    word_dict.pop(i)
        nums_list = word_dict.values()
        ct = 0
        for x in nums_list:
            ct = ct + x
        print list_word, nums_list, ct
        if (len(list_word) - ct) > min_num_letters and len(list_word) < total_word_length:
            d.append(word)
    return d


if __name__ == '__main__':
    scrabble_letters = 'catapult'
    scrabble_sig = signature(scrabble_letters)
    d = all_possibilities('words.txt', scrabble_sig, 5, 9)
    print d
 