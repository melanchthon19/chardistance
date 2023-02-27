#!/usr/bin/env python3

import re
 
with open('esp-phonemic.txt', 'r') as file:
    text = file.read()
    text = re.sub(r' ', '', text)
    text = re.sub(r'\.', '', text)
    text = re.sub(r'#', ' ', text)
    text = re.sub(r'ˈ', '', text)
    text = re.sub(r'\|{4}', '\n', text)
    text = re.sub(r'\|+', ', ', text)
print(text)
with open('esp-phonemic-reformat.txt', 'w') as file:
    file.write(text)