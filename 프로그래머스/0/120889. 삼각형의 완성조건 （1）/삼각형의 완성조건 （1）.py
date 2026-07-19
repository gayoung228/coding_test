def solution(sides):
    max_value = max(sides)
    other = sum(sides) - max_value

    if other > max_value:
        return 1
    else:
        return 2