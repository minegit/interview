def solve(payload, pattern, pattern_dict, pay_index=0, pat_index=0):
    len_payload = len(payload)
    len_pattern = len(pattern)
    if len_payload < len_pattern:
        return False
    if pay_index == len_payload and pat_index == len_pattern:
        return True
    if pay_index == len_payload or pat_index == len_pattern:
        return False
    curr_pattern = pattern[pat_index]
    if curr_pattern in pattern_dict:
        s = pattern_dict[curr_pattern]
        lenS = len(s)
        if pay_index + lenS < len_payload:
            ss = payload[pay_index+lenS]
        else:
            ss= payload[pay_index:]
        if ss != s:
            return False
        return solve(payload, pattern, pattern_dict, lenS+pay_index, pat_index+1)
    for payidx in range(1, len_payload-pay_index+1):
        pattern_dict[curr_pattern] = payload[pay_index:pay_index+payidx]
        if solve(payload, pattern, pattern_dict, payidx+pay_index, pat_index+1):
            return True
        pattern_dict.pop(curr_pattern)
    return False


str = "GeeksforGeeks"
pat = "GfG"

# create a dictionary to store mappings between the pattern and string
dict = {}

# check for solution
if solve(str, pat, dict):
    print(dict)
else:
    print("Solution doesn't exist")