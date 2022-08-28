import pandas as pd

def zScoreNorm(x, x_fold_mean, x_fold_std, y_fold_mean, y_fold_std, isOutput):
    if isOutput: 
        return (x - y_fold_mean) / y_fold_mean
    else:
        return (x - x_fold_mean) / x_fold_std



