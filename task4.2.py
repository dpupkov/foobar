"""Foobar task # 4.2
"""

def main_game(times, time_limit, current_point, current_bunnies, best_bunnies, vector_dict):
    """Function to solve the problem with recursion."""

    # Checking if I'm at the end and we have new best result
    if current_point == len(times) - 1 and len(current_bunnies) > len(best_bunnies):
        if time_limit >= 0:
            best_bunnies = ''.join(sorted(current_bunnies))

    # Checking if I collected all the bunnies
    if len(best_bunnies) == len(times) - 2:
        return best_bunnies

    for i in range(len(times)):
        if i != current_point:
            next_bunnies = current_bunnies

            # If we're in bunnies and we didn't have that one,
            # then adding to the next_bunnies hop list
            if (i not in [0, len(times) -1]) and (str(i) not in current_bunnies):
                next_bunnies += str(i)
                next_bunnies = ''.join(sorted(next_bunnies))

            # Composing new vector and saving in dictionary
            new_vector = str(current_point) + '_' + str(i) + '_' + next_bunnies
            next_time_limit = time_limit - times[current_point][i]

            if new_vector in vector_dict:
                if next_time_limit > vector_dict[new_vector]:
                    vector_dict[new_vector] = next_time_limit
                    result = main_game(times, next_time_limit, i, \
                                    next_bunnies, best_bunnies, vector_dict)
                    if len(result) > len(best_bunnies):
                        best_bunnies = result
            else:
                vector_dict[new_vector] = next_time_limit
                result = main_game(times, next_time_limit, i, \
                                    next_bunnies, best_bunnies, vector_dict)
                if len(result) > len(best_bunnies):
                    best_bunnies = result

    return best_bunnies

def solution(times, time_limit):
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

    # Shaving a little bit on back-and-forth recursion if any
    for i, _ in enumerate(times):
        for j in range(0,i):
            if times[i][j] + times[j][i] < 0:
                times[i][j] = -999
                times[j][i] = -999

    # Sorting the result and returning as a list
    result = list(main_game(times, time_limit, 0, '', [], {}))
    result.sort()
    return [int(i)-1 for i in result]
