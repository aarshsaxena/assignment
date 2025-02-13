class MyIterator:
    def __init__(self, max_n):
        self.max_n = max_n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_n:
            raise StopIteration
        result = self.current
        self.current += 1
        return result


class NestedIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.index = 0
        self.sub_iterator = None

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.nested_list):
            current = self.nested_list[self.index]

            if isinstance(current, list):
                if self.sub_iterator is None:
                    self.sub_iterator = NestedIterator(current)

                try:
                    return next(self.sub_iterator)
                except StopIteration:
                    self.sub_iterator = None
                    self.index += 1
            else:
                self.index += 1
                return current

        raise StopIteration


iterator = MyIterator(10)

for num in iterator:
    print(num)

list1 = [[1, 2], [3, 4], [5]]
iterator = NestedIterator(list1)

for num in iterator:
    print(num)
