class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.number = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number > self.end:
            raise StopIteration
        else:
            return self.number


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)

