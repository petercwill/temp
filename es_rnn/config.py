from math import sqrt

import torch


def get_config(interval):
    config = {
        'prod': True,
        'device': ("cuda" if torch.cuda.is_available() else "cpu"),
        'percentile': 50,
        'training_percentile': 45,
        'add_nl_layer': True,
        'rnn_cell_type': 'LSTM',
        'learning_rate': 1e-3,
        'learning_rates': ((10, 1e-4)),
        'num_of_train_epochs': 20,
        'num_of_categories': 2,  # in data provided
        'batch_size': 16,
        'gradient_clipping': 20,
        'c_state_penalty': 0,
        'min_learning_rate': 0.0001,
        'lr_ratio': sqrt(10),
        'lr_tolerance_multip': 1.005,
        'min_epochs_before_changing_lrate': 2,
        'print_train_batch_every': 5,
        'print_output_stats': 3,
        'lr_anneal_rate': 0.5,
        'lr_anneal_step': 5
    }

    if interval == 'Quarterly':
        config.update({
            'chop_val': 60,
            'variable': "Quarterly",
            'dilations': ((1, 2), (4, 8)),
            'state_hsize': 40,
            'seasonality': 4,
            'input_size': 4,
            'output_size': 8,
            'level_variability_penalty': 80
        })
    elif interval == 'Monthly':
        config.update({
            #     RUNTIME PARAMETERS
            'chop_val': 72,
            'variable': "Monthly",
            'dilations': ((1, 3), (6, 12)),
            'state_hsize': 50,
            'seasonality': 12,
            'input_size': 12,
            'output_size': 18,
            'level_variability_penalty': 50
        })
    elif interval == 'Daily':
        config.update({
            #     RUNTIME PARAMETERS
            'chop_val': 200,
            'variable': "Daily",
            'dilations': ((1, 7), (14, 28)),
            'state_hsize': 50,
            'seasonality': 7,
            'input_size': 7,
            'output_size': 14,
            'level_variability_penalty': 50
        })
    elif interval == 'Yearly':

        config.update({
            #     RUNTIME PARAMETERS
            'chop_val': 25,
            'variable': "Yearly",
            'dilations': ((1, 2), (2, 6)),
            'state_hsize': 30,
            'seasonality': 1,
            'input_size': 4,
            'output_size': 6,
            'level_variability_penalty': 0
        })
    else:
        print("I don't have that config. :(")

    config['input_size_i'] = config['input_size']
    config['output_size_i'] = config['output_size']
    config['tau'] = config['percentile'] / 100
    config['training_tau'] = config['training_percentile'] / 100

    if not config['prod']:
        config['batch_size'] = 10
        config['num_of_train_epochs'] = 15

    return config
