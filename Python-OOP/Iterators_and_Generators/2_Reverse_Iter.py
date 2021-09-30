class reverse_iter:
    def __init__(self, input_list):
        self.list = input_list
        self.index = None

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index < - len(self.list):
            raise StopIteration
        else:
            return self.list[self.index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)






