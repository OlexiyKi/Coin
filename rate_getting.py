import requests
from sqlalchemy.orm import Session
from sqlalchemy import select
import alch_engine
import model_db
import datetime



def get_data():
    rec_ex = requests.get('https://api.coingecko.com/api/v3/exchange_rates').json()
    #rec_ex = {'rates': {'btc': {'name': 'Bitcoin', 'unit': 'BTC', 'value': 1.0, 'type': 'crypto'}, 'eth': {'name': 'Ether', 'unit': 'ETH', 'value': 15.436, 'type': 'crypto'}, 'ltc': {'name': 'Litecoin', 'unit': 'LTC', 'value': 329.16, 'type': 'crypto'}, 'bch': {'name': 'Bitcoin Cash', 'unit': 'BCH', 'value': 206.695, 'type': 'crypto'}, 'bnb': {'name': 'Binance Coin', 'unit': 'BNB', 'value': 82.994, 'type': 'crypto'}, 'eos': {'name': 'EOS', 'unit': 'EOS', 'value': 24199.864, 'type': 'crypto'}, 'xrp': {'name': 'XRP', 'unit': 'XRP', 'value': 71551.947, 'type': 'crypto'}, 'xlm': {'name': 'Lumens', 'unit': 'XLM', 'value': 318926.793, 'type': 'crypto'}, 'link': {'name': 'Chainlink', 'unit': 'LINK', 'value': 3895.038, 'type': 'crypto'}, 'dot': {'name': 'Polkadot', 'unit': 'DOT', 'value': 4292.527, 'type': 'crypto'}, 'yfi': {'name': 'Yearn.finance', 'unit': 'YFI', 'value': 3.133, 'type': 'crypto'}, 'usd': {'name': 'US Dollar', 'unit': '$', 'value': 28445.908, 'type': 'fiat'}, 'aed': {'name': 'United Arab Emirates Dirham', 'unit': 'DH', 'value': 104472.86, 'type': 'fiat'}, 'ars': {'name': 'Argentine Peso', 'unit': '$', 'value': 5738504.281, 'type': 'fiat'}, 'aud': {'name': 'Australian Dollar', 'unit': 'A$', 'value': 42236.256, 'type': 'fiat'}, 'bdt': {'name': 'Bangladeshi Taka', 'unit': '৳', 'value': 3008054.376, 'type': 'fiat'}, 'bhd': {'name': 'Bahraini Dinar', 'unit': 'BD', 'value': 10580.967, 'type': 'fiat'}, 'bmd': {'name': 'Bermudian Dollar', 'unit': '$', 'value': 28445.908, 'type': 'fiat'}, 'brl': {'name': 'Brazil Real', 'unit': 'R$', 'value': 150177.327, 'type': 'fiat'}, 'cad': {'name': 'Canadian Dollar', 'unit': 'CA$', 'value': 38996.495, 'type': 'fiat'}, 'chf': {'name': 'Swiss Franc', 'unit': 'Fr.', 'value': 26317.073, 'type': 'fiat'}, 'clp': {'name': 'Chilean Peso', 'unit': 'CLP$', 'value': 23178909.624, 'type': 'fiat'}, 'cny': {'name': 'Chinese Yuan', 'unit': '¥', 'value': 195912.658, 'type': 'fiat'}, 'czk': {'name': 'Czech Koruna', 'unit': 'Kč', 'value': 637677.641, 'type': 'fiat'}, 'dkk': {'name': 'Danish Krone', 'unit': 'kr.', 'value': 198055.29, 'type': 'fiat'}, 'eur': {'name': 'Euro', 'unit': '€', 'value': 26601.617, 'type': 'fiat'}, 'gbp': {'name': 'British Pound Sterling', 'unit': '£', 'value': 23268.639, 'type': 'fiat'}, 'hkd': {'name': 'Hong Kong Dollar', 'unit': 'HK$', 'value': 223275.915, 'type': 'fiat'}, 'huf': {'name': 'Hungarian Forint', 'unit': 'Ft', 'value': 10580028.861, 'type': 'fiat'}, 'idr': {'name': 'Indonesian Rupiah', 'unit': 'Rp', 'value': 437327392.451, 'type': 'fiat'}, 'ils': {'name': 'Israeli New Shekel', 'unit': '₪', 'value': 104295.5, 'type': 'fiat'}, 'inr': {'name': 'Indian Rupee', 'unit': '₹', 'value': 2347716.184, 'type': 'fiat'}, 'jpy': {'name': 'Japanese Yen', 'unit': '¥', 'value': 3757697.287, 'type': 'fiat'}, 'krw': {'name': 'South Korean Won', 'unit': '₩', 'value': 37228582.338, 'type': 'fiat'}, 'kwd': {'name': 'Kuwaiti Dinar', 'unit': 'KD', 'value': 8607.248, 'type': 'fiat'}, 'lkr': {'name': 'Sri Lankan Rupee', 'unit': 'Rs', 'value': 9508617.967, 'type': 'fiat'}, 'mmk': {'name': 'Burmese Kyat', 'unit': 'K', 'value': 58899882.381, 'type': 'fiat'}, 'mxn': {'name': 'Mexican Peso', 'unit': 'MX$', 'value': 535499.91, 'type': 'fiat'}, 'myr': {'name': 'Malaysian Ringgit', 'unit': 'RM', 'value': 127594.121, 'type': 'fiat'}, 'ngn': {'name': 'Nigerian Naira', 'unit': '₦', 'value': 12913515.52, 'type': 'fiat'}, 'nok': {'name': 'Norwegian Krone', 'unit': 'kr', 'value': 304328.548, 'type': 'fiat'}, 'nzd': {'name': 'New Zealand Dollar', 'unit': 'NZ$', 'value': 45202.482, 'type': 'fiat'}, 'php': {'name': 'Philippine Peso', 'unit': '₱', 'value': 1556702.325, 'type': 'fiat'}, 'pkr': {'name': 'Pakistani Rupee', 'unit': '₨', 'value': 7902565.149, 'type': 'fiat'}, 'pln': {'name': 'Polish Zloty', 'unit': 'zł', 'value': 125289.718, 'type': 'fiat'}, 'rub': {'name': 'Russian Ruble', 'unit': '₽', 'value': 2189831.267, 'type': 'fiat'}, 'sar': {'name': 'Saudi Riyal', 'unit': 'SR', 'value': 106857.054, 'type': 'fiat'}, 'sek': {'name': 'Swedish Krona', 'unit': 'kr', 'value': 298920.554, 'type': 'fiat'}, 'sgd': {'name': 'Singapore Dollar', 'unit': 'S$', 'value': 38179.699, 'type': 'fiat'}, 'thb': {'name': 'Thai Baht', 'unit': '฿', 'value': 967101.824, 'type': 'fiat'}, 'try': {'name': 'Turkish Lira', 'unit': '₺', 'value': 540770.966, 'type': 'fiat'}, 'twd': {'name': 'New Taiwan Dollar', 'unit': 'NT$', 'value': 871383.505, 'type': 'fiat'}, 'uah': {'name': 'Ukrainian hryvnia', 'unit': '₴', 'value': 1035879.081, 'type': 'fiat'}, 'vef': {'name': 'Venezuelan bolívar fuerte', 'unit': 'Bs.F', 'value': 2848.288, 'type': 'fiat'}, 'vnd': {'name': 'Vietnamese đồng', 'unit': '₫', 'value': 671181203.648, 'type': 'fiat'}, 'zar': {'name': 'South African Rand', 'unit': 'R', 'value': 523546.94, 'type': 'fiat'}, 'xdr': {'name': 'IMF Special Drawing Rights', 'unit': 'XDR', 'value': 21132.891, 'type': 'fiat'}, 'xag': {'name': 'Silver - Troy Ounce', 'unit': 'XAG', 'value': 1258.809, 'type': 'commodity'}, 'xau': {'name': 'Gold - Troy Ounce', 'unit': 'XAU', 'value': 14.147, 'type': 'commodity'}, 'bits': {'name': 'Bits', 'unit': 'μBTC', 'value': 1000000.0, 'type': 'crypto'}, 'sats': {'name': 'Satoshi', 'unit': 'sats', 'value': 100000000.0, 'type': 'crypto'}}}
    btc_rate = rec_ex['rates']['usd']['value']

    with Session(alch_engine.engine) as session:
        rec = model_db.RateHistory(
        coin_name = rec_ex['rates']['btc']['name'],
        rate = rec_ex['rates']['usd']['value'],
        date_rec = datetime.datetime.now().strftime("%d.%m.%Y"),
        time_rec = datetime.datetime.now().strftime("%H:%M")
        )

        session.add(rec)
        session.commit()




if __name__ == '__main__':
    pass
