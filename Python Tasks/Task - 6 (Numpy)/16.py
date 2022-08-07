# Words Score
VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
def score_words(words):
    score = 0
    for w in words:
        v = sum([1 for l in w if l in VOWELS])
        score = score + 2 if v%2 == 0 else score + 1
    return score


n = int(input())
words = input().split()
print(score_words(words))