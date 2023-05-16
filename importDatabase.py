import csv
import pymysql

# Menghubungkan ke database MySQL
connection = pymysql.connect(
    host='localhost',
    user=' ',
    password=' ',
    db='manpro'
)

# Membuka file CSV
with open('Data.csv', 'r') as file:
    csv_data = csv.reader(file)
    next(csv_data)  # Melewati baris header jika diperlukan

    # Mengiterasi baris-baris data dan memasukkan ke database
    for row in csv_data:
        cursor = connection.cursor()
        query = "INSERT INTO table_name (Nama, Category, Funding, Country, State, Region, City) VALUES (%s, %s, %s,%s, %s, %s,%s)"
        cursor.execute(query, (row[0], row[1], row[2],row[3], row[4], row[5],row[6]))
        connection.commit()

# Menutup koneksi
connection.close()