import random
from random_words import RandomWords
import time

random.seed(1)

int_list = []
float_list = []
str_list = []

w = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(w.random_word())

# print("Int List:", int_list)
# print("Float List:", float_list)
# print("String List:", str_list)


print('-------task2---------------')
def bubble_sort(my_list, n):
    x = 0
    time_list = []
    while x < n:
        cur_time = time.time()
        length = len(my_list)
        for i in range(length):
            swapped = False
            for j in range(0, length - i - 1):
                if my_list[j] > my_list[j + 1]:
                   my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                   swapped = True
            if not swapped:
                break
        time_list.append(time.time() - cur_time)
        x += 1

    print("AVG time of execution: ", sum(time_list) / len(time_list))


bubble_sort(float_list, 5)
