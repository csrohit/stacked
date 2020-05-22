"""
Stacked submission by Rohit Nimkar(nehalnimkar@gmail.com)
"""
from collections import deque

if __name__ == '__main__':
    op = []
    for _ in range(int(input())):
        input()
        birds = deque(map(int, input().split()))
        # print(birds)
        albert = 0
        binnie = 0
        moves = 0
        prev_albert = 0
        prev_binnie = 0

        while birds:
            moves +=1
            if albert <= binnie:
                prev_albert = 0
                while prev_albert <= prev_binnie and birds:
                    prev_albert += birds.popleft()
                albert += prev_albert
            else:
                prev_binnie = 0
                while prev_binnie <= prev_albert and birds:
                    prev_binnie += birds.pop()
                binnie += prev_binnie
        op.append("%d %d %d" %(moves, albert, binnie))
    print(*op, sep="\n")