# The function takes the text and counts the number of
# distinct words separated by spaces and end-of-line characters.


def count_different_words(text):
    list_of_sentence = text.split("\n")
    list_of_words = []
    for el in list_of_sentence:
        list_of_words.extend(el.split())
    set_of_words = set()
    for el in list_of_words:
        set_of_words.add(el)
    print(len(set_of_words))


rand_text = """Walking, running, cycling and and
              playing football are some kinds 
              of sports that     you do every day day"""
count_different_words(rand_text)
