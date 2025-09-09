#----------------------------------------
#Count Words in a Sentence
#----------------------------------------
def count_words(sentence):
    return len(sentence.split())

# User Input
sentence = input("Enter a sentence: ")
print("Word Count:", count_words(sentence))
