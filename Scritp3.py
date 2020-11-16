dataBuah = []
def tampil():
	if len(dataBuah) <= 0:
		print ('Maaf, tidak ditemukan data Buah')
	else:
		for indeks in range(len(dataBuah)):
			print ('[%d] %s' % (indeks, dataBuah[indeks]))
def simpan():
	buah = input('Nama Buah : ')
	dataBuah.append(buah)

def delete_buah():
	nmbuah = input('Inputkan Nama Buah :')
	buah_del = [x.lower() for x in dataBuah]
	if nbuah.lower() in buah_del:
		nmbuah.remove(nmbuah)
		data.Buah.remove(nmbuah)
		print('Buah', 'Sudah terhapus dari daftar')
	else:
		print('Buah Tidak ada dalam daftar List')
def gemar():
	penggemar = input('Buah apa yg anda gemari ? :')
	CariBuah =  [x.lower() for x in dataBuah]
	if gemar.lower() in CariBuah:
		print('Buah', gemar, 'Adalah Buah yang adan gemari')
	else:
		print('Buah', gemar, 'Buah Tidak ada dalam daftar List')
def show_menu():
	print('\n')	
	print ('		PROGRAM MAGISTER TEKNIK TERAPAN KOMPUTER')	
	print(' 	        	POLITEKNIK CALTEX RIAU')
	print ('	        	      PEKANBARU')
	print('	credits  code : https://github.com/muzammi06/caltex1')
	print('Abdullah Al Muzammi - email : abdullah20s2tk@mahasiswa.pcr.ac.id')
	print('		  site : abdullah20s2tk.wordpress.com')
	print('\n')
	print(' --------------- MENU ---------------')
	print ('[1] Tampilkan daftar buah :')
	print ('[2] Inputkan daftar buah baru :')
	print ('[3] daftar buah yang anda gemari :')
	print ('[4] Hapus Data buah :')
	print ('[5] Keluar Aplikasi :')
	print('='*50)
	print('Perhatikan, Silahkan pilih Sesuai Nomer [1],[2],[3],[4],[5] :')
	print('='*50)
	menu = input('Pilih Menu : ')
	menu = int(menu)
	print ('\n')
	if menu == 1:
		print('Daftar Data Nama Buah-Buahan ')		
		tampil()
	elif menu == 2:
		simpan()
	elif menu == 3:
		gemar()
	elif menu == 4:
		delete_buah()
	elif menu == 5:
		exit()
	else:
		print ('Mohon Maaf Pilihan anda salah, ulangi kembali')
if __name__ == "__main__":
	while(True):
		show_menu()


	

