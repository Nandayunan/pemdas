import pandas as pd

#mendeklarasikan variable data
data = {'Nama': ['John ', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': ['50000', '60000', '70000', '55000']}

df = pd.DataFrame(data)

# Fungsi lambda untuk menggandakan gaji karyawan yang usianya di atas 30 tahun
df['Gaji'] = df.apply(lambda row: str(int(row['Gaji']) * 2) if row['Usia'] > 30 else row['Gaji'], axis=1)

print(df)

# df.apply digunakan untuk menambahkan kolom status