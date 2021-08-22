import itertools

def solution(l):
    answer = 0
    for l in range(1, len(c)+1):
        for i in itertools.permutations(c, l):
            a = int(''.join(str(e) for e in i)) 
            if (a % 3 == 0) and a > answer:
                answer = a
    return(answer)



cases = [[3, 1, 4, 1],
         [3, 1, 4, 1, 5, 9]
        ]
for c in cases:
    print('c: ',c)
    print(solution(c))

