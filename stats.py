def get_book_text(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()


def get_count(text_list: list[str]) -> int:
    return len(text_list)