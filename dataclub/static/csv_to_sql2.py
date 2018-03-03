import pandas as pd
from sqlalchemy import create_engine

csvPath = r"testdata.csv"

df = pd.read_csv(csvPath)
df.columns = [c.lower() for c in df.columns]

engine = create_engine('postgresql://tadeup:unsafe@localhost:5432/dataclub')
df.to_sql("testdata", engine)