s = 'aaa'
N = len(s)
temp = []
result = []
s_split = []

def solution(s):
    count_sol = 1
    sum_list = []

    for i in range(len(s)):
        if i == len(s) - 1:
            if count_sol == 1:
                sum_list.append(s[i])
                break
            if count_sol > 1:
                a = str(count_sol) + s[i]
                sum_list.append(a)
                break

        if count_sol == 1:
            if s[i] == s[i+1]:
                count_sol += 1
                continue
            else:
                sum_list.append(s[i])

        if count_sol > 1:
            if s[i] == s[i+1]:
                count_sol += 1
                continue
            else:
                a = str(count_sol) + s[i]
                sum_list.append(a)
    return "".join(sum_list)



if __name__ == "__main__":
    if N == 1:
        print('result : ', len(s))
        exit()
    for i in range(1, int(N/2) + 1):
        for j in enumerate(list(s), start=1):
            temp.append(j[1])
            temp = ["".join(temp)]
            if j[0] % i == 0 or j[0] == N:
                s_split.append(temp[0])
                temp = []
        result.append(len(solution(s_split)))
        s_split = []
    print('result : ', min(result))