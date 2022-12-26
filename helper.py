import pandas as pd

def zScoreNorm(elem, x_fold_mean, x_fold_std, y_fold_mean, y_fold_std, isOutput):
    if isOutput: 
        return (elem - y_fold_mean) / y_fold_std
    else:
        return (elem - x_fold_mean) / x_fold_std

def RMSE(x_holdout, y_holdout, weights, intercept):
    #let n = # terms in polynomial = len(weights) + 1 for intercept
    #let m = # of instances in holdout 
    #let h = array with m h(x), where h is the polynomial with the weights + intercept
    
    return 0


