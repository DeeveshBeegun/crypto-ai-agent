from binance.client import Client 
from binance import BinanceSocketManager
import asyncio
import pandas as pd

client = Client()

bsm = BinanceSocketManager(client)

async def getInfoFromBinance():
	socket = bsm.kline_socket('BTCUSDT')
	await socket.__aenter__()
	msg = await socket.recv() 
	await socket.__aexit__(None, None, None)
	return msg

def datatransfo(msg):
	df = pd.DataFrame({'Time':msg['E'], 'Price': msg['k']['c']}, index=[0])
	df.Price = df.Price.astype(float)
	df.Time = pd.to_datetime(df.Time,unit='ms')
	return df

print(datatransfo(asyncio.run(getInfoFromBinance())))