def solution(s):
    answer = list(map(int, s.split()))
    max_num = max(answer)
    min_num = min(answer)
    return (f"{min_num} {max_num}")