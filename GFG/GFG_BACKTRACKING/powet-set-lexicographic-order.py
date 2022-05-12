def permute(string, lenString, index = -1, curr = ""):
    if index == lenString:
        return 
    if(len(curr) > 0):
        print(curr, end=",")
    for idx in range(index+1, lenString):
        curr += string[idx]
        permute(string, lenString, idx, curr)
        curr = curr[:len(curr)-1]


def solve(string):
    string = ''.join(sorted(string))
    permute(string, len(string))

solve("dabc")



sensehq
