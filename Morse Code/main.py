def encrypt(pt):
    code = ''
    pt = pt.lower()
    for charac in pt:
        if charac == ' ':
            code += '/'
        elif charac.isalpha() or charac.isdigit():
            code += morse_code[charac] + '/'
    return code

def decrypt(pt):
    code = ''
    temp = ''
    for charac in pt:
        if charac == '/':
            if temp in morse_code.values():
                for key, value in morse_code.items():
                    if value == temp:
                        code += key
                        break
            elif temp == '':
                code += ' '  # add space if multiple consecutive '/'
            temp = ''
        else:
            temp += charac
    return code



morse_code = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
    'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
    'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
    'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

pt = input("Enter plaintext: ")
choice = input("Type E for Encryption and D for Decryption: ")

if choice.upper() == 'E':
    encrypted_text = encrypt(pt)
    print("Encrypted text:", encrypted_text)
else:
    decrypted_text = decrypt(pt)
    print("Decrypted text:", decrypted_text)