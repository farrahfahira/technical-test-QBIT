# Case 1

# data catatan buah yang dimiliki Andi dibuat dalam format python

fruits = [
    {
        'fruitId': 1,
        'fruitName': 'Apel',
        'fruitType': 'IMPORT',
        'stock': 10
    },
    {
        'fruitId': 2,
        'fruitName': 'Kurma',
        'fruitType': 'IMPORT',
        'stock': 20
    },
    {
        'fruitId': 3,
        'fruitName': 'apel',
        'fruitType': 'IMPORT',
        'stock': 50
    },
    {
        'fruitId': 4,
        'fruitName': 'Manggis',
        'fruitType': 'LOCAL',
        'stock': 100
    },
    {
        'fruitId': 5,
        'fruitName': 'Jeruk Bali',
        'fruitType': 'LOCAL',
        'stock': 10
    },
    {
        'fruitId': 6,
        'fruitName': 'KURMA',
        'fruitType': 'IMPORT',
        'stock': 20
    },
    {
        'fruitId': 7,
        'fruitName': 'Salak',
        'fruitType': 'LOCAL',
        'stock': 150
    }
]

# soal no 1 - menampilkan data unique fruitName dari setiap fruits value

print("Soal No. 1")


def tampilkan_namabuah(data_buah):
    nama_buah = set(buah['fruitName'].lower() for buah in data_buah)
    return nama_buah


print("Question: Buah apa saja yg dimiliki Andi?")
print("Answer: ", tampilkan_namabuah(fruits))


# soal no 2 - jumlah wadah berdasarkan tipe buah beserta isi buah dalam tiap wada

print("\nSoal No. 2")


def hitung_jumlah_fruitType(data_buah):
    fruit_types = set(buah['fruitType'] for buah in data_buah)
    return len(fruit_types)


jumlah_wadah = hitung_jumlah_fruitType(fruits)


def tampilkan_buah_per_wadah(data_buah, fruitType):
    buah_per_wadah = [
        buah for buah in data_buah if buah['fruitType'] == fruitType]
    nama_buah_per_wadah = tampilkan_namabuah(buah_per_wadah)
    for nama_buah in nama_buah_per_wadah:
        print(nama_buah, end=', ')


def tampilkan_semua_buah_per_wadah(data_buah):
    fruit_types = set(buah['fruitType'] for buah in data_buah)
    for fruitType in fruit_types:
        print(f"Buah yang ada dalam wadah '{fruitType}':")
        tampilkan_buah_per_wadah(data_buah, fruitType)
        print()


print("Question: Berapa jumlah wadah yang dibutuhkan? Dan ada buah apa saja di masing-masing wadah?")
print("Answer: Jumlah wadah yang dibutuhkan adalah sebanyak", jumlah_wadah)

tampilkan_semua_buah_per_wadah(fruits)

# soal no 3 - total stock buah di tiap wadah

print("\nSoal No. 3")


def total_stock_per_wadah(data_buah):
    total_stock_per_fruitType = {}
    for buah in data_buah:
        fruitType = buah['fruitType']
        stock = buah['stock']
        if fruitType in total_stock_per_fruitType:
            total_stock_per_fruitType[fruitType] += stock
        else:
            total_stock_per_fruitType[fruitType] = stock
    return total_stock_per_fruitType


total_stock_per_fruitType = total_stock_per_wadah(fruits)

print("Question: Berapa total stock buah yang ada di masing-masing wadah?")
for fruitType, total_stock in total_stock_per_fruitType.items():
    print(f"Total stok untuk '{fruitType}': {total_stock}")


# soal no 4 - komentar

print("\nSoal No. 4")

print("Question: Apakah ada komentar terkait kasus di atas?")
print("Answer: Ya. Pertama, beberapa data buah memiliki fruitId yang sama. Id biasanya dijadikan unique atau primary key. Kedua, pada penamaan nama buah (fruitName) dibuat case-sensitive, sehingga Apel dan apel akan terhitung beda. Ketiga, data stock diberikan tipe data number, yamng mana memungkinkan untuk memberi nilai minus.")

# Case 2

comments = [
    {
        'commentId': 1,
        'commentContent': 'Hai',
        'replies': [
            {
                'commentId': 11,
                'commentContent': 'Hai juga',
                'replies': [
                    {
                        'commentId': 111,
                        'commentContent': 'Haai juga hai jugaa'
                    },
                    {
                        'commentId': 112,
                        'commentContent': 'Haai juga hai jugaa'
                    }
                ]
            },
            {
                'commentId': 12,
                'commentContent': 'Hai juga',
                'replies': [
                    {
                        'commentId': 121,
                        'commentContent': 'Haai juga hai jugaa'
                    }
                ]
            }
        ]
    },
    {
        'commentId': 2,
        'commentContent': 'Halooo'
    }
]

# soal no 5 - hitung total komentar

print("\nSoal No. 5")


def hitung_total_komentar(data_komentar):
    total_komentar = 0
    for data in data_komentar:
        total_komentar += 1
        if 'replies' in data:
            total_komentar += hitung_total_komentar(data['replies'])
    return total_komentar


total = hitung_total_komentar(comments)

print("Question: Buatlah fungsi untuk menghitung total komentar yang ada, termasuk semua balasan komentar. Berdasarkan data di atas, total komentar adalah 7 komentar.")
print("Answer: Total komentar adalah sebanyak", total)
