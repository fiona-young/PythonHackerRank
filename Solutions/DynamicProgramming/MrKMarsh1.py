
class Solution:
    def __init__(self):
        self.data = []
        self.rows, self.cols = get_int_list(input())
        for i in range(self.rows):
            self.data.append([1 if val == '.' else 0 for val in input().strip()])
        self.dp = [[[] for j in range(self.cols)] for i in range(self.rows)]
        self.left = [[0] * self.cols for i in range(self.rows)]
        self.up = [[0] * self.cols for i in range(self.rows)]
        self.max = None

    def calculate(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j]:
                    if j > 0 and self.data[i][j - 1]:
                        self.left[i][j] = self.left[i][j - 1] + 1
                    if i > 0 and self.data[i - 1][j]:
                        self.up[i][j] = self.up[i - 1][j] + 1
                    self.find_rectangles(i, j)
        if self.max is None:
            return 'impossible'
        else:
            return self.max

    def add_max(self,rect):
        perimeter = 2*rect[0]+2*rect[1]
        if self.max is None or perimeter > self.max:
            self.max=perimeter

    def find_rectangles(self, row, col):
        up, left = self.up[row][col], self.left[row][col]
        if up == 0 or left == 0:
            return
        rect = self.get_rect_dimens(row, col, up, left)
        if rect is None:
            return
        self.add_rectangles(row, col, rect)

    def add_rectangles(self, row, col, new_rect):
        depth, width = new_rect
        self.add_max(new_rect)
        above=[]
        left=[]
        if (row - depth) >= 0:
            above = self.dp[row-depth][col]
        if (col - width) >= 0:
            left = self.dp[row][col-width]
        self.combine_rects(self.dp[row][col],new_rect,above,left)

    def add_rect_rows(self, new_rect, above_rects):
        add_list = []
        remaining_list =[]
        for above in above_rects:
            if new_rect[1] == above[1]:
                add_list.append((new_rect[0]+above[0],new_rect[1]))
            else:
                remaining_list.append(above)
        return add_list, remaining_list

    def add_rect_cols(self,new_rect, left_rects):
        add_list = []
        remaining_list =[]
        for left in left_rects:
            if new_rect[0] == left[0]:
                add_list.append((new_rect[0],new_rect[1]+left[1]))
            else:
                remaining_list.append(left)
        return add_list, remaining_list

    def combine_rects(self, destination, new_rect, rect_above, rect_left):
        destination.append(new_rect)
        if len(rect_above)!=0 or len(rect_left)!=0:
            rects_from_left,remaining_left = self.add_rect_cols(new_rect, rect_left)
            rects_from_above, remaining_above = self.add_rect_rows(new_rect, rect_above)
            self.add_rect_to_dp(destination, rects_from_left)
            self.add_rect_to_dp(destination, rects_from_above)
            for rect_left in remaining_left :
                extra, _ = self.add_rect_cols(rect_left,rects_from_above)
                self.add_rect_to_dp(destination, extra)
            for rect_above in remaining_above:
                extra, _ = self.add_rect_rows(rect_above,rects_from_left)
                self.add_rect_to_dp(destination, extra)

    def add_rect_to_dp(self, destination, add_list):
        for add_rect in add_list:
            destination.append(add_rect)
            self.add_max(add_rect)


    def get_rect_dimens(self, row, col, up, left):
        for i in range(1, up + 1):
            for j in range(1, left + 1):
                if self.left[row - i][col] >= j and self.up[row][col - j] >= i:
                    return i, j
        return None

def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
