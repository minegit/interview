# def cal1(ch, ca, mh, ma, i, a, h):
#     x=0
#     while(x <= i):
#         lhs = ma * mh
#         rhs = (ch + h *(i-x)) * (ca+a*x)
#         if rhs >= lhs:
#             return "YES"
#         x +=1
#     return "NO"

def _cal11(caa, chh, mh, ma):
    mhc = (mh+caa-1)//caa
    chhc = (chh+ma-1)//ma
    if mhc <= chhc:
        return  True
    return False

def cal(ch, ca, mh, ma, i, a, h):
    x=0
    while(x <= i):
        caa = ca+a*x
        chh = ch + h *(i-x)
        ans1 = _cal11(caa, chh, mh, ma)
        if(ans1):
            return "YES"
        x+=1
    return "NO"



x = cal(25,4, 9,20, 1, 1, 10)
print(x)

x = cal(25,4, 12,20, 1, 1, 10)
print(x)

x = cal(100,1, 45,2, 0, 4, 10)
print(x)

x = cal(9,2, 69,2, 4, 2, 7)
print(x)

if "__main__" == __name__:
    n_input = int(input())
    for x in range(n_input):
        ch, ca = map(int, input().split())
        mh, ma = map(int, input().split())
        i, a, h = map(int, input().split())
        result = cal(ch, ca, mh, ma, i, a, h)
        print(result)