
def wordcounts(words):
    frequency = [words.count(word) for word in words]
    return dict(zip(word,frequency)


