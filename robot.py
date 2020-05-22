"""
Stacked submission by Rohit Nimkar (nehalnimkar@gmail.com)
"""

if __name__ == '__main__':
    # size of the grid
    n = int(input())
    # initial coordinates
    x, y = map(int, input().split())
    # number of moves
    m = int(input())
    fall = False
    for i in range(m):
        dir, steps = input().split()
        steps = int(steps)
        if dir == 'E':
            x += steps
        elif dir == 'W':
            x -= steps
        elif dir == 'N':
            y -= steps
        elif dir == 'S':
            y += steps
        if x<0 or x>n or y<0 or y>n:
            fall = True
    if fall:
        print("FALL")
    else:
        print(x, y)