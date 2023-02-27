#!/usr/bin/env python3

import re
import sys
import string
import argparse
import pandas as pd
from levenshtein import Levenshtein


def read_data(file):
    df = pd.read_csv(file)
    data = {}
    data['esp'] = df['español']
    data['fra'] = df['francés']
    data['cat'] = df['catalán']
    rows = len(df.index)
    return data, rows

def preprocess_ortographic(data):
    for language in data:
        for i in range(len(data[language])):
            # remove punctuation
            data[language][i] = re.sub(rf'[{string.punctuation}\'’]', '', data[language][i])
            # simlplify vowels
            vowels = {'á':'a', 'à': 'a', 'â': 'a',
                      'é': 'e', 'è': 'e', 'ê': 'e',
                      'í': 'i', 'ì': 'i', 'î': 'i',
                      'ó': 'o', 'ò': 'o', 'ô': 'o',
                      'ú': 'u', 'ù': 'u', 'û': 'u'}
            rvowels = re.compile(rf'({list(vowels.keys())})')
            data[language][i] = re.sub(rvowels, lambda m: vowels.get(m.group(), m.group()), data[language][i])

    return data

def preprocess_phonemic(data):
    for language in data:
        for i in range(len(data[language])):
            data[language][i] = re.sub(rf'[{string.punctuation}\'’‿]', '', data[language][i])
    
    return data

def compare_languages(data, rows, index=0, verbose=False):
    ld = Levenshtein()
    espfra = []
    espcat = []
    fracat = []
    for i in range(rows):
        if index: i = index

        ld.compute_distance(data['esp'][i], data['fra'][i])
        espfra.append((ld.med, ld.highlight))
    
        ld.compute_distance(data['esp'][i], data['cat'][i])
        espcat.append((ld.med, ld.highlight))

        ld.compute_distance(data['fra'][i], data['cat'][i])
        fracat.append((ld.med, ld.highlight))

        if verbose:
            print('\nrow:', i)
            print('\nesp fra:\n', espfra[-1])
            print('\nesp cat:\n', espcat[-1])
            print('\nfra cat:\n', fracat[-1])

        if index: break

    return espfra, espcat, fracat

def med_avg(language, rows):
    return round(sum([med[0] for med in language])/rows, 2)

def summary(espfra, espcat, fracat, rows):
    print('\nsummary:\n')
    print('esp fra', med_avg(espfra, rows))
    print('esp cat', med_avg(espcat, rows))
    print('fra cat', med_avg(fracat, rows))

def main(file, index=0, preprocess=False, verbose=False):
    print('setup:\n', 'file:', file, 'index', index, 'preprocess:', preprocess, 'verbose:', verbose)
    data, rows = read_data(file)
    if preprocess == 'ortographic':
        data = preprocess_ortographic(data)
    if preprocess == 'phonemic':
        data = preprocess_phonemic(data)
    espfra, espcat, fracat = compare_languages(data, rows, index, verbose)
    summary(espfra, espcat, fracat, rows)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='file that stores sentences')
    parser.add_argument('-i', '--index', type=int, default=0, help='analyse sentence at given index only')
    parser.add_argument('-p', '--preprocess', default=False, choices=['ortographic', 'phonemic'], help='preprocess data ortographically/phonemically before computing distance')
    parser.add_argument('-v', '--verbose', action='store_true', help='print each minimum edit distance')
    args = parser.parse_args()

    main(args.file, args.index, args.preprocess, args.verbose)