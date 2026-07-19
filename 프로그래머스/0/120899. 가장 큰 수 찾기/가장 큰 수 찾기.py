def solution(array):
    for i in range(len(array)):
        if array[i] == max(array):
            answer = [max(array), i]
    return answer