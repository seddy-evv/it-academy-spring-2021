# The function removes duplicate characters and spaces from the string.


def replace_duplicate(text):
    clean_text = text.replace(" ", "")
    new_str = ""
    for element in clean_text:
        if new_str.find(element) == -1:
            new_str += element

    return new_str


print(replace_duplicate("abc cde def"))
