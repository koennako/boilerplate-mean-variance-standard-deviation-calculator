import numpy as np

def calculate(input_list):
    if(len(input_list) != 9):
        raise ValueError("List must contain nine numbers.")
    
    A = np.array(input_list)
    A = A.reshape(3,3)

    B = {
        'mean': [A.mean(axis = 0).tolist(), A.mean(axis = 1).tolist(), float(A.mean())],
        'variance': [A.var(axis = 0).tolist(), A.var(axis = 1).tolist(), A.var().tolist()],
        'standard deviation': [A.std(axis = 0).tolist(), A.std(axis = 1).tolist(), A.std().tolist()],
        'max': [A.max(axis = 0).tolist(), A.max(axis = 1).tolist(), A.max().tolist()],
        'min': [A.min(axis = 0).tolist(), A.min(axis = 1).tolist(), A.min().tolist()],
        'sum': [A.sum(axis = 0).tolist(), A.sum(axis = 1).tolist(), A.sum().tolist()]
    }
    return B