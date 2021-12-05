class FileStub:
    def __init__(self):
        self.current_index = 0
        self.array = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index == len(self.array):
            raise StopIteration
        else:
            current_value = self.array[self.current_index]
            self.current_index += 1
            return current_value + '\n'

    def set_array(self, array):
        self.array = array

    def readline(self):
        return next(self)

    def read(self):
        return '\n'.join(self.array)