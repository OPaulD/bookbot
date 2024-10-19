def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    word_count = count_words(text)
    number_of_individual_characters = count_characters(text)
    sorted_characters = sort_characters(number_of_individual_characters)

    print(f"\n--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for i in sorted_characters:
        if not i["char"].isalpha():
            continue
        print(f"The '{i['char']}' character was found {i['num']} times")

    print("\n--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def sort_characters(character_dict):
    unsorted_characters = []
    sorted_characters = []
    for i in character_dict:
        unsorted_characters.append({"char":i, "num":character_dict[i]})
    
    sorted_characters = sorted(unsorted_characters, key= lambda d: d["num"], reverse=True)
    return sorted_characters


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
