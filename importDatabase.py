import csv
import pymysql

# Menghubungkan ke database MySQL
connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    db='manpro'
)


count = 0

print("hahahahahahha")
# Membuka file CSV
with open('Data.csv', 'r') as file:
    csv_data = csv.DictReader(file)
    print("hehehehehehhe")
    # Mengiterasi baris-baris data dan memasukkan ke database
    for row in csv_data:
        print("hohoohohohohoho")
        cursor = connection.cursor()
        query = "INSERT INTO startup (Nama, Category, Funding, Country, State, Region, City) VALUES (%s, %s, %s,%s, %s, %s,%s)"
        count += 1
        values = (
            row['name'], row['category_list'], row['funding_total_usd'], row['country_code'],
            row['state_code'], row['region'], row['city']
        )
        print(count)

        cursor.execute(query, values)
        connection.commit()

# Menutup koneksi
print("xixixixiixixi")
connection.close()
