import math
from string import ascii_uppercase

def is_triangle_num(x):
    n = int(math.ceil(math.sqrt(x * 2)))
    y = n * (n - 1) / 2
    return x == y
  
def word_to_num(w):
    L = list(ascii_uppercase)
    return sum(map(lambda x: L.index(x) + 1, w))
	
def is_triangle_word(w):
    return is_triangle_num(word_to_num(w))

def words_from_file():
    with open(r'C:\temp\words.txt') as f:
        for w in f.read().split(','):
            w = w.strip('"')
            yield w

print len([w for w in words_from_file() if is_triangle_word(w)])

