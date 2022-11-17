operators = []
separators = []
reserved = []

def read_file():
    with open('token.in', 'r') as f:
        f.readline()
        for i in range(21):
            operator = f.readline().strip()
            operators.append(operator)
        for i in range(9):
            separator = f.readline().strip()
            if separator == "<space>":
                separator = " "
            separators.append(separator)
        for i in range(9):
            reservedword = f.readline().strip()
            reserved.append(reservedword)
