class complex_num:
    def __init__(self, real : str, nreal : str):
        self.real = real
        self.nreal = nreal

    def __str__(self):
        return f'{self.real} + {self.nreal}'