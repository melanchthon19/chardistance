#!/usr/bin/env python3

import numpy as np
import pandas as pd


class Levenshtein():
    def __init__(self, verbose=0):
        self.verbose = verbose
        self.med = 0  # minimum edit distance
        self.m = None
        self.n = None
        self.matrix = None
        self.path = None
        self.highlight = None

    def compute_distance(self, m, n):
        self.m = m.lower()
        self.n = n.lower()
        # calling it matrix even though it is a df for printing purposes
        self.matrix = self.generate_matrix()
        self.path = self.distance_matrix()
        self. highlight = self.highlight_path()
        if self.verbose:
            print(self.matrix)
            print(self.path)
            print('minimum edid distance score:', self.med)

    def generate_matrix(self):
        matrix = np.zeros((len(self.m)+1, len(self.n)+1), dtype=np.int8)
        df = pd.DataFrame(matrix)
        df.index = ['-'] + [char for char in self.m]
        df.columns = ['-'] + [char for char in self.n]
        df.iloc[0:, 0] = np.arange(len(self.m)+1)
        df.iloc[0, 0:] = np.arange(len(self.n)+1)

        if self.verbose:
            print(df)

        return df

    def distance_matrix(self):
        for i in range(1, self.matrix.shape[0]):  # traversing rows
            c1 = self.matrix.index.values[i]
            for j in range(1, self.matrix.shape[1]):  # traversing columns
                c2 = self.matrix.columns[j]

                if c1 == c2:
                    self.matrix.iloc[i, j] = self.matrix.iloc[i-1, j-1]
                else:
                    cost = self.previous_lowest_cost(i, j)
                    self.matrix.iloc[i, j] = self.distance(c1, c2) + cost

        if self.verbose:
            print(self.matrix)

        last_i = self.matrix.shape[0]-1
        last_j = self.matrix.shape[1]-1
        path = self.backtrace(i=last_i, j=last_j, best=[(last_i, last_j)])
        self.med = self.matrix.iloc[last_i, last_j]

        return path[::-1]


    def distance(self, c1, c2):
        if c1 == c2:
            return 0
        else:
            return 1

    def backtrace(self, i, j, best):
        if (i, j) == (0, 0):
            return best

        previous = self.previous_best_path(i, j)
        best.append(previous)
        self.backtrace(previous[0], previous[1], best)

        return best

    def previous_best_path(self, i, j):
        diag = self.matrix.iloc[max([i-1, 0]), max([j-1, 0])]
        left = self.matrix.iloc[i, max([j-1, 0])]
        up = self.matrix.iloc[max([i-1, 0]), j]
        previous_path = {0: (max([i-1, 0]), max([j-1, 0])),
                         1: (i, max([j-1, 0])),
                         2: (max([i-1, 0]), j)}
        paths = [diag, left, up]

        previous = previous_path[paths.index(min(paths))]

        return previous

    def previous_lowest_cost(self, i, j):
        diag = self.matrix.iloc[i-1, j-1]
        left = self.matrix.iloc[i, j-1]
        up = self.matrix.iloc[i-1, j]
        paths = [diag, left, up]

        lowest = min(paths)
        #previous = paths.index(lowest)

        return lowest

    def highlight_path(self):
        m = list(self.m)
        n = list(self.n)

        cost = self.matrix.iloc[0, 0]
        insert = 0
        for step in range(len(self.path[:])):
            i, j = self.path[step]
            if cost == self.matrix.iloc[i, j]:
                continue  # diagonal without change
            else:
                cost = self.matrix.iloc[i, j]  # setting new cost

                # insert
                if i == self.path[step-1][0] and j == self.path[step-1][1]+1:
                    if n[j-1] == ' ':
                        m.insert(i+insert, ' ')
                    else:
                        m.insert(i+insert, '>')
                        n[j-1] = '_'
                    insert += 1

                #delete
                elif i == self.path[step-1][0]+1 and j == self.path[step-1][1]:
                    m[i-1+insert] = f'({m[i-1+insert]})'

                # substitute
                elif i == self.path[step-1][0]+1 and j == self.path[step-1][1]+1:
                    if n[j-1] == ' ':
                        m[i-1+insert] = '//'
                    else:
                        m[i-1+insert] = f'*{m[i-1+insert]}'
                        n[j-1] = '_'
        if self.verbose:
            print("""
            ( ): delete
            *: replace character
            >: add character
            //: add white space""")
            print(m)
            print(n)
            print(f'{"".join(m)} --> {"".join(n)}')

        return "".join(n)


if __name__ == '__main__':
    ld = Levenshtein(verbose=1)
    ld.compute_distance('había una vez', 'avia una vesces')
    
