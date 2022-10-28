# SuperFastPython.com
# example of parallel imap() with the process pool and a task that does not return a value
from random import random
from time import sleep
from multiprocessing.pool import Pool
 
# task executed in a worker process
def task(identifier):
    # generate a value
    value = random()
    # report a message
    print(f'Task {identifier} executing with {value}', flush=True)
    # block for a moment
    sleep(value)
 
# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    with Pool() as pool:
        # issue tasks to the process pool
        pool.imap(task, range(50))
        # shutdown the process pool
        pool.close()
        # wait for all issued task to complete
        pool.join()
