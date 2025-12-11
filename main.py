def get_book_text(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()

if __name__ == "__main__":
    book_text = get_book_text('books/frankenstein.txt')
    print(book_text)