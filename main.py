def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    word_count = count_words(text)
    number_of_individual_characters = count_characters(text)
    print(f"\n{word_count} words found in the document.")
    print(number_of_individual_characters)



def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    characters_count = {}
    lower_text = text.lower()

    for i in lower_text:
        if i in characters_count:
            characters_count[i] += 1
        else:
            characters_count[i] = 1
    return characters_count


main()
