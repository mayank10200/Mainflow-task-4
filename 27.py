#-------------------------------------------
#Longest Word in a Sentence
#--------------------------------------------
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# User Input
sentence = input("Enter a sentence: ")
print("Longest Word:", longest_word(sentence))
