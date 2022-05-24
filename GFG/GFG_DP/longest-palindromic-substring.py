from tkinter import N


def LPS(string):
    N = len(string)
    if N < 2:
        return N
    start = 0
    max_len = 0
    for i in range(N):
        low, high = i-1, i+1
        while(high < N and string[high] == string[i]):
            high +=1
        while (low >=0 and string[low] == string[i]):
            low -=1
        while (low >= 0 and high < N and string[low]== string[high]):
            low -=1
            high +=1
        length_of_substr = high-low-1
        if max_len < length_of_substr:
            max_len = length_of_substr
            start = low+1
            print("FOUND ", string[start:start+max_len])
    print("LONGEST ", string[start:start+max_len+1])
LPS("KANAKGKAN")