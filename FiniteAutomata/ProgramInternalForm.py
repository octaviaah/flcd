class PIF:
    def __init__(self):
        self.__items = []

    #position is a list with 2 elements:
    #first element is the hash key
    #second element is the position in the deque corresponding to the hash key
    def add(self, token, position):
        self.__items.append((token, position))

    def __str__(self):
        result = ""
        for item in self.__items:
            result += item[0] + " -> " + str(item[1]) + "\n"
        return result