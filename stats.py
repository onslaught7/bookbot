def get_book_text(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()


def get_count(text: str) -> int:
    words_list = text.split()

    return len(words_list)


def get_char_count(text: str) -> dict:
    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def get_sorted_char_dict(char_count: dict) -> list:
    char_count_list = list(char_count.items())
    char_count_list.sort(key=lambda x: x[1], reverse=True)

    return char_count_list