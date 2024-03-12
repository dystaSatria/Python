def tentukan_jenis_kelamin(nama):
    
    awalan_perempuan = ['Sri', 'Ayu', 'Dewi', 'Putri']
    akhiran_perempuan = ['a', 'i', 'u']
    
    
    awalan_laki_laki = ['Bambang', 'Agus', 'Joko']
    akhiran_laki_laki = ['o', 'no', 'di']

    
    for awalan in awalan_perempuan:
        if nama.startswith(awalan):
            return 'Perempuan'
    for akhiran in akhiran_perempuan:
        if nama.lower().endswith(akhiran):
            return 'Perempuan'
    
    
    for awalan in awalan_laki_laki:
        if nama.startswith(awalan):
            return 'Laki-laki'
    for akhiran in akhiran_laki_laki:
        if nama.lower().endswith(akhiran):
            return 'Laki-laki'
    
    
    return 'Tidak Diketahui'

def proses_nama_dari_file(nama_file, output_file):
    with open(nama_file, 'r') as file, open(output_file, 'w') as outfile:
        for nama in file:
            nama = nama.strip()  
            jenis_kelamin = tentukan_jenis_kelamin(nama)
            outfile.write(f"{nama}, {jenis_kelamin}\n")
            print(f"Jenis kelamin untuk nama {nama} kemungkinan adalah {jenis_kelamin}.")


nama_file = 'daftarNama.txt'
output_file = 'hasil_jenis_kelamin.txt'
proses_nama_dari_file(nama_file, output_file)
