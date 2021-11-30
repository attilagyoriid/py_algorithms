from collections import defaultdict
from typing import List


class ArrayElementFinder:

    @staticmethod
    def find_first_non_matching_element(list: List, list_with_missing_item: List) -> int:
        d = defaultdict(int)

        for num in list_with_missing_item:
            d[num] += 1
        for num in list:
            if d[num] == 0:
                return num
            else:
                d[num] -= 1
