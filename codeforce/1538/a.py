def solve():
    arr_size = int(input())
    r_index = 0
    arr = list(map(int, input().split()))
    min_item = arr[0]
    max_item = min_item
    max_index = 1
    min_index = 1
    for item in arr:
        r_index +=1
        if item > max_item:
            max_index  = r_index
            max_item = item
        
        if item < min_item:
            min_index = r_index
            min_item = item
    min_index_r = arr_size - min_index +1
    max_index_r = arr_size - max_index +1

    first_remove = min(min_index_r,max_index_r, min_index, max_index)
    sum_result = first_remove
    if max_index_r == first_remove or max_index == first_remove:
        if max_index_r == first_remove:
            min_index_r -= first_remove
        elif max_index == first_remove:
                min_index -= first_remove
        sum_result += min(min_index, min_index_r)
        return(sum_result)
    else:
        if min_index_r == first_remove:
            max_index_r -= first_remove
        elif min_index == first_remove:
            max_index -= first_remove
        sum_result += min(max_index, max_index_r)
        return (sum_result)
if __name__ == "__main__":
    ninput  = int(input())
    for x in range(ninput):
        ans = solve()
        print(ans)

