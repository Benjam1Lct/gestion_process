"""pool_simple_map_application"""

from multiprocessing import Pool

def cube(x):
    return x**3

if __name__ == '__main__':
    p = Pool(processes=4)
    results = p.map(cube, range(1,7))
    print(results) #[1,8,27,64,125,216]


