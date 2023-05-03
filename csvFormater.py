#!/usr/bin/env python3
import csv

with open('./output.csv', 'r') as fp:
    reader = csv.reader(fp)
    contents = [x for x in reader]

# print(contents)

# for i, val in enumerate(contents):
#     print(val[2], val[4])

#each = {val[4]:val[2] for i, val in enumerate(contents)}

each = [(val[4], val[2], val[-1]) for i, val in enumerate(contents)]

print(each)







