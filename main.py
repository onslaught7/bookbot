from stats import get_book_text, get_count


if __name__ == "__main__":
    book_text = get_book_text('books/frankenstein.txt').split()
    word_count = len(book_text)

    print(f"Found {word_count} total words")