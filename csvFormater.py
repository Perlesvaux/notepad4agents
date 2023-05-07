#!/usr/bin/env python3
import csv

with open('./output.csv', 'r') as fp:
    reader = csv.reader(fp)
    contents = [x for x in reader]

# print(contents)

# for i, val in enumerate(contents):
#     print(val[2], val[4])

#each = {val[4]:val[2] for i, val in enumerate(contents)}

#NK, Spirit Airlines, spirit.com, 18004337300
each = [(val[4].lower(), val[2].lower(), val[-2].lower(), val[-1].lower()) for i, val in enumerate(contents)]


for i, val in enumerate(each):
    if each[i][-1] != '':
        print(val)


"""
 +\w+(?= *$)     matches last word of string
const PROP    = raw_text.match(PROP_rgx)[0].replace(/.*PROPERTY\n\n/i, '').trim()

"""





