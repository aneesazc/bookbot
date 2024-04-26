def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print("--- Begin report of books/frankenstein.txt ---\n" )
    word_count = count_words(text)
    print(f"{word_count} words found in the document")
    letter_count = count_letters(text)
    words_dict = dict_list(letter_count)
    sorted_words = sort_dict(words_dict)
    for word in sorted_words:
        c, count = list(word.items())[0]
        print(f"The '{c}' character was found {count} times")
    print("\n--- End report ---")



def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_letters(text):
    count = {}
    for c in text:
        c = c.lower()
        if c.isalpha():
            count[c] = count.get(c, 0) + 1
    return count

def dict_list(d):
    new_list = []
    for k, v in d.items():
        new_list.append({k: v})
    return new_list


def sort_on(d):
    return list(d.values())[0]

def sort_dict(d):
    return sorted(d, reverse=True, key=sort_on)


main()
