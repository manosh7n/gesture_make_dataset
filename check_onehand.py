# Проверить только одна рука записана(для жестов с одной рукой)

import os

dir = 'dataset/bye'

list_of_gest = sorted(os.listdir(dir))
for folder in list_of_gest:
    for file in os.listdir(os.path.join(dir, folder)):
        if file.endswith(".txt"):
            txt_file = os.path.join(f'{dir}/{folder}', file)
            f = open(txt_file, 'r')
            try:
                print(f.readlines()[1])
                print(txt_file)
            except:
                pass

