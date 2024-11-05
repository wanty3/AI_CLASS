# Definisikan matriks
A = [[3, 0], [-1, 2], [1, 1]]
B = [[4, -1], [0, 2]]
C = [[1, 4, 2], [3, 1, 5]]
D = [[1, 5, 2], [-1, 0, 1], [3, 2, 4]]
E = [[6, 1, 3], [-1, 1, 2], [4, 1, 3]]

# Fungsi untuk perkalian dua matriks
def multiply(X, Y):
    # Memastikan matriks dapat dikalikan
    if len(X[0]) != len(Y):
        raise ValueError("Jumlah kolom matriks X harus sama dengan jumlah baris matriks Y.")
    
    result = []
    for i in range(len(X)):
        row_result = []
        for j in range(len(Y[0])):
            element = sum(X[i][k] * Y[k][j] for k in range(len(Y)))
            row_result.append(element)
        result.append(row_result)
    return result

# Fungsi untuk penjumlahan matriks
def add(X, Y):
    # Memastikan matriks memiliki ukuran yang sama
    if len(X) != len(Y) or len(X[0]) != len(Y[0]):
        raise ValueError("Ukuran matriks harus sama untuk penjumlahan.")
    
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

# Fungsi untuk pengurangan matriks
def subtract(X, Y):
    # Memastikan matriks memiliki ukuran yang sama
    if len(X) != len(Y) or len(X[0]) != len(Y[0]):
        raise ValueError("Ukuran matriks harus sama untuk pengurangan.")
    
    return [[X[i][j] - Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

# Fungsi untuk menampilkan hasil matriks
def print_matrix(label, matrix):
    print(label)
    for row in matrix:
        print(row)
    print()  # Baris kosong untuk pemisah

# Hitung hasil operasi
try:
    A_kali_C = multiply(A, C)
    A_kali_B = multiply(A, B)
    D_tambah_E = add(D, E)
    D_kurang_E = subtract(D, E)

    # Tampilkan hasil
    print_matrix("Hasil dari A x C :", A_kali_C)
    print_matrix("Hasil dari A x B :", A_kali_B)
    print_matrix("Hasil dari D + E :", D_tambah_E)
    print_matrix("Hasil dari D - E :", D_kurang_E)

except ValueError as e:
    print("Terjadi kesalahan:", e)
