from src.data_collection.api import CryptoAPI

def test_nonegative_btc_value():
    api = CryptoAPI()
    bitcoin = api.get_btc()
    assert bitcoin['high'][0] > 0