import numpy as np
def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(lst).reshape(3, 3)

    result = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    for axis in [0, 1, None]:
        if axis is not None:
            result['mean'].append(np.mean(matrix, axis=axis).tolist())
            result['variance'].append(np.var(matrix, axis=axis).tolist())
            result['standard deviation'].append(np.std(matrix, axis=axis).tolist())
            result['max'].append(np.max(matrix, axis=axis).tolist())
            result['min'].append(np.min(matrix, axis=axis).tolist())
            result['sum'].append(np.sum(matrix, axis=axis).tolist())
        else:
            result['mean'].append(float(np.mean(matrix)))
            result['variance'].append(float(np.var(matrix)))
            result['standard deviation'].append(float(np.std(matrix)))
            result['max'].append(int(np.max(matrix)))
            result['min'].append(int(np.min(matrix)))
            result['sum'].append(int(np.sum(matrix)))

    return result