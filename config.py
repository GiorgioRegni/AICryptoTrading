# Which colums to use as input for the nerual network
columns = ['Close','Volume','Low','High']

# Which currency pair are we interested in predicting
pair = 'BTC_ETH' # or 'USDT_BTC'

CONFIG = {
    'pair': pair,
    'period': 300,
    'input_size': 30,
    'output_size': 12,
    'lstm_hidden_size': 50,
    'columns' : columns,
    'csv_src_file' : pair,
    'name': 'lstm',
    'folder': {
        'data': 'data/',
        'weights': 'weights/',
        }
}

CONFIG['filename'] = pair+'_'+CONFIG['name']+"_i%d_o%d_" %(CONFIG['input_size'],CONFIG['output_size']) + '_'.join(columns)


