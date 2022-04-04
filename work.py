#! /usr/bin/env python
import math
while True:
    s = input("Enter a triple: ")
    if s == "q":
        break
    best_case, most_likely_case, worst_case = sorted(map(float, s.split()))
    expected_case = int(math.ceil((best_case + 3*most_likely_case + 2*worst_case) / 6.0))
    print(expected_case)
