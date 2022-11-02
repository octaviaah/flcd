from collections import deque


class HashTable:
    def __init__(self, size, table_name):
        self.__size = size
        self.__table_name = table_name
        self.__items = [deque() for _ in range(size)]

    def hash(self, key):
        #hash function: h(k) = k mod m
        #k is sum of all ASCII values of key's characters
        #m is size of hash table
        sum = 0
        for character in key:
            sum += ord(character)
        return sum % self.__size

    def contains(self, key):
        return key in self.__items[self.hash(key)]

    def get(self, key):
        #get position of key inside the hash table
        position = self.hash(key)
        index = 0

        for item in self.__items[position]:
            if item != key:
                index += 1
            else: break

        return position, index

    def add(self, key):
        if self.contains(key):
            return self.get(key)
        self.__items[self.hash(key)].append(key)
        return self.get(key)

    def __str__(self):
        result = self.__table_name + ":"
        for i in range(self.__size):
            if len(self.__items[i]) != 0:
                result = result + str(i) + "-" + str(self.__items[i]) + '\n'
        return result