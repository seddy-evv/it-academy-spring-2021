# The function takes the text and counts the number of
# distinct words separated by spaces and end-of-line characters.


def count_different_words(text):
    print(len({sentence for sentence in text.split()}))


rand_text = """Walking, running, cycling and and
              playing football are some kinds
              of sports that     you do every day day"""
count_different_words(rand_text)
