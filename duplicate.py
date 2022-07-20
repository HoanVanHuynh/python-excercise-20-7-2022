

sentence = input("Write your sentence")
sentence = sentence.split()

def compare(sentence):
    duplicate = False
    for word in sentence:
        if len(word) != len(set(word)):
            duplicate = True
            return duplicate
        else:
            continue
    return duplicate 


compare(sentence)