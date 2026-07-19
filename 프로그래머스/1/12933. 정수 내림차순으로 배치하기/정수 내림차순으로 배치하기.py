def solution(n):
    num_list = list(str(n))
    num_list.sort()
    num_list.reverse()
    return int("".join(num_list))