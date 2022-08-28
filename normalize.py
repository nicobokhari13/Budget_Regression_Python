import pandas as pd

def zScoreNorm(elem, x_fold_mean, x_fold_std, y_fold_mean, y_fold_std, isOutput):
    if isOutput: 
        return (elem - y_fold_mean) / y_fold_std
    else:
        return (elem - x_fold_mean) / x_fold_std



