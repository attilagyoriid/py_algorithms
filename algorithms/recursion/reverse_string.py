class ReverseString:

    def reverse(self, s: str):
        if len(s) <= 1:
            return s
        return self.reverse(s[1:]) + s[0]
