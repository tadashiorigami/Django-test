import numpy as np

def get_lr_model(x_array, y_array, n):
    
    x_np_array = np.array(x_array)
    y_np_array = np.array(y_array)
    coefs = np.polyfit(x_np_array, y_np_array, n)
    modelPredictions = np.polyval(coefs, x_np_array)
    absError = modelPredictions - y_np_array
    SE = np.square(absError)
    MSE = np.mean(SE)
    RMSE = np.sqrt(MSE)
    return coefs, RMSE

def round_number(number, valid_dec):
    if number >= 10**valid_dec:
        return round(number)
    elif number < 10**valid_dec:
        return round(number, int(-np.ceil(np.log10(abs(number)) - valid_dec)))

def regression_xy(coefs, xmin, xmax):
    offset = 0.1
    interval = (xmax - xmin)
    start = xmin - interval*offset
    finish = xmax + interval*offset
    x_list = np.linspace(start, finish, 200)
    y_list = np.polyval(coefs, x_list)
        
    return x_list, y_list