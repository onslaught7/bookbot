def get_book_text(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()


def get_count(text: str) -> int:
    words_list = text.split()

    return len(words_list)


def get_char_count(text: str) -> str:
    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count