class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cursor = iter(self.list_of_list)
        self.result = [self.cursor]
        return self

    def __next__(self):
        while self.result:
            try:
                i = next(self.result[-1])
            except StopIteration:
                self.result.pop()
                continue
            if isinstance(i, list):
                self.result.append(iter(i))
            else:
                return i
        raise StopIteration


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    print(list(FlatIterator(list_of_lists_2)))


if __name__ == '__main__':
    test_3()
