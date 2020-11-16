mhs = []
nilai = []
print('Datar Mata Kuliah Advanced Programming ')
print('='*50)
def proses():
	Jumlah = sum(nilai)
	Rata2 = Jumlah / len(nilai)
	mhs_max = nilai.index(max(nilai))
	mhs_min = nilai.index(min(nilai))
	print(' Jumlah nilai dari',len(nilai), 'mahasiswa :', Jumlah)
	print(' Rata-Rata Niai',round(Jumlah))
	print('Nilai tertinggi', mhs[mhs_max], 'Nilai', max(nilai))
	print('Nilai terendah', mhs[mhs_min], 'Nilai', min(nilai))
	return
for i in range(1,15):
	nm_mhs = input('Nama Mahasiswa %d :' %i)
	while True:
		try:
			in_nilai = input('input nilai %d :' %i)
			in_nilai = int(in_nilai)
			break
		except ValueError:
			print('Inputkan Angka Nilai')
	mhs.append(nm_mhs)
	nilai.append(in_nilai)
proses()
