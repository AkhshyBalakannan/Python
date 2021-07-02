from random import randint


class Random:
    """Iterator for looping to generate jumbled char"""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        self.rand = self.index
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        n = randint(0, self.rand)
        return self.data[n]


# full_name = input("ENTER YOUR NAME:  ")
# uni_id = Random(full_name)
# val = ''
# for char in uni_id:
#     val += char
# print('YOUR UNI-CODE GENERATED BY ITERATOR ', val)
