import pandas as pd

DATA_PATH = "data/DBNetz-Betriebsstellenverzeichnis-Stand2021-10.csv"

# Reading Data as DataFrame
df = pd.read_csv(DATA_PATH, sep=";")