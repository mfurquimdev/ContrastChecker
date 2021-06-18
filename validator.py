#!/bin/env python

from itertools import permutations
from pprint import pprint
import requests

all_colors = ['242933', '2E3440', '3B4252', '434C5E', '4C566A', 'BF616A', 'D08770', 'EBCB8B', 'A3BE8C', '8FBCBB', '88C0D0', '81A1C1', '5E81AC', 'B48EAD', 'D8DEE9', 'E5E9F0', 'ECEFF4']

for i in list(permutations(all_colors, 2)):
    fg = i[0]
    bg = i[1]
    url = f'https://webaim.org/resources/contrastchecker/?fcolor={fg}&bcolor={bg}&api'
    print(f'Making GET request on {url}')
    response = requests.get(url)
    pprint(response.json())

for i in list(permutations(all_colors, 3)):
    fg = i[0]
    bg = i[1]
    link = i[2]


#curl 'https://webaim.org/resources/contrastchecker/?fcolor={fg}&bcolor={bg}&api'
#curl 'https://webaim.org/resources/linkcontrastchecker/?fcolor={fg}&bcolor={bg}&lcolor={link}&api'
