import collections


def read_input():
    width, height = get_int_list()
    n_shapes = int(input())
    shapes = []
    for i in range(n_shapes):
        line = input().strip().split()
        if line[0] == Solution.C:
            shape = [line[0], int(line[1])]
        else:
            shape = [line[0], int(line[1]), int(line[2])]
        shapes.append(shape)
    return width, height, shapes


class Solution:
    R, C = 'R', 'C'

    def __init__(self):
        self.width, self.height, self.shapes = read_input()

    def calculate(self):
        for shape in self.shapes:
            if self.fits(shape):
                print('YES')
            else:
                print('NO')

    def fits(self, shape):
        if shape[0] == self.C:
            return (shape[1] * 2) <= min(self.width, self.height)
        else:
            if shape[1] <= self.width and shape[2] <= self.height:
                return True
            if shape[2] <= self.width and shape[1] <= self.height:
                return True
            return self.sophisticated_pack(shape)

    def sophisticated_pack(self, shape):
        postbox_h2 = (self.height / 2.) ** 2
        postbox_w2 = (self.width / 2.) ** 2
        shape_radius_sq = ((shape[1] / 2.) ** 2 + (shape[2] / 2.) ** 2)
        intersection_width = abs(shape_radius_sq - postbox_h2) ** 0.5
        intersection_height = abs(shape_radius_sq - postbox_w2) ** 0.5
        len1 = (abs(self.width/2.+intersection_width)**2+abs(self.height/2. + intersection_height)**2)**0.5
        len2 = (abs(self.width/2.-intersection_width)**2+abs(self.height/2. - intersection_height)**2)**0.5
        if shape[1] <= len1 and shape[2] <= len2:
            return True
        if shape[2] <= len1 and shape[1] <= len2:
            return True
        return False


def main():
    my_object = Solution()
    my_object.calculate()


def get_int_list():
    return [int(i) for i in input().strip().split()]


if __name__ == "__main__":
    main()
