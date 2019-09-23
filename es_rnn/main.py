import sys
sys.path.append('/home/peter/forecasts/ESRNN-GPU')
print(sys.path)
import pandas as pd
from torch.utils.data import DataLoader
from es_rnn.data_loading import create_datasets, SeriesDataset
from es_rnn.config import get_config
from es_rnn.trainer import ESRNNTrainer
from es_rnn.model import ESRNN
import time



print('loading config')
config = get_config('Quarterly')

print('loading data')
info = pd.read_csv('../cadre_data/info.csv')

train_path = '../cadre_data/Train/%s-train.csv' % (config['variable'])
test_path = '../cadre_data/Test/%s-test.csv' % (config['variable'])

print(config['output_size'])
train, val, test = create_datasets(train_path, test_path, config['output_size'])

dataset = SeriesDataset(train, val, test, info, config['variable'], config['chop_val'], config['device'])
print(dataset)
dataloader = DataLoader(dataset, batch_size=config['batch_size'], shuffle=True)

run_id = str(int(time.time()))
model = ESRNN(num_series=len(dataset), config=config)
tr = ESRNNTrainer(model, dataloader, run_id, config, ohe_headers=dataset.dataInfoCatHeaders)
tr.train_epochs()
