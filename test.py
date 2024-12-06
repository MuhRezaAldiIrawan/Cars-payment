import tkinter as tk
from tkinter import messagebox

def hitung_angsuran(otr, dp_persen, jangka_waktu):
    
    # Menghitung DP dan pokok utang 
    dp = otr * (dp_persen / 100)
    pokok_utang = otr - dp

    if jangka_waktu <= 12:
        bunga_persen = 12
    elif 12 < jangka_waktu <= 24:
        bunga_persen = 14
    else:
        bunga_persen = 16.5

    # Hitung bunga
    bunga = bunga_persen / 100

    # Hitung angsuran per bulan
    angsuran_per_bulan = (pokok_utang + (pokok_utang * bunga)) / jangka_waktu

    return angsuran_per_bulan, dp


def hitung():
    try:
        otr = float(entry_otr.get())
        dp_persen = float(entry_dp.get())
        jangka_waktu = int(entry_jangka_waktu.get())

        # Hitung angsuran
        angsuran, dp = hitung_angsuran(otr, dp_persen, jangka_waktu)

        result_label.config(text=f"Hasil Perhitungan:\n"
                                 f"Harga Mobil (OTR): Rp{otr:,.2f}\n"
                                 f"Down Payment (DP): Rp{dp:,.2f}\n"
                                 f"Jangka Waktu: {jangka_waktu} bulan\n"
                                 f"Angsuran per bulan: Rp{angsuran:,.2f}")
    except ValueError:
        messagebox.showerror("Error", "Input tidak valid! Harap masukkan angka yang benar.")


window = tk.Tk()
window.title("Penghitung Angsuran Kredit Mobil")
window.geometry("400x400")
window.resizable(False, False)

title_label = tk.Label(window, text="Aplikasi Penghitung Angsuran Kredit Mobil", font=("Arial", 14), pady=10)
title_label.pack()

frame = tk.Frame(window)
frame.pack(pady=10)

tk.Label(frame, text="Harga Mobil (OTR):").grid(row=0, column=0, sticky="w")
entry_otr = tk.Entry(frame, width=20)
entry_otr.grid(row=0, column=1)

tk.Label(frame, text="DP (%) :").grid(row=1, column=0, sticky="w")
entry_dp = tk.Entry(frame, width=20)
entry_dp.grid(row=1, column=1)

tk.Label(frame, text="Jangka Waktu (bulan):").grid(row=2, column=0, sticky="w")
entry_jangka_waktu = tk.Entry(frame, width=20)
entry_jangka_waktu.grid(row=2, column=1)


hitung_button = tk.Button(window, text="Hitung Angsuran", command=hitung, bg="blue", fg="white")
hitung_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

window.mainloop()
