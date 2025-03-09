
def get_number_of_words(text: str) -> int:
    return len(text.split())


def get_character_count(text: str) -> dict[str , int]:
    character_map: dict[str, int] = {}
    for c in text:
        lower_char = c.lower()
        if lower_char in character_map:
            character_map[lower_char] += 1
        else:
            character_map[lower_char] = 1
    return character_map


def get_sorted_characters(char_dict:dict[str,int]) -> dict[str, int]:
    sorted_char_list: list[tuple] = sorted(char_dict.items(),reverse=True, key=lambda x: x[1])
    sorted_char_dict: dict[str, int] = dict(sorted_char_list)
    return sorted_char_dict