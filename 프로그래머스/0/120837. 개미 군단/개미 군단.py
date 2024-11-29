def solution(hp):
    answer = 0
    d_5 = hp // 5
    hp -= d_5 * 5
    d_3 = hp // 3
    hp -= d_3 * 3
    d_1 = hp // 1
    answer = d_5 + d_3 + d_1
    return answer