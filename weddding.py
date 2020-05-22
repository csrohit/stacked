from itertools import combinations
if __name__ == '__main__':
    R,G,B = 4,2,2
    Gmax = R-1
    Bmax = B//2
    Gmin = R - Bmax
    Bmin = 1
    # 4 2 8
    # two rooms for each side
    nG = len(list(combinations(range(2),1)))
    print("nG: %d" % nG)
    nB = len(list(combinations(range(8),2))) + len(list(combinations(range(8),3))) + len(list(combinations(range(8),4)))
    print("nB: %d" % nB)

    # one room for groom and 3 rooms for bride
    print("\n1 and 3")
    nG = len(list(combinations(range(2),2)))
    print("nG: %d" % nG)
    nB = len(list(combinations(range(8),3)))*len(list(combinations(range(5),3))) + len(list(combinations(range(8),4)))*len(list(combinations(range(4),2)))
    print("nB: %d" % (nB/6))
