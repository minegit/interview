def cal(x):
    total_len = len(x)
    zero_len = 0
    one_len = 0
    for i in x:
        one_len = one_len+int(i)
    zero_len = total_len - one_len
    if zero_len != one_len:
        return min(zero_len, one_len)
    return one_len-1

if __name__ == "__main__":
    n_input = int(input())
    for x in range(n_input):
        input_str = str(input())
        print(cal(input_str))

    for i in range(20):
        temp = format(i, "b")
        ans = cal(temp)
        print(i,"----------->",temp,"------->", ans)