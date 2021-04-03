import requests
import pandas as pd
import json

class CryptoAPI:
    def get_pair(self, symbol, granularity=86400):
        #code example from: https://www.cryptodatadownload.com/blog/how-to-download-coinbase-price-data.html
        url = f'https://api.pro.coinbase.com/products/{symbol}/candles?granularity={granularity}'
        response = requests.get(url)
        if response.status_code == 200: 
            data = pd.DataFrame(json.loads(response.text), columns=['unix', 'low', 'high', 'open', 'close', 'volume'])
            data['date'] = pd.to_datetime(data['unix'], unit='s') 
            data['vol_fiat'] = data['volume'] * data['close'] 
            return(data)

    def get_btc(self, granularity=86400):
        if granularity not in [60, 300, 900, 3600, 21600, 86400]:
            raise ValueError('granularity should be one of: 60, 300, 900, 3600, 21600, 86400')
        bitcoin = self.get_pair(symbol='BTC-USD', granularity=granularity)
        return(bitcoin)
