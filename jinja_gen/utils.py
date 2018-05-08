import itertools
import os
import numpy as np


def generate_matrix(matrix, output_dir, template_fname, defaults=None,
                    name_keys=None, output_name_key=None, output_dir_key=None):
    name_keys = name_keys or matrix.keys()

    for config in itertools.product(*matrix.values()):
        template_vars = {**(defaults or {}), **dict(zip(matrix.keys(), config))}
        name = '-'.join(map(lambda x: str(template_vars[x]), name_keys))
        output_f = os.path.join(output_dir, name, template_fname)

        if output_name_key:
            template_vars[output_name_key] = name
        if output_dir_key:
            template_vars[output_dir_key] = os.path.dirname(output_f)

        yield output_f, template_vars


def resolve_random_matrix(matrix):
    mod = False
    for key in matrix.keys():
        if not isinstance(matrix[key], list):
            matrix[key] = resolve_randomized_parameter(**matrix[key])
            mod = True
    return matrix, mod


def resolve_randomized_parameter(dist, n_samples, **kwargs):
    """
    
    :param dist: for numpy distributions 
    :param n_samples: number of samples to generate
    :return: 
    """

    if dist == 'uniform':
        low = float(kwargs.get('low', 0.0))
        high = float(kwargs.get('high', 1.0))
        return np.around(
            np.random.uniform(low=low, high=high, size=n_samples),
            decimals=3
        ).tolist()
    if dist == 'uniformint':
        low = int(kwargs.get('low', 0))
        high = int(kwargs.get('high', 1))
        return np.random.randint(low=low, high=high, size=n_samples).tolist()
    elif dist == 'normal':
        loc = float(kwargs.get('loc', 0.0))
        scale = float(kwargs.get('scale', 1.0))
        return np.around(
            np.random.normal(loc=loc, scale=scale, size=n_samples),
            decimals=3
        ).tolist()
    else:
        raise Exception('Unsupported distribution "{}"'.format(dist))

