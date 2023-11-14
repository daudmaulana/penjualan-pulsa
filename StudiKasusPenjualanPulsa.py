pulsa_umum = [25000, 30000, 50000, 100000]
pulsa_liveon = [65000, 100000, 150000]

def struk(nomor,hasil,bayar):
    print('Konter Apalah')
    print('Jalan-Jalan No. 10')
    print('\n--------------------')
    print(f'Nomor : {nomor}')
    print(f'Beli : {hasil}')
    print(f'Bayar : {bayar}')
    print(f'Kembali : {bayar - hasil}')
    print('--------------------')
    return True

def tampil_pulsa(provider):
    if provider == 'LiveOn':
        print('\nDaftar Pulsa :')
        print()
        for i,v in enumerate(pulsa_liveon):
            print(f'{i+1}. {v}')
        beli = int(input('\nMasukkan Beli Pulsa : '))
        hasil = pulsa_liveon[beli - 1]   
    else:
        print('\nDaftar Pulsa :')
        print()
        for i,v in enumerate(pulsa_umum):
            print(f'{i+1}. {v}')
        beli = int(input('\nMasukkan Beli Pulsa : '))
        hasil = pulsa_umum[beli - 1] 
    
    nomor = input('Masukkan Nomor : ')
    bayar = int(input('Masukkan Bayar : '))
    return struk(nomor,hasil,bayar)     

while True:    
    print('\nSilahkan Pilih Provider :')
    print('------------------')
    print('1. Indosat')
    print('2. XL')
    print('3. Tri')
    print('4. LiveOn')
    print('5. Keluar')
    print('------------------')

    pilih = input('Masukkan Pilihan : ')

    if pilih == '5':
        print('\nKeluar Program')
        break
    elif pilih == '1':
        provider = 'Indosat'
    elif pilih == '2':
        provider = 'XL'
    elif pilih == '3':
        provider = 'Tri'
    elif pilih == '4':
        provider = 'LiveOn'
        
    tampil_pulsa(provider)
    
    
    
    