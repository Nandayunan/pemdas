import pandas as pd

# mendeklarasikan dataframe
data = {'Nama': ['John ', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': ['50000', '60000', '70000', '55000']}

#menampilkan data frame
df = pd.DataFrame(data)

# Fungsi untuk menentukan karyawan muda dan tua
df['Status'] = df['Usia'].apply(lambda x: 'Muda' if x < 30 else 'Tua')

print(df)
