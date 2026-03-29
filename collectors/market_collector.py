from binance.client import Client 
from binance import BinanceSocketManager

client = Client()

bsm = BinanceSocketManager(client)

async def getInfoFromBinance():
	socket = bsm.kline_socket('BTCUSDT')
	await socket.__aenter__()
	msg = await socket.recv() 
	await socket.__aexit__(None, None, None)
	return msg