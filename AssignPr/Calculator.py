class Calcu:
    def Add(self, a, b):
        return a + b

    def Mul(self, a, b):
        return a * b

    def Sub(self, a, b):
        return a - b

    def Div(self, a, b):
        if b == 0:
            return "This is undifined"
        else:
            return a / b
