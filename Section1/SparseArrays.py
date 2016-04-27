import collections
Query = collections.namedtuple("Query","type x y")

class SparseArray:
    def __init__(self):
        self.string = []
        self.queries = []
        self.lastAns = 0
        number_of_strings= int(input().strip())
        for i in range(number_of_strings):
            self.string.append(input().strip())
        number_of_queries= int(input().strip())
        for i in range(number_of_queries):
            self.queries.append(input().strip())

    def calculate(self):
        for query in self.queries:
            count=0
            for string in self.string:
                if query == string:
                    count+=1
            print(count)


def main():
    dynamic_array = SparseArray()
    dynamic_array.calculate()



if __name__ == "__main__":
    main()