"""Foobar task # 4.2"""

def main_game(times, time_limit, current_point, current_bunnies, best_bunnies, path, path_graph):
    """Modules to calculate throught the problem with recursion."""
    if current_point == len(times) - 1:
        if len(current_bunnies) > len(best_bunnies) and time_limit >= 0:
            best_bunnies = ''.join(sorted(current_bunnies))
    if len(best_bunnies) == len(times) - 2:
        return best_bunnies

    if len(path) >= len(times)*3:
        return best_bunnies

    for i in range(len(times)):

        if i != current_point and time_limit - times[current_point][i] > -10:
            new_bunnies = current_bunnies
            if (i not in [0, len(times) -1]) and (str(i) not in current_bunnies):
                new_bunnies += str(i)

            new_vector = str(current_point) + '_' + str(i) + '_' + new_bunnies \
                        + '_' + str(time_limit - times[current_point][i])

            if new_vector not in path_graph:
                path_graph.append(new_vector)
                result = main_game(times, time_limit - times[current_point][i], i, \
                                new_bunnies, best_bunnies, path + str(i), path_graph)
                if len(result) > len(best_bunnies):
                    best_bunnies = result

    return best_bunnies

def solution_task(times, time_limit):
    """Solve foobar task # 4.2 "Running with Bunnies"

    Write a function of the form solution(times, time_limit) to calculate
    the most bunnies you can pick up and which bunnies they are, while
    still escaping through the bulkhead before the doors close for good.
    If there are multiple sets of bunnies of the same size, return the set
    of bunnies with the lowest worker IDs (as indexes) in sorted order.
    The bunnies are represented as a sorted list by worker ID, with the
    first bunny being 0. There are at most 5 bunnies, and time_limit is
    a non-negative integer that is at most 999.
    """
    result = list(main_game(times, time_limit, 0, '', [], '', []))
    result.sort()
    return([int(i)-1 for i in result])
