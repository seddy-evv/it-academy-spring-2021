def return_longest_word(text):
    clean_text = text.replace(",", "")
    clean_text = clean_text.replace(".", "")
    strings = clean_text.split()
    longest_word = ""
    for current_str in strings:
        if len(current_str) > len(longest_word):
            longest_word = current_str
    return longest_word


sentence = ("Walking, running, cycling and "
            "playing football are some kinds "
            "of sports that you do every day.")
print(return_longest_word(sentence))
