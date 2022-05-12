def check_if_sorted(Q, N):  # Rough code !! Not syntactically correct.
    expected_element = 1
    st = []
    finalQ = []
    while(not Q.empty()):
        front = Q.queue(0)
        Q.get()
        if front == expected_element:
            expected +=1
        else:
            if len(st) == 0:
                st.push(front)
            elif len(st) > 0 and front < st.peek():
                st.push(front)
            else:
                return False
        while len(st) != 0 and st.peek() == expected_element:
            st.pop()
            expected_element +=1
    if expected_element -1 == N and len(st) == 0:
        return True
    return False

            
