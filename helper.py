# Matrix based operations
from itertools import product
from typing import List, Tuple
read_text_file = lambda path: [x for x in open(path).read().split('\n')]
read_matrix_text_file = lambda path: [[int(y) for y in x] for x in open(path).read().split('\n')]
cartesian_product = lambda vector1, vector2: product(vector1,vector2)


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


# def get_neighbours(text_file:str = None, matrix:List =None):
    
    
    
from collections import namedtuple
class GetNeighbours():
    read_matrix_text_file = lambda path: [[int(y) for y in x] for x in open(path).read().split('\n')]
    check_neighbour = lambda neighbour, matrix: (neighbour[0] >= 0 and neighbour[0] < len(matrix) and neighbour[1] >= 0 and neighbour[1] < len(matrix[0]))
    get_neighbours = lambda coordinate, matrix: tuple(filter(lambda n: GetNeighbours.check_neighbour(n, matrix),[(coordinate[0]-1, coordinate[1]),(coordinate[0]+1, coordinate[1]),(coordinate[0], coordinate[1]-1),(coordinate[0], coordinate[1]+1)])) 
    @staticmethod
    def generate_neighbours(path: str):
        matrix =  GetNeighbours.read_matrix_text_file(path)
        yield ([GetNeighbours.get_neighbours((row, column), matrix) for column in row] for row in matrix)


from cProfile import runctx
def measure_performance(func):
    def wrapper(*args, **kwargs):
        nonlocal func    
        return runctx('result = func(*args, **kwargs)', globals(), locals())
    return wrapper



reverse_dictionary = lambda dictionary: {value: key for key, value in dictionary.items()}