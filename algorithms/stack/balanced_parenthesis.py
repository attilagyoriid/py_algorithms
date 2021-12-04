from data_structures.stack import Stack


class BalancedParenthesis:

    @staticmethod
    def check(parenthesis_text: str) -> bool:
        if len(parenthesis_text) % 2 != 0:
            return False

        opening = set('([{')

        matches = set([('(', ')'), ('[', ']'), ('{', '}')])

        stack = Stack()

        for paren in parenthesis_text:

            if paren in opening:
                stack.push(paren)

            else:

                if stack.size() == 0:
                    return False

                last_open = stack.pop()

                if (last_open, paren) not in matches:
                    return False

        return stack.size() == 0
