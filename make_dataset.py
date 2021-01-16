# Добавление всех отобранных жестов в единный файл

import pandas as pd
import os
import numpy as np


gestures = ['hello', 'money', 'bye']
dataset = []
max_len = 1134
filler = [-1.0]*63

def join_all_gesture():
    with open('dataset/raw_data.txt', 'w') as out:
        for i, gest in enumerate(gestures):
            for folder in os.listdir(f'dataset/{gest}'):
                f = open(f'dataset/{gest}/{folder}/join/{folder}_.txt')
                row = list(map(float, f.readline().split()))
                length = len(row)
                diff = (max_len - length) // 63

                front = True
                for _ in range(diff):
                    if front:
                        row = list(np.insert(row, 0, filler))
                    else:
                        row.extend(filler)
                    front = not front

                print(*row, file=out)




join_all_gesture()


