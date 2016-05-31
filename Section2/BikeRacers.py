import collections
import math

Coord = collections.namedtuple('Coord', 'x y')
Edge = collections.namedtuple('Edge', 'node distance')


def read_input():
    riders, bikes, max_participants = get_int_list(input())
    rider_list, bike_list = {}, {}
    for i in range(riders):
        rider_list[Coord(*get_float_list(input()))] = i
    for i in range(riders):
        bike_list[Coord(*get_float_list(input()))] = i
    return max_participants, rider_list, bike_list


class BikeRacer:
    def __init__(self):
        self.max_participants, self.riders_list, self.bike_list = read_input()
#        self.graph = collections.defaultdict(list)
#        self.dist = {}
#        self.dist_matrix = []
        self.tuples_bike = collections.defaultdict(list)
        self.tuples_rider = collections.defaultdict(list)
        self.distances = []

    def calculate_distances(self):
        for i_rider, rider in enumerate(self.riders_list):
            dist = []
            for i_bike, bike in enumerate(self.bike_list,len(self.riders_list)):
                distance = math.sqrt((rider.x - bike.x) ** 2 + (rider.y - bike.y) ** 2)
                dist.append(distance)
                self.tuples_bike[i_bike].append((distance, i_rider))
                self.tuples_rider[i_rider].append((distance, i_bike))
                self.distances.append((distance, i_rider, i_bike))
#            self.dist_matrix.append(dist)
        for bike_list in self.tuples_bike.values():
            bike_list.sort()
        for rider_list in self.tuples_rider.values():
            rider_list.sort()
        self.distances.sort()
        rider_d=collections.defaultdict(set)
        bike_d =collections.defaultdict(set)
        pair=set()
        i_pointer = 0
        distance = 0
        while len(bike_d) < self.max_participants or len(rider_d) < self.max_participants or get_independent_set_count(bike_d)<self.max_participants:
            distance,rider, bike = self.distances[i_pointer]
            pair.add((rider,bike))
            bike_d[bike].add(rider)
            rider_d[rider].add(bike)
            i_pointer += 1
        return distance

    def calculate(self):
        return round(self.calculate_distances() ** 2)

def get_independent_set_count(bike_d):
    count = 0
    already_used = set()
    for rider_set in bike_d.values():
        if len(rider_set.difference(already_used)) > 0:
            count += 1
        already_used.update(rider_set)
    return count

def main():
    my_obj = BikeRacer()
    print(my_obj.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


def get_float_list(in_str):
    return [float(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
