"""
Stacked submission by Rohit Nimkar(nehalnimkar@gmail.com)
"""

def check(p, q):
    r = int(q/p)
    if r > p:
        q =  check(p*(p+1), q)
        if q > p*(p+1):
            q = q % p
    return q
if __name__ == '__main__':
    d, p, q = map(int, input().split())
    if d == q:
        print("YES")
    else:
        q = q-d
        q = check(p,q)
        r = int(q/p)
        q = q%p
        if q == r or q == r-1:
            print("YES")
        else:
            print("NO")





