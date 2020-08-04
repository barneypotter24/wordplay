import sys
sys.path.append('.')

def load_words():
    with open('data/words_alpha.txt') as word_file:
        valid_words = [ word for word in word_file.read().split() ]
        # valid_words = set(word_file.read().split())
    return valid_words

if __name__ == '__main__':
    english_words = load_words()
    print('fate' in english_words)
