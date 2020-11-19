# Tuple: ordered, inmutable, allows duplicate elements
import timeit
print(timeit.timeit(stnt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stnt="(0, 1, 2, 3, 4, 5)", number=1000000))