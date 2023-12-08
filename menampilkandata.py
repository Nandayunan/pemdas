import pandas as pd

data = {'Nama': ['John ', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': ['50000', '60000', '70000', '55000']}

df = pd.DataFrame(data)

# Fungsi lambda untuk menentukan status karyawan berdasarkan usia
df['Status'] = df['Usia'].apply(lambda x: 'Muda' if x < 30 else 'Tua')

# Fungsi lambda untuk menghitung total gaji setelah bonus
df['Total Gaji'] = df.apply(lambda row: int(row['Gaji']) * 1.1 if row['Status'] == 'Muda' else int(row['Gaji']) * 1.05, axis=1)

# Data frame yang telah di perbarui
print("Data Karyawan yang sudah diperbarui:")
print(df)

# Menampilkan Hasil
summary = df.groupby('Status').agg({'Total Gaji': ['sum', 'mean']})
print("\nRekapan hasil berdasrkan status:")
print(summary)

#df.groupby disini digunakan untuk mengelompokan atau memisahkan berdasarkan status