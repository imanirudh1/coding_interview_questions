sentence='       hello   world '
def sentence_reversal(sentence):
    s=' '
    i=0
    word=[]
    while i < len(sentence):
        if sentence[i] not in s:
            wordstart=i
            while sentence[i] not in s and i < len(sentence):
                i+=1
            word.append(sentence[wordstart:i])
        i+=1
    return ' '.join(word[::-1])    
print(sentence_reversal(sentence))        