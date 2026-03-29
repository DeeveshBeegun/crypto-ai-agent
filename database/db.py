from sqlalchemy import create_engine
import pandas as pd

from collectors.market_collector import getInfoFromBinance

def create_database_engine(): 
    engine = create_engine('sqlite:///BTCUSDTstream.db')
    return engine


def datatransfo(msg):
	df = pd.DataFrame({'Time':msg['E'], 'Price': msg['k']['c']}, index=[0])
	df.Price = df.Price.astype(float)
	df.Time = pd.to_datetime(df.Time,unit='ms')
	return df

async def updateDatabase(): 
	current_event = pd.Series(pd.to_datetime(0))
	while True:
		msg = await getInfoFromBinance()
		df = datatransfo(msg)
		if df.Time.values > current_event.values:
			current_event = df.Time
			engine = create_database_engine()
			df.to_sql('BTCUSDT', engine, if_exists='append', index=False)
			
def read_sql(table_name: str = 'BTCUSDT'):
	engine = create_database_engine()
	query = f"SELECT * FROM {table_name}"
	return pd.read_sql_query(query, engine)