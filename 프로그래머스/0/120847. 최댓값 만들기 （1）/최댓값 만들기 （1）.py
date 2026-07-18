def solution(numbers):
    answer = 0
    max = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer = numbers[i] * numbers[j]
            if answer > max:
                max = answer
    return max