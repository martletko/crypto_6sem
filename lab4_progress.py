################################# HEX AND BINARY ###############

hexANDbinary = [
    ['0000', '0'],
    ['0001', '1'],
    ['0010', '2'],
    ['0011', '3'],
    ['0100', '4'],
    ['0101', '5'],
    ['0110', '6'],
    ['0111', '7'],
    ['1000', '8'],
    ['1001', '9'],
    ['1010', 'a'],
    ['1011', 'b'],
    ['1100', 'c'],
    ['1101', 'd'],
    ['1110', 'e'],
    ['1111', 'f']
]

b2h = dict()
for i in range(len(hexANDbinary)):
    b2h.update({hexANDbinary[i][0]:hexANDbinary[i][1]})

h2b = dict()
for i in range(len(hexANDbinary)):
    h2b.update({hexANDbinary[i][1]:hexANDbinary[i][0]})

def hex2binary(b):
    z = ''
    for c in b:
        z += h2b[c]
    return z

def binary2hex(b):
    z = ''
    parts_4 = [b[x:x+4] for x in range(0, len(b), 4)]
    #   разбиываем кусок на 16 слов по 32 бита 
    #   words_16 = [dmb[x:x+32] for x in range (0, len(dmb), 32)]
    for elem in parts_4:
        z += b2h[elem]
    return z 

######################## END OF HEX AND BINARY #################

def padding(M1b):
    k = 511 - len(M1b)
    m = '0' * k
    m = m + '1' + M1b
    return m

IV_512 = '0' * 512
h = IV_512
N = '0' * 512
EPSILON = '0' * 512



# print(h2b == md) # BITCH IT'S THE SAME I AIN'T EVER GONNA USE THIS MANUALLY BULLSHIT BITCH

b = '323130393837363534333231303938373635343332313039383736353433323130393837363534333231303938373635343332313039383736353433323130'

b1 = hex2binary(b)
b2 = padding(b1) # b2 - дополненное сообщение до 512 бит (в битовом представлении)
b3 = binary2hex(b2) 
# print(b3)
# m_check = '01323130393837363534333231303938373635343332313039383736353433323130393837363534333231303938373635343332313039383736353433323130'
# print(b3 == m_check)


def xor(x, y):
    if len(x) != len(y):
        raise ValueError
    z = ''
    for i in range(len(x)):
        z += XOR(x[i],y[i])
    return z

def XOR(x, y):
    return IF(x, NOT(y), y)

def IF(x, a, b):
    return a if x == '1' else b

def NOT(x):
    return IF(x, '0', '1')



Pi =[252, 238, 221,  17, 207, 110,  49,  22, 251, 196, 250,
    218,  35, 197,   4,  77, 233, 119, 240, 219, 147,  46,
    153, 186,  23,  54, 241, 187,  20, 205,  95, 193, 249,
    24, 101,  90, 226,  92, 239,  33, 129,  28,  60,  66,
    139,   1, 142,  79,   5, 132,   2, 174, 227, 106, 143,
    160,   6,  11, 237, 152, 127, 212, 211,  31, 235,  52,
    44,  81, 234, 200,  72, 171, 242,  42, 104, 162, 253,
    58, 206, 204, 181, 112,  14,  86,   8,  12, 118,  18,
    191, 114,  19,  71, 156, 183,  93, 135,  21, 161, 150,
    41,  16, 123, 154, 199, 243, 145, 120, 111, 157, 158,
    178, 177,  50, 117,  25,  61, 255,  53, 138, 126, 109,
    84, 198, 128, 195, 189,  13,  87, 223, 245,  36, 169,
    62, 168,  67, 201, 215, 121, 214, 246, 124,  34, 185,
    3, 224,  15, 236, 222, 122, 148, 176, 188, 220, 232,
    40,  80,  78,  51,  10,  74, 167, 151,  96, 115,  30,
    0,  98,  68,  26, 184,  56, 130, 100, 159,  38,  65,
    173,  69,  70, 146,  39,  94,  85,  47, 140, 163, 165,
    125, 105, 213, 149,  59,   7,  88, 179,  64, 134, 172,
    29, 247,  48,  55, 107, 228, 136, 217, 231, 137, 225,
    27, 131,  73,  76,  63, 248, 254, 141,  83, 170, 144,
    202, 216, 133,  97,  32, 113, 103, 164,  45,  43,   9,
    91, 203, 155,  37, 208, 190, 229, 108,  82,  89, 166,
    116, 210, 230, 244, 180, 192, 209, 102, 175, 194,  57,
    75,  99, 182]


def S(b):
    hexstring = ''
    parts_8 = [b[x:x+8] for x in range(0, len(b), 8)]
    for elem in parts_8:
        t1 = elem
        t2 = int(t1, 2)
        hexelem = hex(Pi[t2])[2:]
        hexstring += hexelem
    # print(hexstring)
    binstring = hex2binary(hexstring)
    return binstring

TAU =  [0, 8,  16, 24, 32, 40, 48, 56,
        1, 9,  17, 25, 33, 41, 49, 57,
        2, 10, 18, 26, 34, 42, 50, 58, 
        3, 11, 19, 27, 35, 43, 51, 59, 
        4, 12, 20, 28, 36, 44, 52, 60, 
        5, 13, 21, 29, 37, 45, 53, 61, 
        6, 14, 22, 30, 38, 46, 54, 62, 
        7, 15, 23, 31, 39, 47, 55, 63]

def P(b):
    result = ''
    parts_8 = [b[x:x+8] for x in range(0, len(b), 8)]
    for i in range(64):
        result += parts_8[TAU[i]]
    return result

t1 = xor(h, N)
t2 = S(t1)
# K= LPS(t1)
# print(S(t1))
t3 = P(t2)
# print(len(t3))
# print(hex2binary('8e20faa72ba0b470'))
# 1000111000100000111110101010011100101011101000001011010001110000
matrixA = [ '8e20faa72ba0b470', '47107ddd9b505a38', 'ad08b0e0c3282d1c', 'd8045870ef14980e', 
            '6c022c38f90a4c07', '3601161cf205268d', '1b8e0b0e798c13c8', '83478b07b2468764',
            'a011d380818e8f40', '5086e740ce47c920', '2843fd2067adea10', '14aff010bdd87508', 
            '0ad97808d06cb404', '05e23c0468365a02', '8c711e02341b2d01', '46b60f011a83988e',
            '90dab52a387ae76f', '486dd4151c3dfdb9', '24b86a840e90f0d2', '125c354207487869', 
            '092e94218d243cba', '8a174a9ec8121e5d', '4585254f64090fa0', 'accc9ca9328a8950', 
            '9d4df05d5f661451', 'c0a878a0a1330aa6', '60543c50de970553', '302a1e286fc58ca7', 
            '18150f14b9ec46dd', '0c84890ad27623e0', '0642ca05693b9f70', '0321658cba93c138', 
            '86275df09ce8aaa8', '439da0784e745554', 'afc0503c273aa42a', 'd960281e9d1d5215', 
            'e230140fc0802984', '71180a8960409a42', 'b60c05ca30204d21', '5b068c651810a89e', 
            '456c34887a3805b9', 'ac361a443d1c8cd2', '561b0d22900e4669', '2b838811480723ba', 
            '9bcf4486248d9f5d', 'c3e9224312c8c1a0', 'effa11af0964ee50', 'f97d86d98a327728', 
            'e4fa2054a80b329c', '727d102a548b194e', '39b008152acb8227', '9258048415eb419d', 
            '492c024284fbaec0', 'aa16012142f35760', '550b8e9e21f7a530', 'a48b474f9ef5dc18',
            '70a6a56e2440598e', '3853dc371220a247', '1ca76e95091051ad', '0edd37c48a08a6d8', 
            '07e095624504536c', '8d70c431ac02a736', 'c83862965601dd1b', '641c314b2b8ee083']

'''
t4 = binary2hex(t3)
#print(t4)

# print(len(t4))
parts_2 = [t4[x:x+2] for x in range(0, len(t4), 2)]
# print(parts_8)
# t5 = hex2binary(parts_8[0])
# print(t5)
print(len(parts_2))


# s1 = 'fcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfc'
# print(len(s1)) # 128 длина в 16-ричной системе
# print(s1 == t4)
'''

def xor_arr(arr):
    result = hex2binary(arr[0])
    for i in range(1, len(arr), 1):
        t = hex2binary(arr[i])
        result = xor(result, t)
    return result

def L(arr):
    parts_64_bit_of_t3 = [arr[x:x+64] for x in range(0, len(arr), 64)]
    # print(len(parts_64_bit_of_t3[0]))
    temp_big = []
    for part in parts_64_bit_of_t3:
        temp = []
        i = 0
        for bit in part:
            if bit == '0':
                temp.append('0000000000000000')
            if bit == '1':
                temp.append(matrixA[i])
            i += 1
        temp_big.append(temp)
    # print(len(temp_big))
    # print(temp_big[0])

    k = ''
    for i in range(len(temp_big)):
        k += xor_arr(temp_big[i])

    k1 = binary2hex(k)

    # k2 = 'b383fc2eced4a574b383fc2eced4a574b383fc2eced4a574b383fc2eced4a574b383fc2eced4a574b383fc2eced4a574b383fc2eced4a574b383fc2eced4a574'
    # print(k1==k2) # true

    # k1 = xor_arr(temp_big[0])
    # print(binary2hex(k1))
    return k1
t4 = L(t3)




        












