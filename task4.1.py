import copy

def main_game(entrances, exits, path, corridors_indexes, current_count, best_result):

# running down by list of corridors
    for cr in corridors_indexes:
        
# running down by each corridor array
        for i in [l for l in range(len(path)) if (l not in entrances)]:
            
# spare capacity? let's run down..
            if path[cr][i] != 0:
# checking if we can add bunny into this corridor from homies or from another corridor:
                for origin in  entrances + corridors_indexes:
                    if path[origin][cr] != 0:
# if success then increasing result
                        if origin in entrances:
                            current_bunnies = min (path[cr][i], path[origin][cr])
                        else:
                            current_bunnies = 0
# going deep into recursion
                        p1 = copy.deepcopy(path)
                        p1[cr][i] = 0
                        p1[origin][cr] = 0
                        new_count = main_game(entrances, exits, p1, corridors_indexes, current_count + current_bunnies, best_result)
                        if new_count > best_result:
                            best_result = new_count
# getting out of recurrsion:
    if current_count > best_result:
        best_result = current_count
    return(best_result)

def solution(entrances, exits, path):

    corridors_indexes = [i for i in range(len(path)) if (i not in entrances) and (i not in exits)]
    result = main_game(entrances, exits, path, corridors_indexes, 0, 0)
    return(result)


r = solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])

print(r)

r = solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])

print(r)

