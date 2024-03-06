def encrypt(message):
    E = []
    msg = []
    for i in range(len(message)):
        if message[i].isalpha():
            msg_code.append(ord(message[i]))
            E.append(((msg_code[-1] - ord('a')) + 3) % 26)
            msg.append(chr(E[-1] + ord('a')))
        else:
            msg.append(" ")

    print(''.join(msg))

def decrypt(message):
    DE = []
    msg = []
    for i in range(len(message)):
        if message[i].isalpha():
            msg_code.append(ord(message[i]))
            DE.append(((msg_code[-1] - ord('a')) - 3) % 26)
            msg.append(chr(DE[-1] + ord('a')))
        else:
            msg.append(" ")

    print(''.join(msg))

message = str(input("Input message in lowercase : "))
msg_code = []


choice = int(input("1. Encrypt\n2. Decrypt\n"))

if (choice == 1):
    encrypt(message)
if (choice == 2):
    decrypt(message)
