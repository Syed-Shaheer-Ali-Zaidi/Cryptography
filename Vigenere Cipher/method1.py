def encrypt(M, K):
    E=[]
    for i in range (len(M)):
        E.append(alphabet[int(M[i])][int(K[i%len(key)])])
    print (E)

def decrypt(M, K):
    D = []
    for i in range(len(M)):
        col_index = alphabet[0].index(alphabet[int(K[i % len(K)])][0])
        row_index = alphabet[col_index].index(alphabet[0][M[i]])
        D.append(alphabet[0][row_index])
    print(D)

alphabet = [['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 
            ['B','C','D','E','F','G','H','I','J','K','L','M','N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A'], 
            ['C','D','E','F','G','H','I','J','K','L','M','N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B'], 
            ['D','E','F','G','H','I','J','K','L','M','N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B','C'], 
            ['E','F','G','H','I','J','K','L','M','N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B','C', 'D'], 
            ['F','G','H','I','J','K','L','M','N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B','C', 'D','E'], 
            ['G','H','I','J','K','L','M','N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B','C', 'D','E','F'], 
            ['H','I','J','K','L','M','N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B','C', 'D','E','F','G'], 
            ['I','J','K','L','M','N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B','C', 'D','E','F','G','H'], 
            ['J','K','L','M','N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B','C', 'D','E','F','G','H','I'], 
            ['K','L','M','N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B','C', 'D','E','F','G','H','I', 'J'], 
            ['L','M','N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B','C', 'D','E','F','G','H','I', 'J','K'],
            ['M','N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B','C', 'D','E','F','G','H','I', 'J','K','L'], 
            ['N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B','C', 'D','E','F','G','H','I', 'J','K','L','M'], 
            ['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B','C', 'D','E','F','G','H','I', 'J','K','L','M','N'], 
            ['P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B','C', 'D','E','F','G','H','I', 'J','K','L','M','N','O'], 
            ['Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B','C', 'D','E','F','G','H','I', 'J','K','L','M','N','O','P'], 
            ['R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B','C', 'D','E','F','G','H','I', 'J','K','L','M','N','O','P','Q'], 
            ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B','C', 'D','E','F','G','H','I', 'J','K','L','M','N','O','P','Q','R'], 
            ['T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B','C', 'D','E','F','G','H','I', 'J','K','L','M','N','O','P','Q','R','S'], 
            ['U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B','C', 'D','E','F','G','H','I', 'J','K','L','M','N','O','P','Q','R','S','T'], 
            ['V', 'W', 'X', 'Y', 'Z', 'A', 'B','C', 'D','E','F','G','H','I', 'J','K','L','M','N','O','P','Q','R','S','T','U'], 
            ['W', 'X', 'Y', 'Z', 'A', 'B','C', 'D','E','F','G','H','I', 'J','K','L','M','N','O','P','Q','R','S','T','U','V'], 
            ['X', 'Y', 'Z', 'A', 'B','C', 'D','E','F','G','H','I', 'J','K','L','M','N','O','P','Q','R','S','T','U','V','W'], 
            ['Y', 'Z', 'A', 'B','C', 'D','E','F','G','H','I', 'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X'], 
            ['Z', 'A', 'B','C', 'D','E','F','G','H','I', 'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
        ]

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