import numpy as np
import pandas as pd
from math import *
from copy import deepcopy

def _for_single_file(filename):
    df = pd.read_csv('./data' + filename, error_bad_lines=False)

    # drop irrelevant cols
    to_drop = ['4', '50#']
    df.drop(to_drop, inplace=True, axis=1)

    # drop AYJ
    df.drop(['AYJ'], inplace=True, axis=1)

    # rename cols
    rename_mapping_cands = ['point_id', 'taxi_id', 'time', 'x', 'y', 'OSM_st', 'OSM_ed', 'speed', 'theta', 'status']
    rename_mapping = {}
    for i, name in enumerate(df.columns.values):
        rename_mapping[name] = rename_mapping_cands[i]

    df.rename(rename_mapping, axis=1, inplace=True)

    # modifying data types
    df.time = df.time.astype('str')

    # remove unreal points
    limits = {'long': [39.768522, 40.028584], 'lat': [116.218923, 116.550119]}
    df = df[(df.x >= limits['lat'][0]) & (df.x <= limits['lat'][1])]
    df = df[(df.y >= limits['long'][0]) & (df.y <= limits['long'][1])]

    # remove duplicate timing points
    df.drop_duplicates(['taxi_id', 'time'], inplace=True)

