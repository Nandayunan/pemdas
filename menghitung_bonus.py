import pandas as pd

#mendeklarasi varuabel data
data = {'Nama': ['John ', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': ['50000', '60000', '70000', '55000']}

df = pd.DataFrame(data)

# Fungsi untuk menentukan tua dan muda
df['Status'] = df['Usia'].apply(lambda x: 'Muda' if x < 30 else 'Tua')

# Fungsi untuk menghitung bonus
df['Total Gaji'] = df.apply(lambda row: int(row['Gaji']) * 1.1 if row['Status'] == 'Muda' else int(row['Gaji']) * 1.05, axis=1)

print(df)

#df.apply digunakan untuk menambahkan kolom status
