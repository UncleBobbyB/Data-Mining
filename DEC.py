import sklearn
from sklearn import decomposition
import pandas as pd
import numpy as np
from numpy import matmul
import matplotlib
from matplotlib import pyplot as plt

def _for_single_file(fileurl):
    '''
    Processes a single file.
    Args:
        fileurl: file url

    Returns:
        df: parsed data matrix, numpy.DataFrame
    '''
    df = pd.read_csv(fileurl)
    to_drop = []
    for i in range(3):
        to_drop.append(df.columns.values[i])

    df.drop(to_drop, inplace=True, axis=1)
    times = [i for i in range(1, 97)]
    rename_mapping = {}
    for i, name in enumerate(df.columns.values):
        rename_mapping[name] = times[i]

    df.rename(rename_mapping, inplace=True, axis=1)

    return df


def for_all_files(fileurls):
    '''
    Processes and parses  all files.

    Args:
        fileurls: file urls, List
Returns:
        df: parsed data matrices attached together, numpy.DataFrame
    '''
    headers = [str(i) for i in range(1, 97)]
    # df = pd.DataFrame(columns=headers)
    df = pd.DataFrame()
    for fileurl in fileurls:
        df = df.append(_for_single_file(fileurl))

    return df


