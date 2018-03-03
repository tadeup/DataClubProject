import psycopg2
import csv

conn = psycopg2.connect("host=localhost dbname=dataclub user=tadeup password=unsafe")
cur = conn.cursor()

def createTable():
    cur.execute("""
    CREATE TABLE testData(
        DividendStocks VARCHAR(5),
        EmergingMarkets VARCHAR(5),
        ForeignStocks VARCHAR(5),
        MunicipalBonds VARCHAR(5),
        NaturalResources VARCHAR(5),
        RiskTolerance FLOAT8,
        USStocks VARCHAR,
        q1 integer,
        q2 integer,
        q3 integer,
        q4 integer,
        q5 integer,
        q6 integer,
        q7 integer,
        q8 integer
    );
    """)

# not working
csvPath = r"C:\Users\tadeu\Desktop\FGV\GV DATA\data_project\dataclub\static\testdata.csv"
with open(csvPath, 'r') as f:
    next(f)
    cur.copy_from(f, 'testdata', sep=',')


# always run the following line to commit changes to the database
conn.commit()