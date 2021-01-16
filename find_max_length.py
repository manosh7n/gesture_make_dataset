# Поиск максимальной длины жеста, для выравнивания
# остальных жестов до этого размера

import os
import numpy as np

gestures = ['money', 'bye', 'hello']
full_length = []

def join_points():
    for gest in gestures:
        for folder in sorted(os.listdir(f'dataset/{gest}')):
            try:
                os.mkdir(f'dataset/{gest}/{folder}/join')
            except:
                pass
            with open(f'dataset/{gest}/{folder}/join/{folder}_.txt', 'w') as out:
                for file in sorted(os.listdir(f'dataset/{gest}/{folder}')):
                    if file.endswith('.txt'):
                        txt_file = f'dataset/{gest}/{folder}/{file}'
                        f = open(txt_file)
                        data = list(map(float, f.readline().split()))
                        print(*data, file=out, end=' ')
                        f.close()
            with open(f'dataset/{gest}/{folder}/join/{folder}_.txt', 'r') as fin:
                full_length.append((len(fin.readline().split()), (gest, folder)))


def find_max_length():
    max_ = 0
    max_ind_ = 0
    for i in full_length:
        if i[0] > max_:
            max_ = i[0]
            max_ind_ = i[1]
    return max_, max_ind_


join_points()
max_, max_ind_ = find_max_length()
print(f'Length: {max_}/{max_/63}, Example: {max_ind_}')