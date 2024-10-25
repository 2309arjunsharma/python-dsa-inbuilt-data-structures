def count_word_frequency(sentence):
    # Your code goes here
    word_count={}
    w=sentence.split()
    for word in w:
        if word in word_count:
            word_count[word]+=1
            
        else:
            word_count[word]=1
    return word_count
sentence="Fear leads to anger and anger leads to hatred and hatred leads to conflict and conflict leads to suffering." 
word_frequency=count_word_frequency(sentence)
print(word_frequency)
