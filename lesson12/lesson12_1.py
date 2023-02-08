#1.factorial

import concurrent.futures
import time

dates = [2, 4, 5, 6]


def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


if __name__ == '__main__':
    time_line = {}

    # wo anything
    started_at = time.time()
    print([factorial(i) for i in dates])
    print(f'Time: {time.time() - started_at}')
    t1 = (time.time() - started_at)
    time_line["1- wo anything"] = t1
    print()

    # ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(12) as executor:
        started_at2 = time.time()
        future_dat = {executor.submit(factorial, dat): dat for dat in dates}
        for elem in concurrent.futures.as_completed(future_dat):
            print((elem.result()))
        print(f'Time: {time.time() - started_at2}')
        t2 = (time.time() - started_at2)
        time_line["2-ThreadPoolExecutor"] = t2
        print()

    # ProcessPoolExecutor
    with concurrent.futures.ProcessPoolExecutor() as executor3:
        started_at3 = time.time()
        future_dat3 = {executor3.submit(factorial, dat): dat for dat in dates}
        for elem in concurrent.futures.as_completed(future_dat3):
            print(elem.result())
        print(f'Time: {time.time() - started_at3}')
        t3 = (time.time() - started_at3)
        time_line["3-ProcessPoolExecutor"] = t3
        print()
        
    # best result 
    best_res = min(time_line.values())
    for key in time_line.keys():
        if time_line.get(key) == best_res:
            print("the fastest method is:" , key)
