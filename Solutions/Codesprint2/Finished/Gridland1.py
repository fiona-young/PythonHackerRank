


class Solution:
    def __init__(self):
        self.size = int(input())
        self.array = []
        self.array.append(input().strip())
        self.array.append(input().strip())

    def calculate(self):
        if len(set(self.array[0]+self.array[1]))==1:
            return 1
        results = self.get_circles(self.array[0]+self.array[1][::-1])
        for i in range(self.size):
            seed = '' if i == 0 else self.array[0][i-1::-1]+self.array[1][0:i]
            results.update(self.get_zigzag(seed,1,i,+1))

        for i in range(self.size):
            seed = '' if i == 0 else self.array[1][i - 1::-1] + self.array[0][0:i]
            results.update(self.get_zigzag(seed, 0, i, +1))
        res_set = set(results)
        for set_str in res_set:
            results.add(set_str[::-1])
        return len(results)

    def get_circles(self,loop):
        circles = set()
        circles.add(loop)
        for i in range(self.size*2-1):
            loop = loop[1:]+loop[0]
            circles.add(loop)
        return circles

    def get_zigzag(self,seed,row,col,right):
        output = list(seed)
        steps = 0
        zigzags = set()
        while col >=0 and col <self.size:
            output.append(self.array[row][col])
            steps+=1
            row = 0 if row == 1 else 1
            #if steps < self.size*2:
            #    zigzags.add(self.add_circle_diversion(row,col,right,''.join(output)))
            output.append(self.array[row][col])
            steps+=1
            col+=right
            if steps < self.size*2:
                zigzags.add(self.add_circle_diversion(row,col,right, ''.join(output)))
        zigzags.add(''.join(output))
        return zigzags

    def add_circle_diversion(self, row, col, right, built_str):
        built_str+=self.array[row][col::right]
        remaining = 2*self.size-len(built_str)
        if remaining == 0:
            return built_str
        row = 0 if row == 1 else 1
        built_str+=self.array[row][::-1*right][:remaining]
        return built_str

def main():
    cases = int(input())
    for i in range(cases):
        my_object = Solution()
        print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()
