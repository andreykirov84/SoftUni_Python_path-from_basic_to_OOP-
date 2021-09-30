class vowels:
    def __init__(self, input_string):
        self.list = list(input_string)
        self.index = -1
        self.vowel = ['A', 'a', 'E', 'e', 'I', 'i', 'U', 'u', 'Y', 'y', 'O', 'o']
        self.final_list = []

    def __iter__(self):
        return self

    def __next__(self):
        for i in self.list:
            if i in self.vowel:
                self.final_list.append(i)
            else:
                pass
        print(self)

        self.index += 1
        if self.index == len(self.list):
            raise StopIteration
        else:
            return self.final_list[self.index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

