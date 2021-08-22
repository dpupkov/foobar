import random

def solution(start, length):
    result = 0
    for s in range(length):
        for worker in range(start + s*length, start + (s+1)*length - s):
            if worker > 2000000000:
                return result
#            print(worker)
            result = result^worker
    
    return result

cases = [(0, 3, 2),
         (17, 4, 14),
         (2000000000, 3, 1),
         (random.randint(0,2000), random.randint(1,5), 0)
        ]

for c1, c2, test_result in cases:
#    if solution(c1, c2) != test_result:
    print(c1, c2)
    print(solution(c1, c2), '\n')


