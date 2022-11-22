# Matrix based operations
from itertools import product


read_matrix_text_file = lambda path: [[int(y) for y in x] for x in open(path).read().split('\n')]
cartesian_product = lambda vector1, vector2: set(product(vector1,vector2))

check_neighbour = lambda neighbour, matrix: (neighbour[0] >= 0 and neighbour[0] < len(matrix) and neighbour[1] >= 0 and neighbour[1] < len(matrix[0]))
get_neighbours = lambda i, matrix: tuple(filter(lambda n: check_neighbour(n, matrix),[(i[0]-1, i[1]),(i[0]+1, i[1]),(i[0], i[1]-1),(i[0], i[1]+1)]))

from time import perf_counter, time
def timeit(func):
    def timeit_wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} took {total_time:.6f} seconds')
        return result
    return timeit_wrapper

