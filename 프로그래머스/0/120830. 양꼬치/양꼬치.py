def solution(n, k):
    sale = 0
    if n>=10:
        sale=n//10
    answer = (12000 * n) + (2000 * k) - (2000*sale)
    return answer