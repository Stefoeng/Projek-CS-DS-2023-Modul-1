import random

def mainmenu():
    print(''' 
        Selamat Datang, Agen
    Silahkan pilih:
    1. Daftar Pesan (encrypted)
    2. Daftar pesan (original)
    3. Mamasukkan pesan ke daftar pesan
    4. Menginkripsi pesan
    5. Mengdekripsi pesan
    6. Mengubah pesan
    7. Menghapus pesan
    8. Keluar dari program
        ''')
space="!@#$"
def macan(inkripsi):
    output_str = ""
    for letter in inkripsi:
        if letter.isalpha():
            ascii_code = ord(letter.upper()) + 2
            if ascii_code > ord('Z'):
                ascii_code -= 26
            output_str += chr(ascii_code)
        elif letter == ' ':
            output_str += random.sample(space, 1)[0] # select random special character
        else:
            output_str += letter
    return output_str
def decryption(decryptmacan):
    output = ""
    for i in decryptmacan:
        if i.isalpha():
            code = ord(i) - 2
            if code < ord('A'):
                code += 26
            output += chr(code)
        elif i == '!' or i == '@' or i == '#' or i == '$':
            output += ' '
        else:
            output += i
    return output

def rubah(inkripsi):
    output_str = ""
    for letter in inkripsi:
        if letter.isalpha():
            ascii_code = ord(letter.upper()) + 3
            if ascii_code > ord('Z'):
                ascii_code -= 26
            output_str += chr(ascii_code)
        elif letter == ' ':
            output_str += random.sample(space, 1)[0] # select random special character
        else:
            output_str += letter
    return output_str
def decryption1(deryptrubah):
    output = ""
    for i in decryptrubah:
        if i.isalpha():
            code = ord(i) - 3
            if code < ord('A'):
                code += 26
            output += chr(code)
        elif i == '!' or i == '@' or i == '#' or i == '$':
            output += ' '
        else:
            output += i
    return output

def elang(inkripsi):
    output_str = ""
    for letter in inkripsi:
        if letter.isalpha():
            ascii_code = ord(letter.upper()) + 4
            if ascii_code > ord('Z'):
                ascii_code -= 26
            output_str += chr(ascii_code)
        elif letter == ' ':
            output_str += random.sample(space, 1)[0] # select random special character
        else:
            output_str += letter
    return output_str
def decryption2(decryptelang):
    output = ""
    for i in decryptelang:
        if i.isalpha():
            code = ord(i) - 4
            if code < ord('A'):
                code += 26
            output += chr(code)
        elif i == '!' or i == '@' or i == '#' or i == '$':
            output += ' '
        else:
            output += i
    return output

pesan={'macan':['QNKXGT!CPF$MCM@MTKUVCN$HQTGXC'] , 
       'rubah':['UXEDK!DNDQ@PHQJXDVDL@GXQLD'] , 
       'elang': ['RKETEMR@OEQY@FEGE!MRM$LECS$HEWEV#OITS']}
original={'log1':'Nama tengahnya Pak Jokowi adal'}



while True:
    password=input('Silahkan masukkan Password: ')
    if password=='123':
        while True:
            mainmenu()
            msk=input('')
            if msk=='1':
                print('Berikut adalah daftar pesan yang sudah terdaftar dari HQ, Agen: \nJenis Enigma\t| Pesan\n ')
                for i in pesan:
                    print(f'{i}\t\t|{pesan[i][0:]}')

            elif msk=='2':
                print(f'Berikut adalah daftar pesan yang belum terinkripsi: \n{original}')
            elif msk=='3':
                label=input(f'Silahkan masukkan label pesan: \n')
                pesanmasuk=input(f'Silahkan masukkan pesan: \n')
                original[label]=pesanmasuk
                print(f'Berikut adalah daftar pesan yang belum terinkripsi: \n{original}')
            elif msk=='4':
                while True:
                    print('Berikut adalah daftar pesan original yang belum terinkripsi: ')
                    for i,j in enumerate(original):
                        print(f'{i+1}. {j}: {original[j]}')
                    pilih=input('Masukkan nomor atau label yang hendak diinkripsi: \n')

                    if pilih.isdigit() and int(pilih) in range(1, len(original)+1):
                        index = int(pilih) - 1
                        label = list(original.keys())[index]
                        inkripsi = original[label]
                    elif pilih in original.keys():
                        inkripsi = original[pilih]
                    else:
                        print("Tolong masukkan nomor atau label yang benar!")
                        continue
                    while True:
                        for i,j in enumerate(pesan):
                            print(f'{i+1}. {j}')
                        enigma=input('Pilih nama atau nomor jenis enigma yang ingin dipakai: \n').lower()
                                                
                        if enigma=='macan' or enigma=='1':
                            macan(inkripsi)
                            secret1=macan(inkripsi)
                            pesan['macan'].append(secret1)
                            
                            print(f'pesan berhasil terinkripsi, inkripsi berupa: {secret1} telah masuk di daftar dan terhapus dari daftar original')
                            break
                        elif enigma=='rubah' or enigma=='2':
                            rubah(inkripsi)
                            secret2=rubah(inkripsi)
                            pesan['rubah'].append(secret2)
                            
                            print(f'pesan berhasil terinkripsi, inkripsi berupa: {secret2} telah masuk di daftar dan terhapus dari daftar original')
                            break
                        elif enigma=='elang' or enigma=='3':
                            elang(inkripsi)
                            secret3=elang(inkripsi)
                            pesan['elang'].append(secret3)
                            
                            print(f'pesan berhasil terinkripsi, inkripsi berupa: {secret3} telah masuk di daftar dan terhapus dari daftar original')
                            break
                        else:
                            print('Tolong pilih enigma yang benar!')
                    break
                    
            elif msk=='5':
                while True:
                    for i,name in enumerate(pesan):
                        print(f'{i+1}. {name}')
                    pilihpesan=input('Silahkan pilih nama jenis atau nomor enigma dari daftar: ').lower()
                    if pilihpesan=='macan' or pilihpesan=='1':
                        print('Berikut adalah daftar pesan yang terdaftar dengan enigma macan:')
                        for i,code in enumerate(pesan['macan']):
                            print(f'{i+1}. {code}\n')
                        macanpilih=int(input('Pilihlah nomor pesan yang anda inginkan: '))
                        decryptmacan=pesan['macan'][macanpilih-1]
                        print(f'Pesan tersiratnya adalah: \n{decryption(decryptmacan)}')
                        tigdec=decryption(decryptmacan)
                        while True:
                            mau=input('Apakah anda ingin memasukan pesan kedalam daftar pesan original? Y/N: ').lower()
                            if mau=='y':
                                label=input('silahkan masukkan label pesan: ')
                                original[label]=tigdec
                                del pesan['macan'][macanpilih-1]
                                print(f'pesan {decryptmacan} dengan label {label} telah berhasil masuk ke daftar dan terhapus dari daftar inkripsi')
                                break
                            elif mau=='n':
                                print('Pesan telah dihapuskan selamanya...')
                                break
                            else:
                                print('Tolong jawab dengan Y atau N')
                        break
                    elif pilihpesan=='rubah' or pilihpesan=='2':
                        print('Berikut adalah daftar pesan yang terdaftar dengan enigma rubah: ')
                        for i,code in enumerate(pesan['rubah']):
                            print(f'{i+1}. {code}\n')
                        rubahpilih=int(input('Pilihlah nomor pesan yang anda inginkan: '))
                        decryptrubah=pesan['rubah'][rubahpilih-1]
                        print(f'Pesan tersiratnya adalah: \n{decryption1(decryptrubah)}')
                        foxdec=decryption1(decryptrubah)
                        while True:
                            mau=input('Apakah anda ingin memasukan pesan kedalam daftar pesan original? Y/N: ').lower()
                            if mau=='y':
                                label=input('silahkan masukkan label pesan: ')
                                original[label]=foxdec
                                del pesan['rubah'][rubahpilih-1]
                                print(f'pesan {decryptrubah} dengan label {label} telah berhasil masuk ke daftar dan terhapus dari daftar inkripsi')
                                break
                            elif mau=='n':
                                print('Pesan telah dihapuskan selamanya...')
                                break
                            else:
                                print('Tolong jawab dengan Y atau N')
                        break
                    elif pilihpesan=='elang' or pilihpesan=='3':
                        print('Berikut adalah daftar pesan yang terdaftar dengan enigma elang: ')
                        for i,code in enumerate(pesan['elang']):
                            print(f'{i+1}. {code}\n')
                        elangpilih=int(input('Pilihlah nomor pesan yang anda inginkan: '))
                        decryptelang=pesan['elang'][elangpilih-1]
                        print(f'Pesan tersiratnya adalah: \n{decryption2(decryptelang)}')
                        eagdec=decryption2(decryptelang)
                        while True:
                            mau=input('Apakah anda ingin memasukan pesan kedalam daftar pesan original? Y/N: ').lower()
                            if mau=='y':
                                label=input('silahkan masukkan label pesan: ')
                                original[label]=eagdec
                                del pesan['macan'][elangpilih-1]
                                print(f'pesan {decryptelang} dengan label {label} telah berhasil masuk ke daftar dan terhapus dari daftar inkripsi')
                                break
                            elif mau=='n':
                                print('Pesan telah dihapuskan selamanya...')
                                break
                            else:
                                print('Tolong jawab dengan Y atau N')
                        break             
                    else:
                        print('Tolong masukkan nama enigma yang benar!')
            elif msk=='6':
                try:
                    print('1. Ganti label\n2. ganti isi pesan')
                    pilih=int(input('pilih label dari daftar: '))
                except ValueError:
                    print('maaf tolong masukkan angka dari daftar saja')
                if pilih==1:
                    print('berikut adalah daftar label original:\n')
                    for i, j in enumerate(original.keys()):
                        print(f'{i+1}. {j}')
                    try:
                        chooselabel = int(input('Pilih nomor label yang ingin diubah: '))
                        labellist= list(original.keys())
                        oldlabel = labellist[chooselabel-1]
                        newlabel = input('Masukkan nama label baru: ')
                        original[newlabel] = original.pop(oldlabel)
                        print(f'Label {oldlabel} berhasil diganti dengan label {newlabel}.')
                    except ValueError:
                        print('maaf tolong masukkan angka dari daftar saja')
                elif pilih ==2:
                    for i, isi in enumerate(original.values()):
                        print(f'berikut adalah daftar label original:\n {i+1}. {isi}')
                    try:
                        choosevalue= int(input('Pilih nomor pesan isi yang ada ingin anda ubah: '))
                        label= list(original.keys())[choosevalue-1]
                        newvalue= input('Masukkan pesan baru: ')
                        original[label]=newvalue
                        print(f'Pesan label {label} berhasil diubah menjadi {newvalue}.')
                    except ValueError:
                        print('tolong pilih angka yang hanya di daftar')

            elif msk=='7':
                while True:
                    print('1. Hapus dari daftar pesan enkripsi\n2. Hapus dari daftar pesan original\n')
                    hapus=int(input('Masukkan nomor pilihan dari daftar: '))
                    if hapus==1: ##buat hapus dari tersirat
                        while True:
                            hapusenigma=input('Pilih dari dasar enigma: ')
                            for i,j in enumerate(pesan):
                                print(f'{i+1}. {j}')
                            if hapusenigma=='1':
                                for i, j in enumerate(pesan(macan)):
                                    print(f'{i+1}. {j}')
                                hapusisi=input('Pilih nomor isi yang mau dihapus')
                                del pesan[macan][hapusisi-1]
                                print('Pesan telah terhapus...')
                                break
                            elif hapusenigma=='2':
                                for i, j in enumerate(pesan(rubah)):
                                    print(f'{i+1}. {j}')
                                hapusisi=input('Pilih nomor isi yang mau dihapus')
                                del pesan[rubah][hapusisi-1]
                                print('Pesan telah terhapus...')
                                break
                            elif hapusenigma=='3':
                                for i, j in enumerate(pesan(elang)):
                                    print(f'{i+1}. {j}')
                                hapusisi=input('Pilih nomor isi yang mau dihapus')
                                del pesan[elang][hapusisi-1]
                                print('Pesan telah terhapus...')
                                break
                            else:
                                print('Tolong pilih nomor yang benar')
                    elif hapus==2:
                        
                            for i, j in enumerate(original):
                                print(f'{i+1}. {j}: {original[j]}\n')
                            try:    
                                hapusoriginal=int(input('Pilih nomor pesan original yang mau dihapus: '))
                                del original[list(original.keys())[hapusoriginal-1]]
                                print('Pesan telah dihapus...')
                            except ValueError:
                                print('Pesan dengan nomor tersebut tak ditemukan')
                    else:
                        print('Tolong masukkan 1 atau 2 saja...')
            elif msk=='8':
                print('Selamat jalan, Agen')
                break
            else:
                print('Tolong masukkan pilihan yang benar')
        break
    else:
        print('Hayo kamu ga baca Readme...')








