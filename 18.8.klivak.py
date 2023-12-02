class Sorted:
    def __init__(self, iterable):
        self._data = sorted(iterable)

    def __iter__(self):
        return iter(self._data)

class SortedSet(Sorted, set):
    def __init__(self, iterable):
        Sorted.__init__(self, iterable)
        set.__init__(self, iterable)

    def __str__(self):
        return f"Відсортований набір({set(self).__str__()})"

if __name__ == "__main__":
    unsorted_data = [7, 2, 4, 1, 5, 9, 3, 6, 7, 0, 5]

    sorted_set = SortedSet(unsorted_data)
    print(sorted_set)
