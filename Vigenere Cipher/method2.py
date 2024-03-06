alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(M, K):
    E=[]
    for i in range (len(M)):
        E.append(alphabet[(int(M[i]) + int(K[i%len(key)])) % 26 ])
    print (E)

def decrypt(M, K):
    D = []
    for i in range (len(M)):
        D.append(alphabet[(int(M[i]) - int(K[i%len(key)]) + 26) % 26 ])
    print(D)

message = str(input("Input message in uppercase : "))
key = str(input("Input Key in uppercase : "))
temp = []
M=[]
K=[]

for i in range(len(message)):
        if message[i].isalpha():
            temp.append(ord(message[i]))
            M.append(temp[-1] - ord('A'))

for i in range(len(key)):
        if key[i].isalpha():
            temp.append(ord(key[i]))
            K.append(temp[-1] - ord('A'))

choice = int(input("1. Encrypt\n2. Decrypt\n"))

if (choice == 1):
    encrypt(M, K)
if (choice == 2):
    decrypt(M, K)
