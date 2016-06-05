import collections
import math
Box = collections.namedtuple('Box', 'w l h')
FootPrint = collections.namedtuple('FootPrint', 'area w l')
Volume =  collections.namedtuple('FootPrint', 'area w l h')
def read_input():
    number = int(input())
    box = Box(*get_int_list(input()))
    return number, box


class Solution:
    def __init__(self):
        self.number, self.box = read_input()
        self.dp_floor = {}

    def calculate(self):
        result = self.get_configuration()
        return result.area

    def get_configuration(self):
        best_area = None
        for height in range(1,self.number+1):
            bottom = self.get_squarest(math.ceil(self.number/height))
            my_area = Volume(self.get_area(bottom.w,bottom.l,height),bottom.w,bottom.l,height)
            if best_area is None or my_area.area < best_area.area:
                best_area = my_area
        return best_area

    def get_squarest(self, foot_print):
        if foot_print not in self.dp_floor:
            best_footprint = None
            for width in range(1,foot_print+1):
                length = math.ceil(foot_print/width)
                my_footprint = FootPrint(self.get_outside_len(width,length),width,length)
                if best_footprint is None or my_footprint.area < best_footprint.area:
                    best_footprint = my_footprint
            self.dp_floor[foot_print]= best_footprint
        return self.dp_floor[foot_print]


    def get_outside_len(self, width, length):
        return 2*width*self.box.w+2*length*self.box.l

    def get_area(self, width, length, height):
        lengths = Box(width*self.box.w,length*self.box.l,height*self.box.h)
        return 2*lengths.w*lengths.l+2*lengths.w*lengths.h+2*lengths.l*lengths.h



def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
