"""
Stacked submission by Rohit Nimkar (nehalnimkar@gmail.com)
"""

if __name__ == '__main__':
    input()
    # amount of silver in each shop
    S = sorted([int(i) for i in input().split()], reverse=True)
    op = []
    for i in range(int(input())):
        p = int(input())
        pay = 0
        not_looted = [*S]
        while not_looted:
            popped = not_looted.pop()
            pay += popped
            not_looted = not_looted[p:]
        op.append(pay)
    print(*op, sep="\n")
