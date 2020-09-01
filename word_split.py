def word_split(phrase,listofword,output=None):
    if output is None:
        output=[]
    for word in listofword:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):],listofword,output)    
    return output  

      
print(word_split('mantheran',['the','ran','man']))
    