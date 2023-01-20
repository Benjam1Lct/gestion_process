from multiprocessing import current_process, Process
from os import getpid

def info(title):
    print(title)
    print('module name :', __name__)
    print('parent process :', getpid())
    print('process id :', getpid())

def f(num):
    my_p = current_process() #objet représentant le process
    print('Hello:', num, my_p.pid, my_p._parent_pid, my_p.name)

if __name__ == "__main__":
    info('main program')
    num = 0
    p = Process(target=f, args=(num,))
    p.start()
    print('\nprocess name :', p.name)
    print('process id :', p.pid)
    p.join()
