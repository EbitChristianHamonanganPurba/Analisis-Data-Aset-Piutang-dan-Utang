import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari file CSV
data_aset = pd.read_csv('aset.csv')
data_piutang = pd.read_csv('piutang.csv')
data_utang = pd.read_csv('utang.csv')

# Analisis Aset
# Memplot histogram nilai aset
plt.figure(figsize=(12, 6))
sns.histplot(data_aset['Nilai (Ribuan $)'], bins=20, kde=True, color='skyblue')
plt.title('Distribusi Nilai Aset', fontsize=16)
plt.xlabel('Nilai Aset (Ribuan $)', fontsize=14)
plt.ylabel('Frekuensi', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)
plt.show()

# Memplot boxplot untuk nilai aset berdasarkan jenis
plt.figure(figsize=(12, 8))
sns.boxplot(data=data_aset, x='Jenis', y='Nilai (Ribuan $)', palette='pastel')
plt.title('Distribusi Nilai Aset Berdasarkan Jenis', fontsize=16)
plt.xlabel('Jenis Aset', fontsize=14)
plt.ylabel('Nilai Aset (Ribuan $)', fontsize=14)
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
plt.grid(True)
plt.show()

# Analisis Piutang
# Memplot jumlah piutang berdasarkan jenis
plt.figure(figsize=(12, 6))
sns.countplot(data=data_piutang, x='Jenis', palette='pastel')
plt.title('Jumlah Piutang Berdasarkan Jenis', fontsize=16)
plt.xlabel('Jenis Piutang', fontsize=14)
plt.ylabel('Jumlah', fontsize=14)
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
plt.grid(True)
plt.show()

# Memplot pie chart untuk persentase jumlah piutang berdasarkan status
plt.figure(figsize=(8, 8))
data_piutang['Status'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2', len(data_piutang['Status'].unique())))
plt.title('Persentase Status Piutang', fontsize=16)
plt.ylabel('')
plt.show()

# Analisis Utang
# Memplot jumlah utang berdasarkan status
plt.figure(figsize=(12, 6))
sns.countplot(data=data_utang, x='Status', palette='Set1')
plt.title('Jumlah Utang Berdasarkan Status', fontsize=16)
plt.xlabel('Status Utang', fontsize=14)
plt.ylabel('Jumlah', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)
plt.show()

# Memplot boxplot untuk nilai utang berdasarkan jenis
plt.figure(figsize=(12, 8))
sns.boxplot(data=data_utang, x='Jenis', y='Nilai (Ribuan $)', palette='Set2')
plt.title('Distribusi Nilai Utang Berdasarkan Jenis', fontsize=16)
plt.xlabel('Jenis Utang', fontsize=14)
plt.ylabel('Nilai Utang (Ribuan $)', fontsize=14)
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
plt.grid(True)
plt.show()
