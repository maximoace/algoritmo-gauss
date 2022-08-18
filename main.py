from random import gauss
from modules.gauss import gauss_elimination

if __name__ == '__main__':
    mtx = [[2,3,4],[5,6,7],[8,9,10]]
    print(gauss_elimination(mtx))