import pandas as pd
from sqlalchemy import create_engine

# Buat koneksi engine ke DB postgres
engine = create_engine('postgresql+psycopg2://postgres:mysecretpassword@localhost:5433/hr_data')

# Baca file CSV
df = pd.read_csv('employee_clean_data.csv')

# Masukin data nya
df.to_sql('employee_data', con=engine, if_exists='replace', index=False)

print("Data berhasil di-inject ke tabel employee_data")

