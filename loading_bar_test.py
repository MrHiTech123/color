from time import sleep
from random import random



def rand_sleep() -> None:
    sleep(random())


for i in range(100):
    print(i, flush=True)
    rand_sleep()
