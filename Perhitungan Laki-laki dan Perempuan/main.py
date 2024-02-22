def hitung_jenis_kelamin(input_file):
    
    jumlah_laki_laki = 0
    jumlah_perempuan = 0

   
    with open(input_file, 'r') as file:
        for line in file:
            parts = line.strip().split(', ')
            
            if len(parts) == 2:
                _, jenis_kelamin = parts
                if jenis_kelamin == 'Laki-laki':
                    jumlah_laki_laki += 1
                elif jenis_kelamin == 'Perempuan':
                    jumlah_perempuan += 1
            else:
                print(f"Baris tidak sesuai format dan akan dilewati: {line}")

    
    return jumlah_laki_laki, jumlah_perempuan

    
    jumlah_laki_laki = 0
    jumlah_perempuan = 0

    
    with open(input_file, 'r') as file:
        for line in file:
            _, jenis_kelamin = line.strip().split(', ')
            if jenis_kelamin == 'Laki-laki':
                jumlah_laki_laki += 1
            elif jenis_kelamin == 'Perempuan':
                jumlah_perempuan += 1

    
    return jumlah_laki_laki, jumlah_perempuan

def tulis_hasil_quick_count(output_file, jumlah_laki_laki, jumlah_perempuan):
    with open(output_file, 'w') as file:
        file.write("Quick Count Jenis Kelamin\n")
        file.write(f"Jumlah Laki-laki: {jumlah_laki_laki}\n")
        file.write(f"Jumlah Perempuan: {jumlah_perempuan}\n")


input_file = 'hasil_jenis_kelamin.txt'
output_file = 'quick_count_jenis_kelamin.txt'


jumlah_laki_laki, jumlah_perempuan = hitung_jenis_kelamin(input_file)


tulis_hasil_quick_count(output_file, jumlah_laki_laki, jumlah_perempuan)

print("Quick count jenis kelamin telah berhasil ditulis ke file output.")
