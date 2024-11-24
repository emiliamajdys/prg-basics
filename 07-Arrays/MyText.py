def fa(word):
    return len(word.split())

def fb(word):
    words = word.split()
    return sorted(words, key=len, reverse=True)

def fc(word):
    words=word.split()
    return sorted(words)