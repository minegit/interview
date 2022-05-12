def permute(strng, startIndx, endIndx):
    if startIndx == endIndx:
        print(strng)
    else:
        for idx in range(startIndx, endIndx):
            strng[idx], strng[startIndx] = strng[startIndx], strng[idx]
            permute(strng, startIndx+1, endIndx)
            strng[startIndx], strng[idx] = strng[idx], strng[startIndx]
def permute1(strng, ans):
    if len(strng) == 0:
        print(ans)
        return 
    for x in range(len(strng)):
        ch = strng[x]
        rest = strng[0:x]+strng[x+1:]
        permute1(rest, ans+ch)
permute1(list("abc"),"")
permute(list("abc"), 0, 3)