import random
import os

z

def end():
    os.system('end')

class HangManGame:
    words = []
    with open('./files/words.txt','r', encoding='utf-8') as w:
        words = w.read().split()
    random_word = random.choice(words)
    for i in random_word:
        i = '_'
        print(i, end=' ')
    




if __name__ == '__main__':
    HangManGame