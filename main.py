def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_report(book_path):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(num_words)
    print(chars_dict)

    chars_list = list(chars_dict.items())
    chars_list.sort(key=lambda a: a[1], reverse=True)
    print(chars_list)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for character, count in chars_list:
        if character.isalpha():
            print(f"The '{character}' character was found {count} times")

    print("--- End report ---")

def main():
    book_path = "books/frankenstein.txt"
    get_report(book_path)

################################################################################
main()