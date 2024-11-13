import tkinter as tk  # Import pustaka tkinter untuk membuat GUI
from tkinter import ttk  # Import ttk untuk widget dengan gaya lebih modern

# Fungsi untuk menangani hasil prediksi
def tampilkan_hasil():
    hasil_label.config(text="Prodi Pilihan: Teknologi Informasi")  # Tampilkan hasil prediksi statis

# Inisialisasi jendela utama
root = tk.Tk()  # Membuat jendela utama aplikasi
root.title("Aplikasi Prediksi Prodi Pilihan")  # Mengatur judul jendela
root.geometry("400x500")  # Mengatur ukuran jendela

# Label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))  # Membuat label judul
judul_label.pack(pady=10)  # Menempatkan label judul di jendela dengan jarak vertikal

# Frame untuk memasukkan nilai mata pelajaran
input_frame = tk.Frame(root)  # Membuat container untuk label dan entry nilai mata pelajaran
input_frame.pack(pady=10)  # Menempatkan frame di dalam root dengan jarak vertikal

# Label dan Entry untuk nilai mata pelajaran
entries = []  # Daftar untuk menyimpan entry nilai
for i in range(1, 11):  # Membuat 10 label dan entry untuk input nilai
    mata_pelajaran_label = tk.Label(input_frame, text=f"Nilai Mata Pelajaran {i}:")  # Label untuk tiap mata pelajaran
    mata_pelajaran_label.grid(row=i-1, column=0, padx=5, pady=5, sticky="w")  # Menempatkan label dalam grid
    
    entry = tk.Entry(input_frame, width=10)  # Membuat entry untuk input nilai
    entry.grid(row=i-1, column=1, padx=5, pady=5)  # Menempatkan entry dalam grid di kolom kedua
    entries.append(entry)  # Menyimpan entry dalam daftar untuk akses nanti

# Tombol Hasil Prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=tampilkan_hasil)  # Membuat tombol untuk prediksi
prediksi_button.pack(pady=10)  # Menempatkan tombol di jendela dengan jarak vertikal

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="Prodi Pilihan: -", font=("Arial", 12))  # Label untuk menampilkan hasil prediksi
hasil_label.pack(pady=10)  # Menempatkan label hasil di jendela dengan jarak vertikal

# Jalankan GUI
root.mainloop()  # Menjalankan loop utama GUI