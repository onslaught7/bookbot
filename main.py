from stats import get_book_text, get_count, get_char_count, get_sorted_char_dict


if __name__ == "__main__":
    book_text = get_book_text('books/frankenstein.txt')
    word_count = get_count(book_text)
    char_count = get_char_count(book_text)
    sorted_char_list = get_sorted_char_dict(char_count)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in sorted_char_list:
        if char.isalpha():
            print(f"{char}: {count}")