from marzano.marzano import powerlaw
from random import randint

grades = [1, 2]
for _ in range(1, 20):
    grades.append(randint(grades[_ - 1], max(grades[_] + 1, 4)))
    print(f"{grades}\t{powerlaw(grades)}")
