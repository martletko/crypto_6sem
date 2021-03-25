def str_to_bytes(my_str: str) -> str:
    return ''.join(format(ord(c), '08b') for c in my_str)

def bits2string(b: str) -> str:
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))

def bits2hex(b: str) -> str:
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*16))

def dvoich(n: int) -> str:
    b = ''
    while n > 0:
        b = b + str(n % 2)
        n = n // 2
    return b


K = ['01000010100010100010111110011000',
    '01110001001101110100010010010001',
    '10110101110000001111101111001111',
    '11101001101101011101101110100101',
    '00111001010101101100001001011011',
    '01011001111100010001000111110001',
    '10010010001111111000001010100100',
    '10101011000111000101111011010101',
    '11011000000001111010101010011000',
    '00010010100000110101101100000001',
    '00100100001100011000010110111110',
    '01010101000011000111110111000011',
    '01110010101111100101110101110100',
    '10000000110111101011000111111110',
    '10011011110111000000011010100111',
    '11000001100110111111000101110100',
    '11100100100110110110100111000001',
    '11101111101111100100011110000110',
    '00001111110000011001110111000110',
    '00100100000011001010000111001100',
    '00101101111010010010110001101111',
    '01001010011101001000010010101010',
    '01011100101100001010100111011100',
    '01110110111110011000100011011010',
    '10011000001111100101000101010010',
    '10101000001100011100011001101101',
    '10110000000000110010011111001000',
    '10111111010110010111111111000111',
    '11000110111000000000101111110011',
    '11010101101001111001000101000111',
    '00000110110010100110001101010001',
    '00010100001010010010100101100111',
    '00100111101101110000101010000101',
    '00101110000110110010000100111000',
    '01001101001011000110110111111100',
    '01010011001110000000110100010011',
    '01100101000010100111001101010100',
    '01110110011010100000101010111011',
    '10000001110000101100100100101110',
    '10010010011100100010110010000101',
    '10100010101111111110100010100001',
    '10101000000110100110011001001011',
    '11000010010010111000101101110000',
    '11000111011011000101000110100011',
    '11010001100100101110100000011001',
    '11010110100110010000011000100100',
    '11110100000011100011010110000101',
    '00010000011010101010000001110000',
    '00011001101001001100000100010110',
    '00011110001101110110110000001000',
    '00100111010010000111011101001100',
    '00110100101100001011110010110101',
    '00111001000111000000110010110011',
    '01001110110110001010101001001010',
    '01011011100111001100101001001111',
    '01101000001011100110111111110011',
    '01110100100011111000001011101110',
    '01111000101001010110001101101111',
    '10000100110010000111100000010100',
    '10001100110001110000001000001000',
    '10010000101111101111111111111010',
    '10100100010100000110110011101011',
    '10111110111110011010001111110111',

    '11000110011100010111100011110010']


H = ['01101010000010011110011001100111',
    '10111011011001111010111010000101',
    '00111100011011101111001101110010',
    '10100101010011111111010100111010',
    '01010001000011100101001001111111',
    '10011011000001010110100010001100',
    '00011111100000111101100110101011',
    '01011011111000001100110100011001']


def str_or(x,y):
    while len(x) < len(y):
        x = '0' + x
    while len(y) < len(x):
        y = '0' + y
    
    result = ''
    for i in range(len(x)):
        t1 = int(x[i])
        t2 = int(y[i])
        result += str(t1|t2)
    return result


def str_and(x,y):
    while len(x) < len(y):
        x = '0' + x
    while len(y) < len(x):
        y = '0' + y
    
    result = ''
    for i in range(len(x)):
        t1 = int(x[i])
        t2 = int(y[i])
        result += str(t1&t2)
    return result


def str_no(x):
    result = ''
    for i in x:
        if i == '1':
            result += '0'
            continue
        result += '1'
    return result


def str_mod2(x, y):
    while len(x) < len(y):
        x = '0' + x
    while len(y) < len(x):
        y = '0' + y
    
    result = ''
    for i in range(len(x)):
        t1 = int(x[i])
        t2 = int(y[i])
        result += str((t1 + t2) % 2)
    return result

# jopa dodelaj
def rotr(x,d):
    '''
    циклический сдвиг ВПРАВО! на d
    '''
    d1 = abs(d) % len(x)
    return x[-d:] + x[:-d]


def CH (x, y, z):
    t1 = str_and(x,y)
    t2 = str_no(x)
    t3 = str_and(t2, z)
    t4 = str_mod2(t1, t3)
    return t4


def shr(x, d):
    '''
    логический сдвиг (>) ВПРАВО на d
    '''
    result = ''
    for i in range(d):
        result += '0'
        t = 0
    for i in range(d,len(x)):
        result += x[t]
        t+=1
    return result

def MAJ(x, y, z):
    t1 = str_and(x, y)
    t2 = str_and(x, z)
    t3 = str_and(y, z)
    t4 = str_mod2(t1, t2)
    t5 = str_mod2(t4, t3)
    return t5

def SIGMA0(x):
    t1 = rotr(x, 2)
    t2 = rotr(x, 13)
    t3 = rotr(x, 22)
    t4 = str_mod2(t1, t2)
    t5 = str_mod2(t4, t3)
    return t5

def SIGMA1(x):
    t1 = rotr(x, 6)
    t2 = rotr(x, 11)
    t3 = rotr(x, 25)
    t4 = str_mod2(t1, t2)
    t5 = str_mod2(t4, t3)
    return t5

def sigma0(x):
    t1 = rotr(x, 7)
    t2 = rotr(x, 18)
    t3 = shr(x, 3)
    t4 = str_mod2(t1, t2)
    t5 = str_mod2(t4, t3)
    return t5

def sigma1(x):
    t1 = rotr(x, 17)
    t2 = rotr(x, 19)
    t3 = shr(x, 10)
    t4 = str_mod2(t1, t2)
    t5 = str_mod2(t4, t3)
    return t5


def add_mod2(x,y): # сложение по модулю 2^32
    t = (int(x,2) + int(y,2)) % 4294967296
    t1 = format(t, '032b')
    return t1


message = 'h'
mb = ''.join(format(ord(c),'08b') for c in message)
k = (448 - len(mb) - 1) % 512
kb = '0'*k
len_dvoich = format(len(mb), '064b')
dmb = mb + '1' + kb + len_dvoich

M_t = [dmb[x:x+32] for x in range (0, len(dmb), 32)]

w = [0]*64
for i in range(16):
    w[i] = M_t[i]

for i in range(16,64):
    t1 = add_mod2(sigma1(w[i-2]), w[i-7])

    #print(i, len(t1))
    t2 = add_mod2(sigma0(w[i-15]), w[i-16])
    #print(i, len(t2))
    t3 = add_mod2(t1, t2)
    #print(i, len(t3))
    w[i] = t3

# print(w[-1]) # тут пока все ок 

a,b,c,d,e,f,g,h = H

for t in range(64):
    t1 = add_mod2(h, SIGMA1(e))
    t2 = add_mod2(CH(e, f, g), K[t])
    t3 = add_mod2(t1, t2)
    T1 = add_mod2(t3, w[t])

    T2 = add_mod2(SIGMA0(a), MAJ(a, b, c))

    h = g
    g = f
    f = e

    e = add_mod2(d, T1)

    d = c
    c = b
    b = a
    a = add_mod2(T1, T2)

H[0] = add_mod2(a, H[0])
H[1] = add_mod2(b, H[1])
H[2] = add_mod2(c, H[2])
H[3] = add_mod2(d, H[3])
H[4] = add_mod2(e, H[4])
H[5] = add_mod2(f, H[5])
H[6] = add_mod2(g, H[6])
H[7] = add_mod2(h, H[7])

bHASH = H[0] + H[1] + H[2] + H[3] + H[4] + H[5] + H[6] + H[7]
#print(len(bHASH))

req_res = 'aaa9402664f1a41f40ebbc52c9993eb66aeb366602958fdfaa283b71e64db123'
'''
print(len(req_res))
b1 = str_to_bytes(req_res)
print(len(b1))
print()
nHASH = bits2hex(bHASH)
print(len(nHASH))
print(nHASH)
'''

t1 = int(bHASH,2)
print(t1)
print(format(t1,'0x'))

