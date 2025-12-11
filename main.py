from stats import get_book_text, get_char_count


if __name__ == "__main__":
    book_text = get_book_text('books/frankenstein.txt')
    char_count = get_char_count(book_text)

    print(char_count)