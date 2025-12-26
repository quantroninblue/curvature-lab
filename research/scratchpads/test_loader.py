from dotenv import load_dotenv
load_dotenv()

from engine.data_loader import load_fred_series

df = load_fred_series("DTB3")
print(df.tail())


