from os import system
from datetime import datetime
import getpass
import time

system("cls")
print("Harap Masukkan Password Terlebih Dahulu\n")
user_password = getpass.getpass()

while user_password != "12345":
	time.sleep(1)
	system("cls")
	print("Password yang dimasukkan salah, harap coba lagi.\n")
	time.sleep(1)
	
	user_password = getpass.getpass()
	system("cls")
else:
	time.sleep(1)
	system("cls")
	print("Password yang Dimasukkan Benar! Selamat Datang!")
time.sleep(1)

def view_menu():
	system("cls")
	menu = """
APLIKASI DAFTAR BARANG BELANJA
[A] - Tambah daftar barang
[B] - Tampilkan daftar barang
[C] - Cari Barang
[D] - Perbarui daftar barang
[E] - Hapus barang
[I] - Tampilkan total harga
[Q] - Keluar
		"""
	print(menu)

def verify_ans(char):
	char = char.upper()
	if char == "Y":
		return True
	else:
		return False

def print_header(msg):
	system("cls")
	print(msg)

def buat_id_barang():
	today = datetime.now()
	year = today.year
	month = today.month
	hari = today.day
	counter = len(data_barang)+1
	id_barang = str("%4d%02d%02d-C%03d" % (year, month, hari, counter))
	return id_barang

def print_daftar_barang(id_barang = None, all_fields = False, harga = True):
	if id_barang != None and all_fields == False:
		print(f"""
		-DATA DITEMUKAN -
	ID \t:{id_barang}
	Nama \t:{data_barang[id_barang]["nama"]}
	Jumlah \t:{data_barang[id_barang]["jumlah"]}
	Harga \t:${data_barang[id_barang]["harga"]}
	Tanggal Kadaluarsa \t:{data_barang[id_barang]["tanggal kadaluarsa"]}
		""")
	
	elif id_barang != None and harga == False:
		print(f"""
		-DATA DITEMUKAN-
	ID \t:{id_barang}
	Nama \t:{data_barang[id_barang]["nama"]}
	Jumlah \t:{data_barang[id_barang]["jumlah"]}
			""")

	elif all_fields == True:
		for id_barang in data_barang:
			nama = data_barang[id_barang]["nama"]
			jumlah = data_barang[id_barang]["jumlah"]
			harga = data_barang[id_barang]["harga"]
			tanggal_kadaluarsa = data_barang[id_barang]["tanggal kadaluarsa"]
			print(f"ID:{id_barang}\tNAMA:{nama}\tJUMLAH:{jumlah}\tHARGA:${harga}\tTANGGAL KADALUARSA:{tanggal_kadaluarsa}")

def tambah_barang():
	 
	print_header("-MEMASUKKAN DATA BARANG BARU-")
	nama = input("NAMA\t:") #key dict
	while True:
		try:
			jumlah = int(input("JUMLAH\t:"))
			break
		except ValueError:
			time.sleep(0.3)
			print("Masukkan jumlah dalam bentuk angka")
			time.sleep(0.5)
			continue

	while True:
		try:
			harga = int(input("HARGA\t:$"))
			break
		except ValueError:
			time.sleep(0.3)
			print("Masukkan harga dalam bentuk angka")
			time.sleep(0.5)
			continue

	tanggal_kadaluarsa = input("TANGGAL KADALUARSA\t:")
	user_ans = input("Tekan Y untuk menyimpan(Y/N) : ")
	
	if verify_ans(user_ans):
		id_barang = buat_id_barang()
		print("Menyimpan Data ...")
		
		data_barang[id_barang] = {
			"nama" : nama,
			"jumlah" : jumlah,
			"harga" : harga,
			"tanggal kadaluarsa" : tanggal_kadaluarsa
		}
		print("Data Tersimpan")
	else:
		print("Data batal Disimpan")
	input("Tekan ENTER untuk kembali ke MENU")


def print_data():
	print_header("-SEMUA BARANG-")
	if len(data_barang) == 0:
		print("<BELUM ADA DAFTAR BELANJA YANG DISIMPAN>")
	else:
		print_daftar_barang(all_fields=True)
	input("Tekan ENTER untuk melanjutkan.")


def searching(barang):
	for id_barang in data_barang:
		if data_barang[id_barang]["nama"] == barang:
			print_daftar_barang(id_barang=id_barang)
			return True
	else:
		print("-DATA TIDAK DITEMUKAN-")
		return False

def get_id_contact_from_name(barang):
	for id_barang in data_barang:
		if data_barang[id_barang]["nama"] == barang:
			return id_barang

def seraching_by_id(id_barang):
	if id_barang in data_barang:
		print_daftar_barang(id_barang=id_barang)
		return True
	else:
		print("-DATA TIDAK DETIMUKAN-")
		return False

def cari_barang():
	print_header("-CARI BARANG-\n")
	nama = input("Nama Barang Yang Dicari : ")
	result = searching(nama)
	input("Tekan ENTER untuk kembali Ke menu awal.")

def hapus_barang():
	print_header("-MENGHAPUS BARANG-")
	nama = input("Masukkan Nama Barang Yang Akan Dihapus : ")
	result = searching(nama)
	if result:
		respon = input(f"Yakin ingin menghapus {nama} (Y/N) : ")
		if verify_ans(respon):
			id_barang = get_id_contact_from_name(nama)
			print("Data telah dihapus.")
		else:
			print("Data batal dihapus")
	input("Tekan ENTER untuk kembali ke menu utama")
	
def update_nama(barang):
	print(f"Nama Lama \t:{barang}")
	new_nama = input("Nama Baru \t: ")
	respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
	if verify_ans(respon):
		id_barang = get_id_contact_from_name(barang)
		data_barang[id_barang]["nama"] = new_nama
		#del data_barang[barang]
		print("Data telah di-update")
	else:
		print("Data batal di perbarui")

def update_jumlah(barang):
	id_barang = get_id_contact_from_name(barang)
	print(f"Nama \t:{data_barang[id_barang]['nama']}")
	print(f"Jumlah Lama\t:{data_barang[id_barang]['jumlah']}")
	while  True:
		try:
			new_jumlah = int(input("Jumlah Baru\t: "))
			break
		except ValueError:
			time.sleep(0.3)
			print("Masukkan jumlah dalam bentuk angka")
			time.sleep(0.5)
			continue

	respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
	if verify_ans(respon):
		data_barang[id_barang]['jumlah'] = new_jumlah
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_harga(barang):
	id_barang = get_id_contact_from_name(barang)
	print(f"Nama \t:{data_barang[id_barang]['nama']}")
	print(f"Harga Lama\t:${data_barang[id_barang]['harga']}")
	while True:
		try:
			new_harga = int(input("Harga Baru\t:$"))
			break
		except ValueError:
			time.sleep(0.3)
			print("Masukkan harga dalam bentuk angka")
			time.sleep(0.5)
			continue

	respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
	if verify_ans(respon):
		data_barang[id_barang]['harga'] = new_harga
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_tanggal_kadaluarsa(barang):
	print(f"Nama \t:{data_barang[id_barang]['nama']}")
	print(f"Tangga Kadaluarsa Lama\t:{data_barang[id_barang]['tanggal kadaluarsa']}")
	new_date = input("Tanggal Kadaluarsa Baru\t: ")
	respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
	if verify_ans(respon):
		data_barang[id_barang]['tanggal kadaluarsa'] = new_date
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_barang():
	print_header("PERBARUI DAFTAR BELANJA\n")
	nama = input("Nama Barang yang ingin diperbarui : ")
	result = searching(nama)
	if result == True:
		if result:
			print("Data yang ingin diperbarui : ")
			print("[1]. Nama , [2]. Jumlah , [3]. Harga , [4]. Tanggal Kadaluarsa")
			respon = input("Pilihan : ")
			if respon == "1":
				update_nama(nama)
			if respon == "2":
				update_jumlah(nama)
			if respon == "3":
				update_harga(nama)
			if respon == "4":
				update_tanggal_kadaluarsa(nama)
			input("Tekan ENTER untuk kembali ke menu utama")
	else:
			input("Tekan ENTER untuk kembali ke menu awal.")

def total_harga(id_barang = True):
	print_header("TOTAL HARGA")
	check_input("B")
	print("\n")
	total = sum(x['harga'] for x in (data_barang.values()))
	print("Total Harga : $%i" % total)
	input("-Tekan ENTER untuk kembali Ke menu awal")

data_barang = {
	"20201007-C001" : {
		"nama" : "Buku",
		"jumlah" : "3",
		"harga" : 3,
		"tanggal kadaluarsa" : "Tidak ada"
	},
	"20201007-C002" : {
		"nama" : "Tas",
		"jumlah" : "4",
		"harga" : 9,
		"tanggal kadaluarsa" : "Tidak ada"
	}
}


def check_input(char):
	char = char.upper()
	if char == "Q":
		return True
	elif char == "A":
		tambah_barang()
	elif char == "B":
		print_data()
	elif char == "C":
		cari_barang()
	elif char == "D":
		update_barang()
	elif char == "E":
		hapus_barang()
	elif char == "I":
		total_harga()
stop = False

while not stop:
	view_menu()
	user_input = input("Pilihan : ")
	stop = check_input(user_input)

