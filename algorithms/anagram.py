from typing import Dict


class Anagram:

    @classmethod
    def anagram(cls, text1: str, text2: str) -> bool:
        char_map1 = cls._get_char_map(cls._get_text_without_whitespace(text1))
        char_map2 = cls._get_char_map(cls._get_text_without_whitespace(text2))
        return cls._is_char_maps_equal(char_map1, char_map2)

    @staticmethod
    def _get_text_without_whitespace(text: str) -> str:
        return text.lower().replace(' ', '')

    @staticmethod
    def _get_char_map(text: str) -> Dict:
        text_map = {}
        for c in text:
            if c not in text_map:
                text_map[c] = 0
            text_map[c] += 1

        return text_map

    @staticmethod
    def _is_char_maps_equal(char_map1: Dict, char_map2: Dict) -> bool:
        if len(char_map1) != len(char_map2):
            return False
        try:
            for k in char_map1.keys():
                if char_map1[k] != char_map2[k]:
                    return False
        except KeyError:
            return False
        return True
