# List A yang sudah diberikan
A = [2, 2, 1, 3, 5, 5, 5, 7, 2, 10]

# Input nilai yang ingin dicari
x = int(input("Masukkan nilai x yang ingin ditampilkan: "))

# Logika untuk menghitung kemunculan dan indeks
if x in A:
    count = A.count(x)  # Menghitung berapa kali x muncul
    indices = [index for index, value in enumerate(A) if value == x]  # Mendapatkan semua indeks

    # Output hasil
    print(f"\nVariabel x ({x}) muncul {count} kali dalam list A.")
    print(f"Indeks kemunculan nilai x ({x}): {indices}")
else:
    print(f"\nVariabel x ({x}) tidak ditemukan dalam list A.")
