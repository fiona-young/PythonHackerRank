import array


class Fenwick:
    def __init__(self, size):
        self.size = size
        self.array = array.array('l', [0] * (size + 1))
        self.bare_array = array.array('l', [0] * size)

    def update(self, key, value):
        last_value = self.bare_array[key]
        difference = value - last_value
        self.bare_array[key] = value
        tree_key = key + 1
        while tree_key < self.size + 1:
            self.array[tree_key] += difference
            tree_key += tree_key & -tree_key

    def query(self, key):
        tree_key = min(key + 1, self.size)
        sum = 0
        while tree_key > 0:
            sum += self.array[tree_key]
            tree_key -= tree_key & -tree_key
        return sum


class FenwickRangeFinder:
    def __init__(self, size):
        self.fenwick = Fenwick(size)

    def add(self, node_id):
        self.fenwick.update(node_id, 1)

    def remove(self, node_id):
        self.fenwick.update(node_id, 0)

    def range_count(self, min_val, max_val):
        count_fen = self.fenwick.query(max_val) - self.fenwick.query(min_val - 1)
        return count_fen

class PairGenerator:
    def __init__(self, pair_list, used1, used2):
        self.pair_list = pair_list
        self.used1 = used1
        self.used2 = used2

    def __repr__(self):
        return str(self.pair_list)

    def get_next(self, item1, item2):
        my_pair = PairGenerator(self.pair_list.append((item1, item2)),self.used1.union({item1}),self.used2.union({item2}))
        return my_pair

class Pairs:
    def __init__(self, list1 :list, list2: list):
        self.list1 = list1
        self.list2 = list2
        self.combination = [[PairGenerator([(item1, item2)],{item1},{item2}) for item1 in list1 for item2 in list2]]


    def get_pairs(self, length):
        calculated_length =  len(self.combination)
        my_list = [[]]
        for item1 in self.list1:
            for item2 in self.list2:
                my_list[0].append('%s:%s'%(item1,item2))
        my_list.append([])
        for i in range(1,2):
            for last_item in my_list[i-1]:
                for item1 in self.list1:
                    for item2 in self.list2:
                        my_list[i].append('%s|%s:%s'%(last_item,item1,item2))

        if length <= calculated_length:
            return self.combination[length-1]
        else:
            for i_length in range(calculated_length,length):
                self.combination.append([])
                for last_list in self.combination[i_length-1]:
                    remaining_set1 = self.set1.difference(last_set.used1)
                    for item1 in remaining_set1:
                        for item2 in self.set2.difference(last_set.used2):
                            self.combination[length-1].append(last_set.get_next(item1, item2))
                    print(last_set)
                print(i_length)
        print(self.set1, self.set2, length)


