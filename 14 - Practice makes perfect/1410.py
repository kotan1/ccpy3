def censor(text, word):
    res = ""
    
    words = text.split()
    
    for i in range(0, len(words)):
        if words[i] == word:
            words[i] =  "*" * len(word)
            
    res = " ".join(words)
        
    return res

print censor("this hack is wack hack", "hack")
