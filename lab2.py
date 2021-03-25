import os

def dvoich(n: int) -> str:
    b = ''
    while n > 0:
        b = b + str(n % 2)
        n = n // 2
    return b

def from_str_to_bits(msg: str) -> str:
    _bits = ''
    for letter in msg:
        _bits += dvoich(ord(letter))
    return _bits

def fr2210(chislo: str) -> int:
    ch = 0
    j = 0
    for i in range(len(chislo)-1, -1, -1):
        ch += int(chislo[i]) * pow(2, j)
        j += 1
    return ch

def str_to_bytes(my_str: str) -> str:
    return ''.join(format(ord(c), '08b') for c in my_str)

def bits2string(b: str) -> str:
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))


### BASE64 ###
def my_base64(text: str) -> str:
    enc_text = ''

    bits = str_to_bytes(text)

    counter = 0
    chunk = ''
    for i in range(len(bits)):
        chunk += bits[i]
        counter += 1
        if counter!=0 and counter % 6 == 0:
            num = fr2210(chunk)
            enc_text += popa[num]
            chunk = ''
            counter = 0

    padding = ''
    if len(chunk) == 2:
        padding = '=='
        chunk += '0000'
    if len(chunk) == 4:
        padding = '='
        chunk += '00'

    if len(padding) != 0:
        num = fr2210(chunk)
        enc_text += popa[num]
        chunk = ''
        counter = 0
        enc_text+=padding

    #print(enc_text)
    return enc_text

def dec_my_base64(enc_text):
    while('=' in enc_text):
        enc_text = enc_text.replace('=','')
    enc_bits = ''
    for letter in enc_text:
        enc_bits += dict_64[letter]
    return bits2string(enc_bits)

### END OF BASE64 ###

### BASE32 ###
def my_base32(text: str) -> str:
    enc_text = ''
    bits = str_to_bytes(text)

    padding = ''
    if len(bits) % 5 == 3:
        padding = '======'
    if len(bits) % 5 == 1:
        padding = '===='
    if len(bits) % 5 == 4:
        padding = '==='
    if len(bits) % 5 == 2:
        padding = '='

    while(len(bits) % 5 != 0):
        bits += '0'

    counter = 0
    chunk = ''
    for i in range(len(bits)):
        chunk += bits[i]
        counter += 1
        if counter!=0 and counter % 5 == 0:
            num = fr2210(chunk)
            enc_text += popa_32[num]
            chunk = ''
            counter = 0

    enc_text += padding

    return enc_text


def dec_my_base32(enc_text: str) -> str:
    while('=' in enc_text):
        enc_text = enc_text.replace('=','')
    enc_bits = ''
    for letter in enc_text:
        enc_bits += dict_32[letter]
    return bits2string(enc_bits)

### END OF BASE32 ###

### MENU FUNCTIONS ###
def read_str_from_file(filepath: str) -> str:
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
    
def write_to_file(filename: str, text: str) -> str:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

### END OF MENU FUNCTIONS ###

dict_64 = {'A': '000000', 
        'B': '000001',
        'C': '000010',
        'D': '000011',
        'E': '000100',
        'F': '000101',
        'G': '000110',
        'H': '000111',
        'I': '001000',
        'J': '001001',
        'K': '001010',
        'L': '001011',
        'M': '001100',
        'N': '001101',
        'O': '001110',
        'P': '001111',
        'Q': '010000',
        'R': '010001',
        'S': '010010',
        'T': '010011',
        'U': '010100',
        'V': '010101',
        'W': '010110',
        'X': '010111',
        'Y': '011000',
        'Z': '011001',
        'a': '011010',
        'b': '011011',
        'c': '011100',
        'd': '011101',
        'e': '011110',
        'f': '011111',
        'g': '100000',
        'h': '100001',
        'i': '100010',
        'j': '100011',
        'k': '100100',
        'l': '100101',
        'm': '100110',
        'n': '100111',
        'o': '101000',
        'p': '101001',
        'q': '101010',
        'r': '101011',
        's': '101100',
        't': '101101',
        'u': '101110',
        'v': '101111',
        'w': '110000',
        'x': '110001',
        'y': '110010',
        'z': '110011',
        '0': '110100',
        '1': '110101',
        '2': '110110',
        '3': '110111',
        '4': '111000',
        '5': '111001',
        '6': '111010',
        '7': '111011',
        '8': '111100',
        '9': '111101',
        '+': '111110',
        '/': '111111'}

popa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

dict_32 = {'A': '00000',
           'B': '00001',
           'C': '00010',
           'D': '00011',
           'E': '00100',
           'F': '00101',
           'G': '00110',
           'H': '00111',
           'I': '01000',
           'J': '01001',
           'K': '01010',
           'L': '01011',
           'M': '01100',
           'N': '01101',
           'O': '01110',
           'P': '01111',
           'Q': '10000',
           'R': '10001',
           'S': '10010',
           'T': '10011',
           'U': '10100',
           'V': '10101',
           'W': '10110',
           'X': '10111',
           'Y': '11000',
           'Z': '11001',
           '2': '11010',
           '3': '11011',
           '4': '11100',
           '5': '11101',
           '6': '11110',
           '7': '11111'}

popa_32 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'

text = 'Man'
# print(text, my_base32(text), dec_my_base32(my_base64(text)))
# print(text, my_base64(text), dec_my_base64(my_base64(text)))

enc_name = 'enc_text.txt'
dec_name = 'dec_text.txt'




Flag = True
err_counter = 0
while(Flag):
    if err_counter > 3:
        Flag = False
    m_num = input("выберите способ кодировки:\n1) base64\n2)base32\n3)выход ")
    if m_num.isnumeric() == False:
        print("введите число пж, осталось, ",err_counter, "попыток")
        err_counter += 1
        continue
    m_num_int = int(m_num)
    if m_num_int < 1 or m_num_int > 3:
        print("введите число 1 2 или 3 пж, осталось, ",err_counter, "попыток")
        err_counter += 1
        continue

    if m_num_int == 1:
        print("ввод сообщения из файла или из консоли?")
        console_or_file = input("1)консоль\n2)файл\n")
        if console_or_file.isnumeric() == False:
            print("error")
            err_counter += 1
            continue
        console_or_file_int = int(console_or_file)
        if console_or_file_int < 1 or console_or_file_int > 2:
            print("error")
            err_counter += 1
            continue

        if console_or_file_int == 1:
            msg = input("введите ваше сообщение пж ")
            print("исходное сообщение: ", msg)
            enc_msg = my_base64(msg)
            write_to_file(enc_name, enc_msg)
            print("закодированное сообщение ", enc_msg)
            dec_msg = dec_my_base64(enc_msg)
            write_to_file(dec_name, dec_msg)
            print("раскодированное сообщение ", dec_msg)
            break

        if console_or_file_int == 2:
            text_path = input("введите путь до файла с текстом, пж не ломайте ")
            msg = read_str_from_file(text_path)
            print("исходное сообщение: ", msg)
            enc_msg = my_base64(msg)
            write_to_file(enc_name, enc_msg)
            print("закодированное сообщение ", enc_msg)
            dec_msg = dec_my_base64(enc_msg)
            write_to_file(dec_name, dec_msg)
            print("раскодированное сообщение ", dec_msg)
            break
    
    if m_num_int == 2:
        print("ввод сообщения из файла или из консоли?")
        console_or_file = input("1)консоль\n2)файл\n")
        if console_or_file.isnumeric() == False:
            print("error")
            err_counter += 1
            continue
        console_or_file_int = int(console_or_file)
        if console_or_file_int < 1 or console_or_file_int > 2:
            print("error")
            err_counter += 1
            continue

        if console_or_file_int == 1:
            msg = input("введите ваше сообщение пж ")
            print("исходное сообщение: ", msg)
            enc_msg = my_base32(msg)
            write_to_file(enc_name, enc_msg)
            print("закодированное сообщение ", enc_msg)
            dec_msg = dec_my_base32(enc_msg)
            write_to_file(dec_name, dec_msg)
            print("раскодированное сообщение ", dec_msg)
            break

        if console_or_file_int == 2:
            text_path = input("введите путь до файла с текстом, пж не ломайте ")
            msg = read_str_from_file(text_path)
            print("исходное сообщение: ", msg)
            enc_msg = my_base32(msg)
            write_to_file(enc_name, enc_msg)
            print("закодированное сообщение ", enc_msg)
            dec_msg = dec_my_base32(enc_msg)
            write_to_file(dec_name, dec_msg)
            print("раскодированное сообщение ", dec_msg)
            break
    
    if m_num_int == 3:
        break
    
            

        


