#mendeklarasikan delta
deltaL1 = {'q0':{'0':'q0', '1':'q1'},
           'q1':{'0':'q2', '1':'q1'},
           'q2':{'0':'q0', '1':'q3'},
           'q3':{'0':'q3', '1':'q3'}}

deltaL2 = {'q0':{'0':'q4', '1':'q1'},
           'q1':{'0':'q2', '1':'q4'},
           'q2':{'0':'q4', '1':'q3'},
           'q3':{'0':'q3', '1':'q3'},
           'q4':{'0':'q4', '1':'q4'}}

deltaL3 = {'q0': {'0': 'q0', '1':'q1'},
           'q1': {'0': 'q2', '1':'q1'},
           'q2': {'0': 'q0', '1':'q3'},
           'q3': {'0': 'q2', '1':'q1'}}

deltaL4 = {'q0': {'0': 'q1', '1':'q0'},
           'q1': {'0': 'q0', '1':'q1'}}

deltaL5 = {'q0': {'0': 'q0', '1':'q1'},
           'q1': {'0': 'q1', '1':'q0'}}

def valid(pil, string):
    if pil == 1:
        validasi = 'Diterima' if deltatopi(deltaL1, 'q0', {'q3'}, string) else 'Ditolak'
        print('\n' + string, '->', validasi)
    if pil == 2:
        validasi = 'Diterima' if deltatopi(deltaL2, 'q0', {'q3'}, string) else 'Ditolak'
        print('\n' + string, '->', validasi)
    if pil == 3:
        validasi = 'Diterima' if deltatopi(deltaL3, 'q0', {'q3'}, string) else 'Ditolak'
        print('\n' + string, '->', validasi)
    if pil == 4:
        validasi = 'Diterima' if deltatopi(deltaL4, 'q0', {'q0'}, string) else 'Ditolak'
        print('\n' + string, '->', validasi)
    if pil == 5:
        validasi = 'Diterima' if deltatopi(deltaL5, 'q0', {'q1'}, string) else 'Ditolak'
        print('\n' + string, '->', validasi)

def deltatopi(transisi,initial,finalstate,s):
    state = initial
    i = len(s)
    j = 1
    k = 1

    print('\ndeltop(q0',',',s,')\n')

    #untuk menampilkan fungsi deltatopi
    for c in s:
        if k == i:
            print('=', k, 'delta ( deltop ( q0, e )', s[(i - k):i], ')')
        else:
            print('=', k, 'delta ( deltop ( q0,', s[0:(i - k)], ')', s[(i - k):i], ')')
        k+=1

    #Transition Function
    for c in s:
        try:
            print('=',(i+1)-j,'delta (', state, ',', c, ')', s[j:i])
            state = transisi[state][c]
            j+=1
        except KeyError:
            return False

    print('=',state)
    return state in finalstate

# Main
print('Program Pengecekan 5 Bahasa (DFA)')

# Menu
exit = True
while (exit):
    print('Menu :')
    print('1. L1 = Himpunan semua string yang mengandung substring 101')
    print('2. L2 = Himpunan semua string yang mengandung prefiks 101')
    print('3. L3 = Himpunan semua string yang mengandung sufiks 101')
    print('4. L4 = Himpunan semua string yang mengandung jumlah simbol 0 genap')
    print('5. L5 = Himpunan semua string yang mengandung jumlah simbol 1 ganjil')
    try:
        pil = int(input('Masukan Pilihan Menu : '))
        if 0 < pil < 6:
            break
        else:
            print("Pilihan Menu Tidak Tersedia")
    except:
        print("Pilihan Menu Tidak Tersedia")

    # input
    str = input('Enter a String : ')
    for char in str:
        if char != '0' and char != '1':
            print('String Terdiri Selain 0 dan 1')
            break

    valid(pil, str)
    while (exit):
        exit = input('Apakah Anda Ingin Mengulanginya Lagi [Y/N] : ')
        if exit == 'N' or exit == 'n':
            print('Terima Kasih Sudah Menggunakan Program Kami')
            exit = False
        elif exit == 'Y' or  exit == 'y':
            break
        else:
            print('Pilihan Tidak Tersedia, Pilihan Tersedia Hanya Y atau N')

