from typing import List, Tuple


class SumUp:

    @staticmethod
    def get_sum_up_pairs(ls: List, num: int) -> List[Tuple]:
        result = []
        i = 1
        for n in ls:
            print(ls[i:])
            for k in ls[i:]:

                if n + k == num:
                    result.append((n, k))
            i += 1
        return result

    @staticmethod
    def get_sum_up_pairs2(arr, k):

        if len(arr) < 2:
            return

        seen = set()
        output = set()

        for num in arr:

            target = k - num

            if target not in seen:
                seen.add(num)

            else:

                output.add((min(num, target), max(num, target)))

        return len(output)
