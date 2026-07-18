def solution(num_list):
    jjak = 0
    hol = 0
    for i in range(0, len(num_list), 1):
        if num_list[i] % 2 == 0:
            jjak+=1
        else:
            hol+=1
    return [jjak, hol]