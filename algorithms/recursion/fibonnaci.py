class Fibonnaci:

    def calculate(self, nth: int):
        if nth <= 1:
            return nth
        else:
            return self.calculate(nth - 1) + self.calculate(nth - 2)
